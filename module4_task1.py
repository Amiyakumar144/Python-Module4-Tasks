n=int(input("enter the nuber  factorial check"))

def factotial(n):
    if n<2:
        return 1
    else:
        return n*(factotial(n-1))

result=factotial(n)
print(f"the factorial is : {result}")