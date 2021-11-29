def brackets(status, income):
    if (status == "1" and 0<=income<=8350) or (status == "2" and 0<=income<=16700)  or (status == "3" and 0<=income<=8350)  or (status == "4" and 0<=income<=11950):
        return (income - (income * .1))
    elif (status == "1" and 8351<=income<=33950) or (status == "2" and 16701<=income<=67900)  or (status == "3" and 8351<=income<=33950)  or (status == "4" and 11951<=income<=45500): #15%
        return (income - (income * .15))
    elif (status == "1" and 33951<=income<=82250) or (status == "2" and 67901<=income<=137050)  or (status == "3" and 33951<=income<=68525)  or (status == "4" and 45501<=income<=117450): #25%
        return (income - (income * .25))
    elif (status == "1" and 82251<=income<=171550) or (status == "2" and 137051<=income<=208850)  or (status == "3" and 68526<=income<=104425)  or (status == "4" and 117451<=income<=190200): #28%
        return (income - (income * .28))
    elif (status == "1" and 171551<=income<=372950) or (status == "2" and 208851<=income<=372950)  or (status == "3" and 104426<=income<=186475)  or (status == "4" and 190201<=income<=372950): #33
        return (income - (income * .33))
    elif (status == "1" and income>=372951) or (status == "2" and income>=372951)  or (status == "3" and income>=186476)  or (status == "4" and income>=372951): #35%
        return (income - (income * .35))
    else:
        print("Invalid income or filing status")


income = float(input("How much income do you recieve?\n "))
status = (input("What is your filing status?\n[1] Single\n"
                   "[2] Married Filing Jointly or Qualifying Widow(er)\n"
                   "[3] Married Filing Separately\n"
                   "[4] Head of Household\n"))

print("Your income after taxes is:\n {}".format(brackets(status, income)))