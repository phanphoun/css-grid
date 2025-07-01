materials =[
  {"name": "computer", "quantity": 20, "retial_price": 400, "quality": "Good"},
  {"name": "computer", "quantity": 10, "retial_price": 200, "quality": "Not good"},
  {"name": "Monitor", "quantity": 20, "retial_price": 1000, "quality": "Not good"},
  {"name": "Keyboard", "quantity": 10, "retial_price":150, "quality": "Good"},
  {"name": "Speaker", "quantity": 5, "retial_price": 50, "quality": "Good"}
 ]
total_price = 0
for key in materials:
    if key["quality"] == "Good":
        total_price += key["quantity"] * key["retial_price"]
print(total_price)



 