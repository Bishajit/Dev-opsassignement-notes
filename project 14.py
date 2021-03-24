class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi,I am {self.name}")


new_name = Person("New Name")
print(new_name.name)
new_name.talk()

bob_name = Person("Bob Name")
print(bob_name.name)
bob_name.talk()
