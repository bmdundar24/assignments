"""
def my_min(*args):
    return min(args)
print(my_min(-100))

def my_sum(*args):
    return sum(args)
"""
n = int(input("Enter the n value for Factorial:"))
def factoriall(n):
    if n<=1:
        return 1
    else:
        return n*factoriall(n-1)

print(factoriall(n))
