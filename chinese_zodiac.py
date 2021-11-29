def zodiac(year):
    animals = ["monkey", "rooster", "dog", "pig", "rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep"]
    return (animals[year%12])

year = int(input("Please enter a year:\n "))
print("This is the year of the {}".format(zodiac(year)))