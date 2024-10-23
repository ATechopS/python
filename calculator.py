a=int(input("enter first number: "))
b=int(input("enter second number: "))
sank=input("enter what you want to do: ")


if(sank=="+") :
    print(a+b)

elif(sank=="-"):
    print(a-b)
elif(sank=="x"):
    print(a*b)
elif(sank=="/"):
    print(a/b)
else :
     print(a%b)
    
