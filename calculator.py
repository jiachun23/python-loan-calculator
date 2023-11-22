import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--interest', help='the interest rate')
parser.add_argument('--total_amount', help='the amount (price of the object)')
parser.add_argument('--downpayment', help='downpayment amount')
parser.add_argument('--years', help='loan peroid in years')

args = parser.parse_args()

downpayment_percent = float(args.downpayment) / float(args.total_amount) * 100
interest_rate = float(args.interest) / 100
loan_amount =  float(args.total_amount) - float(args.downpayment)
years = int(args.years)

monthly_instalment = (loan_amount*interest_rate*years+loan_amount)/(years*12)

json_output = {"downpayment": round(float(args.downpayment),2), "downpayment_percentage": round(downpayment_percent,2), "interest_rate": args.interest, \
               "loan_amount": round(loan_amount,2), "loan_period": "{} years".format(args.years), "monthly_instalment": round(monthly_instalment,2)}

print(json_output)

