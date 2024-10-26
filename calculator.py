a=int(input("enter first number: "))
b=int(input("enter second number: "))
sank=input("enter what you want to do: ")

# here created conditional statement according to input given by user what user want to 
def text():
    print("Your Answer is here:")


if(sank=="+") :
    text()
    print(a+b)

elif(sank=="-"):
    text()
    print(a-b)
elif(sank=="x"):
    text()
    print(a*b)
elif(sank=="/"):
    text()
    print(a/b)
else :
     text()
     print(a%b)
    
