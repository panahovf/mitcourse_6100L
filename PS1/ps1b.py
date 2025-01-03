## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter yearly salary: "))
portion_saved = float(input("Savings rate (percentage 0 to 1): "))
cost_of_dream_home = float(input("Enter home price: "))
semi_annual_raise = float(input("Enter raise (percentage 0 to 1): "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
amount_saved = 0
r = 0.05

downpayment = cost_of_dream_home * portion_down_payment
months = 0


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amount_saved < downpayment:
    interest_income = amount_saved * (r/12)
    monthly_savings = (yearly_salary/12) * portion_saved
    amount_saved = amount_saved + interest_income + monthly_savings
    months = months + 1
    
    if months%6 == 0:
        yearly_salary = yearly_salary * (1 + semi_annual_raise)
    
print(months)
