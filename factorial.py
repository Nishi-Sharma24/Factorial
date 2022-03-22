#Find the factorial of a number.
n=int(input("Enter a number:"))
f=1      
for x in range(n,0,-1):
      f*=x
print("The factorial is",f)
input()
