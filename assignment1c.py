# William Meares
# Assignment 1C

name_of_object = input("Enter the name of the object: ")
mass_kg = input("Enter the mass of the object in KG: ")
velocity = input("Enter the mass of the object in m/s: ")

name_of_object_clean = name_of_object.strip().title()
mass_kg_num = float(mass_kg)
velocity_num = float(velocity)

KE_joules = 1/2*mass_kg_num*(velocity_num**2)

KE_calories = KE_joules/4.184
KE_ergs = KE_joules*10**7

output_line_one = f"Kinetic Energy Report for: {name_of_object_clean}"
print(output_line_one)
print("--------------------------------------")

output_line_two = f"Joules:\t{KE_joules} J"
print(output_line_two)

output_line_three = f"Calories:\t{KE_calories} cal"
print(output_line_three)

output_line_four = f"Ergs:\t{KE_ergs} erg"
print(output_line_four)