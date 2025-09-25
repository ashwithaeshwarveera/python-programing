def greet():
    print("welcome to python:")
greet()


def greet_user(name):
    print("hello,",name)
greet_user("ashu")


def add(a,b):
    sum = a + b
    print(sum)
add(2,3)    


def introduce(name,age):
-    print(f"my name is {name} and i am {age} year old")
introduce(name = "ashwitha",age = 18)


def introduce(name,age):
    name = name
    age = 18
    print(name,end = " ")
    print(age)
introduce("ashu",18)


def greet(name = 'guest'):
    print("hello",name)
greet()
greet("vaishu")


x = 100
def fun():
    y = 50
    print("inside function, x =",x) #access globally
    print("inside function, y =",y) #access locally

fun()    
print("outside function, x =",x) #access globally

