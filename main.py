from page import page
from hash.ex_hash import EH
from student import student

__author__ = 'kamil'

filename = 'student.txt'
mydb = page(filename)
kamil = student(1, "Kamil", "k.salakhiev@innopolis.ru", "Yelabuga. Mira 47")
bro = student(2, 'Brot', 'bro@innopolis.ru', 'Kazan. Somewhere 32')
mydb.insert(kamil)
mydb.insert(bro)

kamil_str = kamil.get_string()
print(kamil_str)
print(kamil_str[16])
