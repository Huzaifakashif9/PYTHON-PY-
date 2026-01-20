#  Class kya hoti hai?

# Class = blueprint / design

#  Object kya hota hai?

# Object = class ka real instance

# Example (Real Life)

# Class = Student
# Object = Ali, Ahmed, Huzaifa



# Constructor = object banne ke sath auto run hone wala function

# step:1) CONSTRUCTOR (__init__)
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age


s1=student("huzaifa",18)
print(s1.name,s1.age)

# step 2) METHODS (Functions inside class)
class car:
    def __init__(self,name,model):
        self.name=name
        self.model=model

    def introduce(self):
        print("my car name is",self.name)
        print("my car model is",self.model)
c1=car("vitz",2015)
c1.introduce()

# step3) ENCAPSULATION (Data Protection)
class bank:
    def __init__(self):
        self.name="huzaifa" 
        self.__balance=5000
    def show_balance(self):
        print("balance is",self.__balance)
b1=bank()
b1.show_balance()

# part 4): INHERITANCE (Parent → Child)
class accounts:
    def __init__(self,name):
        self.name=name
    def welcome(self):
        print("helo welcome",self.name)
    
class savinigaccount(accounts):
    def __init__(self,name,balance):
        super().__init__(name)
        self.balance=balance
    def okay(self):
        print(self.name,"your balance is",self.balance)

hk=savinigaccount("huzaifa",1000)
hk.welcome()
hk.okay()

# part 5) POLYMORPHISM (Same Function, Different Work)
class Bird:
    def sound(self):
        print("Bird sound")

class Parrot(Bird):
    def sound(self):
        print("Parrot talks")

class Crow(Bird):
    def sound(self):
        print("Crow caws")

birds = [Parrot(), Crow()]

for b in birds:
    b.sound()