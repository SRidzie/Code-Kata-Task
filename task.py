def supermarket_checkout(a):	
	d = {'A':0,'B':0,'C':0,'D':0}
	for x in a:
		if x not in d:
			d[x] = 1
		else:
			d[x] += 1

	a_bill = 0
	b_bill = 0
	c_bill = 0
	d_bill = 0
	t = d.copy()
	for x in d:
		if x == "A":
			while d[x] !=0:	
				if d[x] >= 3:
					a_bill += 130
					d[x]-=3
				else:
					a_bill += 50
					d[x] -= 1	
		elif x == "B":
			while d[x] !=0:	
				if d[x] >= 2:
					b_bill += 45
					d[x]-=2
				else:
					b_bill += 30
					d[x] -= 1	
		elif x == "C":
			c_bill += d[x]*20
		elif x == "D":
			d_bill += d[x]*15	
	fa = a_bill+b_bill+c_bill+d_bill
	return fa

if __name__=="__main__":
	items = input("Enter Items : ").upper()
	final_price = supermarket_checkout(items)
	print(final_price)