#Create a virtual garage. 
#Define vehicle class.
class Vehicle:
  """Create a class for vehicles."""
  def __init__(self, make, model):
    self.make = make
    self.model = model
#Define the get of the make and model of vehicle. 
  def get_make_model(self):
    """Prints the make and model of the vehicle."""
    print(f"The make is: {self.make}")
    print(f"The model is: {self.model}")
   

#Define a Car class that inherits from Vehicle.
class Car(Vehicle):
  """A car class that lets user enter the amount of car doors."""
  #Add the attribute cardoors.
  def __init__(self, make, model, cardoors):
    """Initialize the parent class."""
    super().__init__(make, model)
    self.cardoors = cardoors
#Define the get of the make, model and car doors.
  def get_make_model(self):
    """Prints the number of car doors along with make and model."""
    #Print the number of car doors alond with make and model.
    print(f"\nThis car has {self.cardoors} doors.")
    print(f"The make is: {self.make}")
    print(f"The model is: {self.model}")
    
#Define the pick up class that inherits from Vehicle.
class Pickup(Vehicle):
  """A pickup class that lets user enter the length of truck bed."""
  #Add the attribute bed lenth.
  def __init__(self, make, model, bed_length):
    """Initialize the parent class."""
    super().__init__(make, model)
    self.bed_length = bed_length
#Define the get of the Pickup class.
  def get_make_model(self):
    """Prints the bed length along with the make and model."""
    #Print the bed lengh along with the make and model. 
    print(f"\nThis truck bed length is {self.bed_length} feet long.")
    print(f"The make is: {self.make}")
    print(f"The model is: {self.model}")

#Create a greeting.
print("Hello, Welcome to Howard's Virtual Garage.")
#Create a loop so the user can continue as long as they want.
#Create a menu style choice for user input.
while True:
  #Convert user input into an interger.
  choice = int(input("\nEnter 1 to create a car, 2 to create a pickup, or 3 to quit: "))
  #Gather user input and react depending on the user's input.
  #Create multiple if statements for the users choice.
  if choice == 1:
    #First if statement will represent the class Car.
    make = input("\nPlease enter the make of your car: ")
    model = input("\nPlease enter the model of your car: ")
    cardoors = input("\nEnter the number of doors on your car: ")
    #Gather user input, create a new car based on that input.
    new_car = Car(make, model, cardoors)
    #print new car with the get from the Car class.
    new_car.get_make_model()
    
  elif choice == 2:
    #This choice and elif statement will represent the Pickup class.
    bed_length = input("\nEnter the length of the pickup bed: ")
    make = input("\nPlease enter the make of your pickup: ")
    model = input("\nPlease enter the model of your pickup: ")
    #Gather user input, create a new pickup based on that input. 
    new_pickup = Pickup(make, model, bed_length)
    #Print the new pickup with the get from the Pickup class.
    new_pickup.get_make_model()
  elif choice == 3:
    #This choice represents if the user wants to quit.
    print("\nThank you for using Howard's Virtual Garage, goodbye.")
    break    
    #End program.

#Random notes:
#make = input("Please enter the make of your vehicle: ")
#model = input("Please enter the model of your vehicle: ")
#new_car = Car()
