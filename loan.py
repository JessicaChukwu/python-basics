debt= float(input("How much do you owe?"))
rate= float(input("what is the interest percentage rate?:"))
paidoff= float(input("how much have you paid so far?:"))
months = int(input("how many months do you want to see interest for?:"))



monthly_rate= rate/100/12



for i in range(months):
    interest= debt+monthly_rate

    debt = debt+ interest

    if (debt - paidoff < 0):
        print("The last payment is", debt)
        print("You paid off the loan in", i+1, "months")

        break
debt = debt+ paidoff

print("Paid", paidoff, "off which", interest, "was interest")
print("Now i owe", debt)

    

