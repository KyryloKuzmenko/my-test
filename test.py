def func(f):
    def wrap():
        print('some happen')
        f()
        print("That's so easy!")

    return wrap
@func
def func2():
    print("my message")

func2()

