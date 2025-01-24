class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        print(f"Hello {self.name}")

class Worker(Human):
    def __init__(self, name, age, work):
        super().__init__(name, age)
        self.work = work

h1 = Human("EVGEN", 37)
h2 = Worker("DIMA", 8, "super_work")
h1.greetings()
h2.greetings()
