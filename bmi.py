def bmi(weight, height):
    return weight/(height*height)


weight = float(input("Please enter your weight in kilograms:\n"))
height = float(input("Please enter your height in meters:\n"))

print("Your Body Mass Index is {}".format(bmi(weight, height)))