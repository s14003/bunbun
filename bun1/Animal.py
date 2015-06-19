
class Animal:
    def __init__(self, name, voice):
        self.name = name
        self.voice = voice

    def say(self):
        print(self.voice)

class Dog(Animal):
    def __init__(self,name='ななし',voice='（Ｕ＾ω＾）わんわんお！',breed='柴犬'):
        Animal.__init__(self,name,voice)
        self.breed = breed
    def print_info(self):
        print('名前:',self.name,'犬種:',self.breed)

class Turtle(Animal):
    def say(self):
        print("・・・・。")

class Cat(Animal):
    pass

if __name__ == '__main__':
    puppy = Dog()
    puppy.say()
    puppy.print_info()