def func(f):
    def wrap(a, b):
        print('First print')
        print(f())
        print('Thirt print')
        return a + b
        
    return wrap

@func
def qwer():
    s = 'Second print'
    return s


print(qwer(2, 5))

