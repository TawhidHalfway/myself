"""
take name give first name and second name
"""
name = input("name: ")
def name_seperate(name):
    first_second_name = name.split()
    print(f"your first name is: {first_second_name[0]} and your second name is : {first_second_name[1]}")

name_seperate(name)