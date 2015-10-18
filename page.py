__author__ = 'kamil'


class page:
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

    def __init__(self, filename):
        self._filename = filename
        f = open(filename, 'r+')
        header_str = self.read_until_char(f, '#')
        header = header_str.split('$')
        print(header)
        f.close()
        first = header[0]
        count_str = first[len('header'):len('header') + 3]
        count_str = count_str.strip()
        count = int(count_str)
        self._count = count
        self._end_pointer = int(header[1])
        lengths_strs = header[2:]
        for length_str in lengths_strs:
            if length_str != '#':
                self._lengths.append(int(length_str))
        self._occupied_space = self._data_offset

    def fit(self, student):
        return student.get_string() < (self._total_space - self._occupied_space)

    def insert(self, student):
        f = open(self._filename, 'r+')
        f.seek(self._end_pointer)
        stud_str = student.get_string()
        f.write(stud_str)

        #increase counter
        self._count += 1
        f.seek(len('header'))
        count_str = self.add_spaces_to_size(str(self._count),3)
        f.write(count_str)

        #update end pointer
        self._end_pointer += len(stud_str)
        f.seek(len('header???$'))
        f.write(str(self._end_pointer))

        #update the lengths
        f.seek(0)
        header = self.read_until_char(f, '#')
        print('header = ', header)
        f.seek(len(header)-1)
        f.write(str(len(stud_str)))
        f.write('$#')
        f.close()

        self._occupied_space += len(stud_str)