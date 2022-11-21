import random
import os

import pathlib

from data.data import Person
from faker import Faker


faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():  # создаем генератор человека
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )


def generated_file():
    #path = rf'C:\Users\user\PycharmProjects\myprojectT\filetest{random.randint(0, 999)}.txt'
    #file = open(path, 'w+')
    #file.write(f'TestMan{random.randint(0, 999)}')
    #file.close()

    #path = tmpdir.mkdir("mydir").join(f"test{random.randint(0, 999)}")
   # path.write(f'TestMan{random.randint(0, 999)}')
    base_dir = pathlib.Path(f'test{random.randint(0, 999)}.txt')
    base_dir.write_text(f'TestMan{random.randint(0, 999)}')
    return base_dir
