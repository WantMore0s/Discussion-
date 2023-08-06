import json 

def repeat_file():
    """Gather user info, stores in a file, then reads the file and
    displays the contents of the file to user."""
    #Ask user for file name.
    name_file = input("Which file are would you like to choose? ")
    #Store the user input as a json file.
    filename = 'name_file.json'
    #Ask user for their name.
    user_name = input("Please enter your name: ")
    #Ask user for their address
    user_addy = input("Please enter your address including city, state and zip code. (Example: 555 Main st. New York, New York 55555): ")
    #Ask user for their phone number. 
    user_phone = input("Please enter a valid phone number including area code (Example: 555-555-5555): ")
    #Store information gathered from user to a variable.
    user = f"{user_name},{user_addy},{user_phone}"
    #Open file and write the user info from program to the file.
    with open(filename, 'w') as f:
      json.dump(user, f)
    #Open file and load user info from the file created. 
    with open(filename) as f:
      filename = json.load(f)
    #Display contents of the file to the user. 
      print(f"{filename}")
    #Program ends.


#Call the program.
repeat_file()
