def func(a, b):
    def wrap():
        print('some happen')
        print("That's so easy!")
        return a + b

    return wrap

qw = func(2, 5)
print(qw())


