from dataclasses import dataclass


# создание рандомных данных
@dataclass
class Person:
    email: str = None
    password: str = None
    firstname: str = None
    lastname: str = None
    full_name: str = None
    current_address: str = None
    permanent_address: str = None
    mobile: str = None
    subject: str = None
    age: int = None
    salary: int = None
    department: str = None
