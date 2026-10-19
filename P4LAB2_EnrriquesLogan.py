# Logan Enrriques
# 10/19/2026
# P4LAB2
# Use while loop and for loop together

# Get value integer from the user #
# Determine if integer is positive or negative #
# If number is negative, display multiplication table #
# If number is postive, tell user program cannot accept it #
# Ask user to run again #

run_again = 'yes'

while run_again != "no":

    user_num = int(input("Enter an integer: "))
    if user_num >= 0:
        for item in range(1, 12+1):
            print(f"{user_num} * {item} = {user_num * item}")

    else:
        print("This program does not handle negative values.")
    run_again = input("Would you like to run the program again? ")
# Loop has broken. User said "no" #
print("Program is ending...")