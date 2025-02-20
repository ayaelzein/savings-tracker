
months = {"January" : "salary_per_jan", 
          "February" : "salary_per_feb", 
          "March" : "salary_per_mar", 
          "April": "salary_per_apr",
          "May" : "salary_per_may", 
          "June" : "salary_per_jun", 
          "July" : "salary_per_jul", 
          "August" : "salary_per_aug", 
          "Septermber" : "salary_per_sep",
          "October" : "salary_per_oct", 
          "November" : "salary_per_nov", 
          "December" : "salary_per_dec" }

for month in months :
  print(month)


selectedmonth = input("Please enter the selected month: ")
salary_per_month = [months.values]
print(salary_per_month)

salary = int(input(f"Please enter your salary for {selectedmonth}: "))

# outmonth = input("Please enter the selected month: ") 

# while outmonth != "stop":
  # if outmonth == month:
 #   salary = int(input("Please enter your salary for the month: "))
 #   salary_per_month.append(int(salary))
