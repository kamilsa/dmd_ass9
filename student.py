__author__ = 'kamil'

class student:
    _id = int() # max = 999
    _name = ""
    _email = ""
    _address = ""

    def __init__(self, id = 0, name = "", email = "", address = "", to_parse = None):
        if to_parse == None:
            self._id = id
            self._name = name
            self._email = email
            self._address = address
        else:
            tokens = to_parse.split('$')
            self._id = int(tokens[0])
            self._name = tokens[3]
            self._email = tokens[4].strip()
            self._address = tokens[5]

    def get_string(self):
        mail_offset = 2 + 1 + 2 + 1 + 3 + 1 + len(self._name) + 1
        address_offset = mail_offset + 30 + 1
        address_offset += 2 + 1
        res = ""
        id_str = str(self._id)
        for i in range(0,3-len(id_str)):
            id_str += " "
        res += id_str
        res += '$'
        res += str(mail_offset)
        res += '$'
        res += str(address_offset)
        res += '$'

        res += self._name
        res += '$'
        email = self._email
        for i in range(0, 30-len(self._email)):
            email += ' '
        res += email
        res += '$'
        res += self._address
        res += '$'
        return res

    def __repr__(self):
        return {self._id, self._name, self._email, self._address}.__repr__()