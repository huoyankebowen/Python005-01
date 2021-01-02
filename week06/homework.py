from abc import ABCMeta, abstractmethod

shapes={'小':1,'中等':2,'大':3}

class Zoo(object):
    def __init__(self,name):
        self.name=name
        self.animals=set()
    def add_animal(self,animal):        
        self.animals.add(animal)
        self.__dict__[animal.__class__.__name__]=animal.__class__.__name__

        for an in self.animals:
            print(an.name)
        
    

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,form,shape,character) :
        self.form=form
        self.shapevalue=shapes[shape]
        self.character=character
        if (self.shapevalue>=2 and self.form=='食肉' and self.character=='凶猛' ):
            self.ferocious=True
        else:
            self.ferocious=False        

class Cat(Animal):
    sound='miao'
    def __init__(self,name,form,shape,character):
        self.name=name
        super().__init__(form,shape,character)
        self.suit_pet=not self.ferocious
        


class Dog(Animal):
    sound='wang'
    def __init__(self,name,form,shape,character):
        self.name=name
        super().__init__(form,shape,character)
        self.suit_pet=not self.ferocious

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(have_cat)