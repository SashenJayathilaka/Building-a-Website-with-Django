customer = {
    "Name": 'John Smith',
    "Age": 30,
    "is_Verified": True
}

customer["Name"] = 'Thomas Cruise'
print(customer["Name"])
print(customer.get("Birthday", "August  06 2001"))
