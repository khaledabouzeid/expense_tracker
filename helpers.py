import requests

def transform_to_base(currency, amount):
    if amount <= 0:
        print("Invalid amount")
        return False
    # request the currency and base
    try:
        response=requests.get(f"https://api.frankfurter.dev/v2/rates?quotes={currency}&base=USD")
        data = response.json()
        amount_to_base=float(data[0]["rate"])

    except:
        return False
    

   

    # calc the amount
    number=float(amount / amount_to_base)
    # round it
    new_amount =round(number, 2)
    

    # return the amount in base
    return new_amount