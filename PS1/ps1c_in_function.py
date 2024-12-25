def part_c(initial_deposit):
	#########################################################################
	cost_of_dream_home = 800000
	portion_down_payment = 0.25
	
	downpayment = cost_of_dream_home * portion_down_payment
	months = 36 # 3 years
	
	deposit = initial_deposit
	max_deposit = initial_deposit * (1+1/12)**months
	
	steps = 0
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	if initial_deposit >= downpayment or downpayment - initial_deposit <= 100:
	    r = 0
	    print("Best savings rate:", r)
	elif max_deposit < downpayment:
	    r = None
	    print("Best savings rate:", r)
	else:
	    r = 0.5 # initial guess point
	    r_lower = 0
	    r_upper= 1
	    
	    while abs(downpayment - deposit) > 100:
	        deposit = initial_deposit * (1+r/12)**months
	        steps = steps + 1
	        
	        if abs(downpayment - deposit) <=100:
	            print("Best savings rate:", r)
	        elif deposit > downpayment:
	            r_upper = r
	            r = (r_lower + r_upper) / 2
	        elif deposit < downpayment:
	            r_lower = r
	            r = (r_lower + r_upper) / 2
	    
	print("Steps in bisection search:", steps)
	return r, steps