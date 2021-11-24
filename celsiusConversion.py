if __name__ == '__main__':
    fahrenheit = int(input("Enter the current temperature:"))
    celsius = (5 / 9)*(fahrenheit - 32)

    if (fahrenheit <= 32):
        print("Program has frozen.")
    elif (fahrenheit >= 78):
        print("CPU is overheating")
    else:
        print("Perfect operating conditions")
