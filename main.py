from page import page
from hash.ex_hash import EH
from student import student
import names
import faker
import pickle

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
    # mydb = EH(filename)
    # studs = []
    # for i in range(1, 100):
    #     studs.append(get_random_student(i))
    #
    # for stud in studs:
    #     mydb.put(stud._id, stud)
    #
    # save(mydb)
    mydb = load()
    print(mydb.get(5))


db_test()
# page_test()