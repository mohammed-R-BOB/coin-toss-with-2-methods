import random
print("welcome to coin toss game!!")
print("which method you want to use?")
print("method 1: random.randiant()")
print("method 2: random.random()")
# piking up a method
method = input("enter your choice (1 or 2): ")
method = int(method)
# method number 1 uses random.randint()
if method == 1:

    user_input1 = input("enter your choice (head or tail): ")
    user_input1 = user_input1.lower()
    random_num1 = random.randint(0, 1)
    if random_num1 == 0:
        computer_choice = "head"
    else:
        computer_choice = "tail"
        if user_input1 == computer_choice:
            print("you gussed it right!!")
            print("your choice was:", user_input1)
            print("computer choice was: ", computer_choice)
        else:
            print("you gussed it wrong!!")
            print("your choice was:", user_input1)
            print("computer choice was: ", computer_choice)
# method number 2 uses random.random()
elif method == 2:
    user_input2 = input("enter your choice (head or tail):")
    user_input2 = user_input2.lower()
    random_num2 = random.random()
    if random_num2 >= 0.5:
        computer_choice2 = "head"
    else:
        computer_choice2 = "tail"
        if user_input2 == computer_choice2:
            print("you gussed it right!!")
            print("your choice was:", user_input2)
            print("computer choice was: ", computer_choice2)
        else:
            print("you gussed it wrong!!")
            print("your choice was:", user_input2)
            print("computer choice was: ", computer_choice2)
# if the method number is not 1 or 2
else:
    print("invalid method number, please try again")
