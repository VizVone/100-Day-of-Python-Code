print("Welcome to Tip Calculator")

totalbill=float(input("What was the total bill? "))

totalpercentage=int(input("What percentage tip would you like to give ? "))

percentcalc=totalpercentage/100

finalpercent=totalbill*percentcalc

totalbill+=finalpercent

nosplit=int(input("How many people to split the bill ? "))

result=totalbill/nosplit
result=round(result,2)
print(f"Each Person should pay ${result}")