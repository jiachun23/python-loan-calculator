from fastapi import FastAPI

app = FastAPI()

# test endpoint
@app.get("/test")
async def test():
    return "ok"

# endpoint to perform calculation
@app.post("/calculate")
async def calculate(data: dict):
    downpayment_percent = float(data.get("downpayment")) / float(data.get("total_amount")) * 100
    interest_rate = float(data.get("interest")) / 100
    loan_amount =  float(data.get("total_amount")) - float(data.get("downpayment"))
    years = int(data.get("years"))

    monthly_instalment = (loan_amount*interest_rate*years+loan_amount)/(years*12)

    json_output = {"downpayment": round(float(data.get("downpayment")),2), "downpayment_percentage": round(downpayment_percent,2), "interest_rate": "{} %".format(data.get("interest")), \
               "loan_amount": round(loan_amount,2), "loan_period": "{} years".format(years), "monthly_instalment": round(monthly_instalment, 2)}

    return json_output