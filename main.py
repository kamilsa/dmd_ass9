from Profiler import Profiler
from page import page
from hash.ex_hash import EH
from student import student
import names
import faker
import pickle
import time

__author__ = 'kamil'


def save(hb):
    pickle.dump(hb, open('save.p','wb'))

def load():
    hb = pickle.load(open('save.p', 'rb'))
    return hb

def get_random_student(id):
    fake = faker.Faker()
    name = names.get_full_name()
    first_last = name.lower().split(' ')
    email = first_last[0][0] + '.' + first_last[1] + '@innopolis.ru'
    address = fake.address().replace('\n', ' ')


    return student(id, name, email, address)


def page_test():
    filename = 'student.txt'
    page1 = page(filename, 0)
    studs = []
    for i in range(1, 5):
        studs.append(get_random_student(i))

    for stud in studs:
        page1.insert(stud)

    page1.setDoubling(2)


def db_test():
    filename = 'student.txt'
    mydb = EH(filename)
    studs = []
    for i in range(1, 10000):
        if i % 100 == 0:
            print('#',i)
        studs.append(get_random_student(i))
    print('inserting...')
    with Profiler() as p:
        for stud in studs:
            mydb.put(stud._id, stud)
            print('#',stud._id,'added')

    save(mydb)
    # mydb = load()
    print(mydb.get(6))

def generate_dataset():
    filename = 'to_put.txt'
    f = open(filename, 'w')
    for i in range(1, 10000):
        if i % 100 == 0:
            print('#',i)

        student = get_random_student(i)
        to_ins = str(student._id) + ' ' + student._name + ' ' + student._address + ' ' + student._email + '\n'
        f.write(to_ins)
    f.close()

def get_dataset():
    filename = 'to_put.txt'
    f = open(filename, 'r')
    line = f.readline()
    toks = line.split(' ')

generate_dataset()
# db_test()
# page_test()