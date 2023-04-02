import requests
res = requests.post('http://localhost:5000/predict', json={
    "Age": 22,
        "Sex": "female",
        "Job": 2 ,
        "Housing" : "own",
        "Saving_accounts" : "little" ,
        "Checking_account" : "moderate" ,
            "Credit_amount" : 5951 ,
            "Duration" : 48 , 
            "Purpose" : "radio/TV"
     
})
if res.ok:
    print(res.json())