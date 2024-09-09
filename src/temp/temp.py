class Human():
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, power):
        self.name = name
        self.power = power

if __name__ == "__main__":
    human = Human("John")
    man = Man(123)
    print(human)
    print(man)