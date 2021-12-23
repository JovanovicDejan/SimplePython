#Count the number of sing change in user input's

n = int(input("How many numbers do you want to enter? "))
list_of_user_inputs = []
counter = 0

for i in range(n):
    user_input = float(input(f"Enter {i+1} number"))
    list_of_user_inputs.append(user_input)
    if list_of_user_inputs[i] >= 0 and list_of_user_inputs[i-1] < 0 or list_of_user_inputs[i] < 0 and list_of_user_inputs[i-1] > 0:
        counter += 1
print(f"Number of sing change in user inputs {counter} ")

# for i in range(n):
#     user_input = float(input(f"Enter {i+1} number "))
#     list_of_user_inputs.append(user_input)

# for j in range(n-1):
#     if list_of_user_inputs[j] >= 0 and list_of_user_inputs[j-1] < 0 or list_of_user_inputs[j] < 0 and list_of_user_inputs[j-1] > 0:
#         counter += 1
# print(f"Number of sing change in user inputs {counter} ")
