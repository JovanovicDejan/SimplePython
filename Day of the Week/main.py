#Count certain days of the week

user_input = int(input("Enter one number between 1 and 7 to see what is that day: "))
days = [1,2,3,4,5,6,7]

while user_input not in days:
        print("You enter the wrong number please try again! ")
        user_input = int(input("Enter one number between 1 and 7 to see what is that day: "))
if user_input == 1:
    print("It's a Monday ")
elif user_input == 2:
    print("It's a Tuesday")
elif user_input == 3:
    print("It's a Wednesday")
elif user_input == 4:
    print("It's a Thursday")
elif user_input == 5:
    print("It's a Friday ")
elif user_input == 6:
    print("It's a Saturday")
elif user_input == 7:
    print("It's a Sunday")
