
months = {
          "January" : "salary_per_jan",
          "February" : "salary_per_feb", 
          "March" : "salary_per_mar", 
          "April": "salary_per_apr",
          "May" : "salary_per_may", 
          "June" : "salary_per_jun", 
          "July" : "salary_per_jul", 
          "August" : "salary_per_aug", 
          "September" : "salary_per_sep",
          "October" : "salary_per_oct", 
          "November" : "salary_per_nov", 
          "December" : "salary_per_dec"
           }

selectedmonth = input("Please enter the selected month: ")
#  salary = int(input(f"Please enter your salary for {selectedmonth}: "))
  
if selectedmonth:
  salary = int(input(f"Please enter your salary for {selectedmonth}: "))
  months[selectedmonth] = salary
     
  savings = int(input(f"Please enter the percentage that you've allocated for savings in the {selectedmonth}: "))
  electricity = int(input(f"Please enter the percentage that you've allocated for electricity in the {selectedmonth}: "))
  rent = int(input(f"Please enter the percentage that you've allocated for rent in the {selectedmonth}: "))

  spentperc = savings + electricity + rent
  spent = (spentperc/100) * salary
  remainingsalary = salary - spent

  print(f"Your spent total is {spent}")
  print(f"Your remaining salary for other expenses is {remainingsalary}")

  calcsavings = (savings/100) * salary
  calcelectricity = (electricity/100) * salary
  calcrent = (rent/100) * salary

  yearlyrent = calcrent * 12
  yearlyelect = calcelectricity * 12 

  print(f"The estimated cost of your yearly rent is {yearlyrent}")
  print(f"The estimated cost of your yearly electricity is {yearlyelect}")

  salarytotwo = salary * salary

  print(f"Nabiha's salary to the power of two is {salarytotwo}")

  remainingper = 100 - spentperc
  additionalsavings = input("Are there any additional savings: (Yes or No)")
  outsidesavings = input("Are these additions from your original salary: (Yes or No) ")

  if additionalsavings == "Yes" and outsidesavings == "No" :

    externaladdedsavings = int(input("How much are you adding: "))
    totalsavings = externaladdedsavings + calcsavings

    print(f"Your total savings for the month is {totalsavings}")

  elif outsidesavings == "Yes" and remainingper < 100 and additionalsavings == "Yes":
    
    addsavesal = int(input("Please enter the additional amount: "))
    totalsavings =  addsavesal + calcsavings
    updatedremaining = remainingsalary - addsavesal
    updatedpersavings = (savings*addsavesal/calcsavings) + savings

    print(f"Your updated savings in percentage is {updatedpersavings}")
    print(f"Your updated reamining is {updatedremaining}")
  
  elif outsidesavings == "Yes" and remainingper == 100 and additionalsavings == "Yes":

    print("You are unable to allocate more to your savings from your original salary.")

  elif outsidesavings == "No" and remainingper < 100 and additionalsavings == "No":

    print("Okay, have a nice day.")

  elif additionalsavings == "No" and outsidesavings == "Yes":

    print("You must've entered the wrong answer for the last question")




     

#elif selectedmonth == "February":
 #   months["February"]= int(input(salary))
  #  print(months.get("February"))

 # elif selectedmonth == "March":
   # months["March"] =  int(input(salary))
    #print(months.get("March"))

 # elif selectedmonth == "April":
   # months["April"] =  int(input(salary))
   # print(months.get("April"))

#  elif selectedmonth == "May":
   # months["May"] =  int(input(salary))
   # print(months.get("May"))

 # elif selectedmonth == "June":
   # months["June"] =  int(input(salary))
   # print(months.get("June"))

 # elif selectedmonth == "July":
   # months["July"] =  int(input(salary))
   # print(months.get("July"))

 # elif selectedmonth == "August":
   # months["August"] =  int(input(salary))
   # print(months.get("August"))

 # elif selectedmonth == "September":
   # months["September"] =  int(input(salary))
   # print(months.get("September"))

 # elif selectedmonth == "November":
   # months["November"] =  int(input(salary))
   # print(months.get("November"))

 # elif selectedmonth == "October":
   # months["October"] =  int(input(salary))
   # print(months.get("October"))

 # elif selectedmonth == "December":
  #  months["December"] =  int(input(salary))
   # print(months.get("December"))

  #  print(months)

 #while selectedmonth == "January":
 #months["January"] = int(input(salary))
 #print(months.get("January"))

# salary_per_month = [months.values]
# print(salary_per_month)
 

# outmonth = input("Please enter the selected month: ") 

# while outmonth != "stop":
  # if outmonth == month:
 #   salary = int(input("Please enter your salary for the month: "))
 #   salary_per_month.append(int(salary))
