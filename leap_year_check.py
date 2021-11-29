def leap_year(year):
    if ((year%4 == 0 and year%100) or year%400 == 0):
        return "This year is froggy!"
    else:
        return "This year is not very froggy at all..."

year = int(input("Hey there, stranger! Could you tell me what year it is?\n"))

print(leap_year(year))