# lessonl -- 03
info = {
    "name": "mishi",
    "age": 17,
    "city": "karachi",
    "course": "agentica-ai",
    "marks": 650,
}
# q---3
print("city" in info)
# q---1

for information in info:
    print(information)
    # q--2
info["grade"] = "A++"
print(info)
# q--4
students = {
    " student1": {"name": "amna", " roll_no": 23, " city": "islamabad"},
    "student_2": {"name": "nehau", " roll_no": 24, " city": "karachi"},
    "student_3": {"name": "mishkat", " roll_no": 25, " city": "karachi"},
}
for student_key, info in students.items():
    print(f"\n---{student_key} ----")
    for key, value in info.items():
        print(f"{key} : {value}...")
    # print(info)
# q--5

marks = {"Math": 95, "English": 88, "Python": 99}
for value in marks.values():
    print(value)
print(sum(marks.values()) / len(marks))


# lesson 04
# q--1
def add(a, b):
    return a + b


# add(2,3)
print(add(5, 19))


# q--2
def greet(name):
    return f"hello , how are you {name}!!"


print(greet("nehu"))


# q--3
def grade(marks):
    if marks >= 90:
        return f"your grade is A+ with {marks}"

    elif marks >= 80:
        return f"your grade is A with {marks}"
    elif marks >= 70:
        return f"your grade is B+ with {marks}"
    elif marks >= 60:
        return f"your grade is B with {marks}"
    elif marks >= 50:
        return f"your grade is C with {marks}"
    else:
        return "fail"


print(grade(50))


# q --- 4
def avrage(numbers):
    return sum(numbers) / len(numbers)


print(avrage([10, 20, 30]))


# q--5
def func(name, city="karahci"):
    return f"hello {name},in city {city}"


print(func("nehu"))

# lesson 6 classees
# class faculty:
#     def putdata(self):
#         self.id = input("enter your  id")
#         self.name = input("enter you name")
#     def display(self):
#         print(f"your id is {self.id}")
#         print(f"your name is {self.name}")
# a = faculty()
# a.putdata()
# a.display()


# q--1
class Car:
    def __init__(self, name, brand, model, speed):
        self.name = name
        self.brand = brand
        self.model = model
        self.speed = speed

    def info(self):
        print(
            f"your car name  is {self.name} , \n the brand is{self.brand},\n  the model is {self.model}, \n the speed is {self.speed}"
        )

    def speed_checker(self):
        if self.speed >= 150:
            return "Fast"
        else:
            return "slow"


func1 = Car("bmw", "toyota", "tutu", 180)
func2 = Car("bmw", "toyota", "tutu", 120)
func3 = Car("bmw", "toyota", "tutu", 2000)
func1.info()
print(func1.speed_checker())
func2.info()
print(func2.speed_checker())
func3.info()
print(func3.speed_checker())


# q--2
class bankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        print(f"tumhara current balance ye ha {amount}")
        self.balance = amount + self.balance
        print(f"your amount is {amount}  aagaye ha !!")
        print(f"ab tumhara balance y ha {self.balance}")

    def withdraw(self, amount):
        print(f" your balance is {self.balance}")
        if amount > self.balance:
            return "itna  balance nhn ha"
        else:
            self.balance = self.balance - amount
            print(f"{amount} itnay paisay nikal gaye")
            print(f"your current balance is {self.balance}")

func = bankAccount("nehu", 5000)
func.deposit(5000)
func.withdraw(20)
# q---3
class Student:
    def __init__(self,name,age,city,marks):
        self.name = name
        self.age = age
        self.city = city
        self.marks = marks
    def grade(self):
        if self.marks >= 90:
            return f"your grade is A+ with {self.marks}"
        elif self.marks >= 80:
            return f"your grade is A with {self.marks}"
        elif self.marks >= 70:
            return f"your grade is B+ with {self.marks}"
        elif self.marks >= 60:
            return f"your grade is B with {self.marks}"
        elif self.marks >= 50:
            return f"your grade is C with {self.marks}"
        else:
            return "fail"
gradess = Student("nehuu",17,"lahore",100)
print(gradess.grade())

# lesson # 5 Libraries
print("--------------------------------------------------")
# q--1
import math
print(math.sqrt(2))
print(math.pow(2,2))
print(math.floor(9.7))
print(math.ceil(9.7))
# q --- 2
import random
print(random.randint(1,100))
arr = ["apple", "mango","orange"]
print(random.choice(arr))
random.shuffle(arr)
print(arr)
# q---3
import datetime
current = datetime.datetime.now()
print(current)
print(current.year)
print(current.month)
print(current.day)

print("all lessons done!!")

