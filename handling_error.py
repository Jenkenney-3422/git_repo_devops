





def get_int_input():
    while True:
        try:
            val =int(input("enter the withdraw amount:  "))
            return val
        except ValueError:
            print("the withdraw amount (val) is not valid input only integer ...!")
            
                   
def withdraw(val):
    try:
        if val > 1000:
            print("the entered amount exceeded the current user balance")


try:
    valid_input =get_int_input()
    print(f"Entered a valid input",valid_input)
    withdraw(valid_input)
except ValueError as e:
    print(f"Error accured : ",str(e))

