def part_a(yearly_salary, portion_saved, cost_of_dream_home):
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
	    
	print(months)
	return months