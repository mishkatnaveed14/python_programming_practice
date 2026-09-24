# q--4 
# my library 

def add(a, b):
    return a + b

def greet(name):
    return f"hello , how are you {name}!!"


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


