def fib(n):
    #proverq dali n e 0 ili 1 zashtoto 0-voto chislo ot fibonachi e 0, a 1-voto - 1
    if n <= 1:
        return n
    x = 0
    y = 1
    #i se uvelichava dokato stane ravno na n; izchislqva dqsnata strana(y, x+y) i gi prisvoqva ednovremenno - x poluchava staroto y, y poluchava staroto x+y
    for i in range(n):
        x, y = y, x + y
    return x

def fib_rec(n):
    #proverq dali n e 0 ili 1 zashtoto 0-voto chislo ot fibonachi e 0, a 1-voto - 1
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

print(fib(5))
print(fib_rec(8))