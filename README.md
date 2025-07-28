# Pizza Billing System

A simple **Python console application** that simulates a pizza ordering and billing process. Users can choose pizza types, add toppings and extras, and receive a final bill including GST.

---

##  How to Run

1. Make sure Python is installed.
2. Save the script as `pizza_bill.py`.
3. Run the program:

```bash
python pizza_bill.py
```
# Features
Choose between:

Normal Pizza: Veg (₹300) or Non-Veg (₹400)

Deluxe Pizza: Veg (₹600) or Non-Veg (₹800)

Optional Add-ons:

Extra Cheese (₹100)

Extra Toppings (₹100)

Water Bottles (₹20 each)

Ketchup Packets (₹5 each)

Soft Drinks (₹75 each)

Take Away Charges (₹20)

GST @ 18% is automatically calculated.

Itemized bill is printed.
# Sample Input Flow
Pizza Types 

1.Normal

2.Delux

Enter your Choice [1 or 2]: 1

Pizza Types

1.Veg

2.Non Veg

Enter your Choice [1.yes or 2.no]: 2

Extra Cheese? [1.Yes or 2.NO]: 1

Extra Topping? [1.Yes or 2.NO]: 2

Do you want Water Bottles? [1.Yes or 2.NO]: 1

How many bottels do you want: 5

Do you want Ketchup? [1.Yes or 2.NO]: 1

How many Packets? : 2

Do you want Soft Driknks? [1.Yes or 2.NO]: 1

How many drinks? : 4

Is it a Take Away? [1.Yes or 2.NO]: 2

# Sample Output
___________________________
***Pizza Bill Generator***
___________________________
Base Price                =  400.0

Extra Cheese              = 100.0

Water bottle              = 20.0

Ketchup Packets           = 25.0

Soft Drinks               = 75.0
___________________________

Total Cost                = 910.0

GST Charges @18           = 163.79999999999998
___________________________
Net Amount Payable        = 1073.8

# Notes
Input validation is minimal—ensure to enter numeric values as prompted.

You can customize base prices or tax rate as per your requirements.

Ideal for learning basic Python, conditionals, input/output formatting.
