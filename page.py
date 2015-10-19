from student import student

__author__ = 'kamil'


class page:
    _page_offset = 0
    _filename = ''
    _count = 0
    _data_offset = 100
    _end_pointer = 0
    _total_space = 500
    _occupied_space = 0

    _lengths = []
    def add_spaces_to_size(self, string, size):
        res = string
        for i in range(0, size-len(string)):
            res += ' '
        return res

    def read_until_char(self, f, ch):
        res = ""
        while True:
            new_ch = f.read(1)
            res += new_ch
            if (new_ch == ch):
                break
        return res

    def __init__(self, filename, page_offset):
        self._filename = filename
        self._page_offset = page_offset

        f = open(filename, 'r+')
        f.seek(page_offset)
        check_str = f.read(len('header'))
        if check_str != 'header':
            f.seek(page_offset)
            f.write('header0  $100  $0  $#')
        f.seek(page_offset)
        header_str = self.read_until_char(f, '#')
        header = header_str.split('$')
        # print(header)
        first = header[0]
        count_str = first[len('header'):len('header') + 3]
        count_str = count_str.strip()
        count = int(count_str)
        self._count = count
        self._end_pointer = int(header[1])
        dbl_str = header[2]
        self.d = int(dbl_str)
        self.key_list = []
        lengths_strs = header[3:]
        self._lengths = []
        for length_str in lengths_strs:
            if(length_str.strip() != '#'):
                self._lengths.append(int(length_str))
        prev = page_offset + self._data_offset
        for length in self._lengths:
            f.seek(prev)
            id_str = f.read(3)
            id_int = int(id_str)
            self.key_list.append(id_int)
            prev += length
        # for length_str in lengths_strs:
        #     if length_str.strip() != '#':
        #         # self._lengths.append(int(length_str))
        #         f.seek(prev)
        #         id_str = f.read(3)
        #         id_int = int(id_str)
        #         self.key_list.append(id_int)
        #         prev += int(length_str)

        self._occupied_space = self._end_pointer

        f.close()

    def fit(self, a_student):
        return len(a_student.get_string())+self._occupied_space < self._total_space

    def insert(self, student):
        f = open(self._filename, 'r+')
        f.seek(self._page_offset + self._end_pointer)
        stud_str = student.get_string()
        f.write(stud_str)

        #increase counter
        self._count += 1
        f.seek(self._page_offset + len('header'))
        count_str = self.add_spaces_to_size(str(self._count),3)
        f.write(count_str)

        #update end pointer
        self._end_pointer += len(stud_str)
        f.seek(self._page_offset + len('header???$'))
        f.write(str(self._end_pointer))

        #update the lengths
        f.seek(self._page_offset)
        header = self.read_until_char(f, '#')
        f.seek(self._page_offset + len(header)-1)
        f.write(str(len(stud_str)))
        f.write('$#')
        f.close()
        self._lengths.append(len(stud_str))

        self._occupied_space += len(stud_str)
        self.key_list.append(student._id)

    def get(self, key):
        print(self._lengths)
        f = open(self._filename, 'r+')
        prev = self._page_offset + self._data_offset
        for length in self._lengths:
            f.seek(prev)
            record_str = f.read(length)
            id = int(record_str[:3])
            if (id == key):
                f.close()
                return student(to_parse=record_str)
            prev += length
        f.close()

    def setDoubling(self, d):
        self.d = d
        f = open(self._filename, 'r+')
        header = self.read_until_char(f, '#')
        tokens = header.split('$')
        # print(tokens)
        offset = len(tokens[0]) + 1 + len(tokens[2]) + 1 + 2
        # print(offset)
        f.seek(offset)
        to_set = self.add_spaces_to_size(str(d), 3)
        f.write(to_set)
        f.close()

    def fetch(self):
        f = open(self._filename, 'r+')
        f.seek(self._page_offset)
        res = f.read(self._total_space)
        f.close()
        return res