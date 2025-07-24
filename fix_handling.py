def get_integer_input():
    while True:
        try:
            user_input = int(input("enter a valid integer: "))
            return user_input
        except ValueError :
            print("Error : Invalid integer value.please try again.")     
def withdraw(val):
    if val >1000:
        raise ValueError("Entered amount exceeded current balance !")
   

try:
    valid_integer =get_integer_input()
    print("valid integer entered: ", valid_integer)
    withdraw(valid_integer)
except ValueError as e:
    print("An error occurred: ",str(e))
    #print(f"Error : {e}") 

