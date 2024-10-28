class Person:
    name: str
    age: int
    address: str

    def __init__(self, name: str, age: int, address: str):
        self.name=name
        self.age=age
        self.address=address

    def display_person_info(self) -> None:
        print(f"Name: {self.name}\tAge: {self.age}\tAddress: {self.address}")
