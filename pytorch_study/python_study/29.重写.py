class Animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"一支叫${self.name}的动物在跑")

    def sleep(self):
        print(f"一支叫${self.name}的动物在睡觉")


class Dog:

    def run(self):
        print("狗跑")


dog = Dog()

print(dog.run())
