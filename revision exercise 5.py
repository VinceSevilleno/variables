#Vince Sevilleno
#22/09/2014
#Revision Exercise 5

print("The program will ask for dimensions of both a Lift and a Fridge, it will then calculate the volume inside the lift when the fridge is inside.")
print()
print("Give three measurements of a lift's height/width/depth:")
print()
lift_height=int(input("Please enter a height:"))
print()
lift_width=int(input("Please enter a width:"))
print()
lift_depth=int(input("PLease enter a depth:"))
lift_volume=lift_height*lift_width*lift_depth
print("The volume within the lift is {0}.".format(lift_volume))
print()
print("Now give values for the dimensions of a fridge but make sure that the measurements are SMALLER than the measurements of the lift.")
print()
fridge_height=int(input("Please enter a height:"))
print()
fridge_width=int(input("Please enter a width:"))
print()
fridge_depth=int(input("Please enter a depth:"))
print()
fridge_volume=fridge_height*fridge_width*fridge_depth
print("The volume of the fridge is {0}.".format(fridge_volume))
volume_withfridge=lift_volume-fridge_volume
print("The overall volume inside the lift with the fridge inside is {0}.".format(volume_withfridge))

