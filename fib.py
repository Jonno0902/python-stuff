def fib(x):
    if x==0:
        return 0
    elif x<2:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def fibSequence(i):
    for x in range(i):
        print(fib(x))
