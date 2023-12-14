# Python - Loan / Monthly Instalment Calculator 
This is a simple loan calculator program built in Python to show the monthly installment required.
Inputs are passed through `argument parser`:
- Total amount `(--total_amount)`
- Loan Period in years `(--years)`
- Downpayment Amount `(--downpayment)`
- Interest Rate `(--interest)`

Command: 
```
python calculator.py --interest 2.54 --total_amount 122000 --years 5 --downpayment 42000
```

Expected Output (A JSON Object): 
```
{'downpayment': 42000.0, 'downpayment_percentage': 34.426, 'interest_rate': '2.54', 'loan_amount': 80000.0, 'loan_period': '5 years', 'monthly_instalment': 1502.67}
```

Command for FastAPI:
```
uvicorn main:app --reload
```

NOTE: The FastAPI respond object is shown in `screenshots/fastapi_postman.png`