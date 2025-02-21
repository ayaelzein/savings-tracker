
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

  spent = savings + electricity + rent
  percentageofspent = (spent/100) * salary
  remainingsalary = salary - percentageofspent

  print(f"Your spent total is {percentageofspent}")
  print(f"Your remaining salary for other expenses is {remainingsalary}")

  calcsavings = (savings/100) * salary
  calcelectricity = (electricity/100) * salary
  calcrent = (rent/100) * salary

  yearlyrent = calcrent * 12
  yearlyelect = calcelectricity * 12 

  print(f"The estimated cost of your yearly rent is {yearlyrent}")
  print(f"The estimated cost of your yearly electricity is {yearlyelect}")

     

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
