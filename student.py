__author__ = 'kamil'

class student:
    _id = int() # max = 999
    _name = ""
    _email = ""
    _address = ""

    def __init__(self, id, name, email, address):
        self._id = id
        self._name = name
        self._email = email
        self._address = address

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