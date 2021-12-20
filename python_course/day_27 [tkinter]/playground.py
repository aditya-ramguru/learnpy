def add(*args):  # args is a tuple
    s = 0
    for i in args:
        s += i
    print(s)


# add(1,2,3,4,5,6,7)


def calculate(n, **kwargs):
    n += kwargs['add']  # dictionary
    n *= kwargs['multiply']
    return n


# print(calculate(2, add=3, multiply=5))


class Car:

    def __init__(self,**kw):
# incase user doesnt enter any keyword argument the get function
# allows us to bypass the error by assigning it as None
        self.make = kw.get('make')
        self.model = kw.get('model')


my_car = Car(make='nissan', model='gtr')
print(my_car.make)
