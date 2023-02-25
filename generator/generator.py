import random
from data.data import Person
from faker import Faker

# faker_en = Faker('En')
faker_ru = Faker('ru_RU')


def generated_person():
    yield Person(
        email=faker_ru.email(),
        # password=faker_ru.password(),
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name()+ ' ' + faker_ru.middle_name(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),

        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10,99),
        salary=random.randint(10000,99000),
        department=faker_ru.job()
    )


# def generated_file():
#     path = rf'C:\Users\Александр\PycharmProjects\pythonAutoTest1\test_fail{random.randint(10, 100)}.txt'
#     file = open(path,  'w')
#     file.write(f'HelloWord{random.randint(20, 100)}')
#     file.close()
#     return path
