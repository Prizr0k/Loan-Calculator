import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', choices=['diff', 'annuity'])
parser.add_argument('-pr', '--principal', type=int)
parser.add_argument('-pay', '--payment', type=float)
parser.add_argument('-per', '--periods', type=int)
parser.add_argument('-in', '--interest', type=float)

args = parser.parse_args()

values = [args.type, args.principal, args.payment, args.periods, args.interest]


def number_of_monthly(principal, payment,  interest):
	i = interest / (12 * 100)
	if interest == 0:
		n = principal / payment
	else:
		n = math.log((payment / (payment - i * principal)), (1 + i))
	return n
	
def annuity_payment(principal, periods, interest):
	i = interest / (12 * 100)
	if interest == 0:
		n = principal / periods
	else:
		n = principal * ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
	return n

def loan_principal(annuity, periods, interest):
	i = interest / (12 * 100)
	if interest == 0:
		n = annuity * periods
	else:
		n = annuity  / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
	return n	
	
def differentiated_payments(principal, interest, periods, m):
	i = interest / (12 * 100)
	d = (principal / periods) + i * (principal - ((principal * (m - 1)) / periods))
	return d
flag = ''
if args.type == 'diff' and args.principal != None and args.periods != None and args.interest != None:
	flag = "diff"
elif args.type == 'annuity' and args.principal != None and args.periods != None and args.interest != None and args.payment == None:
	flag = "payment"
elif args.type == 'annuity' and args.principal == None and args.periods != None and args.interest != None and args.payment != None:
	flag = "principal"
elif args.type == 'annuity' and args.principal != None and args.periods == None and args.interest != None and args.payment != None:
	flag = "periods"
else:
	flag = 'Incorrect parameters'



if flag == 'diff':
	credit = args.principal
	summa = 0
	for i in range(1, args.periods + 1):
		res = math.ceil(differentiated_payments(args.principal, args.interest, args.periods, i))
		summa += res
		print(f'Month {i}: payment is {res}')
	print()
	print(f'Overpayment = {summa - credit}')
else:
	if flag == 'principal':
		res = math.ceil(loan_principal(args.payment, args.periods, args.interest))
		overpayment = args.payment * args.periods - res
		print(f'Your loan principal = {res}')
		print(f'Overpayment = {overpayment}')
	elif flag == 'payment':
		res = math.ceil(annuity_payment(args.principal, args.periods, args.interest))
		overpayment = res * args.periods - args.principal
		print(f'Your annuity payment = {res}!')
		print(f'Overpayment = {overpayment}')
	elif flag == 'periods':
		res = math.ceil(number_of_monthly(args.principal, args.payment, args.interest))
		year = res // 12
		mon = res % 12
		overpayment = args.payment * res - args.principal
		if mon == 0 and year > 1:
			print(f'It will take {year} years to repay this loan!')
		elif mon == 0 and year == 1:
			print(f'It will take {year} year to repay this loan!')
		elif mon > 1 and year > 1:
			print(f'It will take {year} years and {mon} months to repay this loan!')
		elif mon > 1 and year == 0:
			print(f'It will take {mon} months to repay this loan!')
		elif mon == 1 and year > 1:
			print(f'It will take {year} years and {mon} month to repay this loan!')
		elif mon > 1 and year == 1:
			print(f'It will take {year} year and {mon} months to repay this loan!')
		elif mon == 1 and year == 1:
			print(f'It will take {year} year and {mon} month to repay this loan!')
		print(f'Overpayment = {overpayment}')
	else:
		print(flag)

		

