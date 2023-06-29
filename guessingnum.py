name = input("What is your name:-")
print(name)
print("Hey!",name,"So I have a game for you\n This game name is Guess the number\n You have to guess the number from 1 to 10")

num = int(input())

if(num<5):
    print("Your number is small")
    print("So!",name,"Your number is",num)
elif(num>5):
    print("Your number is big")
    print("So!",name,"Your number is",num)
else:
    print("Try again")