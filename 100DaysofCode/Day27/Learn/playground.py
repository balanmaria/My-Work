def add(*args):
    print(type(args))
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum
    #return sum(args)

# print(add(1,2,3,4,5,6,7,8))
#
# print(add(1,2,3,4,5,6))

def calculate(n, **kwargs):
    #print(kwargs)
    #print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)
    n+= kwargs["add"]
    n*= kwargs["multiply"]

    print(n)

    print(kwargs["add"])

#calculate(2, add = 3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make=kw.get("make")
        self.model=kw.get("model")

my_car= Car(make="Nissan", model="GT-8")
print(my_car.model)