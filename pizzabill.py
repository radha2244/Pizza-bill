print("Pizza Types\n1.Normal\n2.Delux")
c = int(input("Enter your Choice [1 or 2]:"))
cost = 0
if c == 1:
    print("Pizza Types\n1.Veg\n2.Non Veg")
    cz = int(input("Enter your Choice [1.yes or 2.no]:"))
    if cz == 1:
        cost = cost + 300
        temp=cost
    else:
        cost = cost + 400
        temp=cost
else:
    print("Pizza Types\n1.Veg\n2.Non Veg")
    cz = int(input("Enter your Choice [1.yes or 2.no]:"))
    if cz == 1:
        cost = cost + 600
        temp=cost
    else:
        cost = cost + 800
        temp=cost
p = int(input("Extra Cheese? [1.Yes or 2.NO]:"))
if p == 1:
    cost = cost + 100
t = int(input("Extra Topping? [1.Yes or 2.NO]: "))
if t == 1:
    cost = cost + 100
w = int(input("Do you want Water Bottles? [1.Yes or 2.NO]:"))
if w == 1:
    how = int(input("How many bottels do you want:"))
    cost = cost + 20 * how
k = int(input("Do you want Ketchup? [1.Yes or 2.NO]:"))
if k == 1:
    how = int(input("How many Packets? :"))
    cost = cost + 5 * how
s = int(input("Do you want Soft Driknks? [1.Yes or 2.NO]:"))
if s == 1:
    how = int(input("How many drinks? :"))
    cost = cost + 75 * how
i = int(input("Is it a Take Away? [1.Yes or 2.NO]:"))
if i == 1:
    cost = cost + 20
print("___________________________")
print("***Pizza Bill Generator***")
print("___________________________")
print("Base Price                = ",float(temp))
if p==1:
    print("Extra Cheese            = 100.0")
if t==1:
    print("Extra Toppings         = 100.0")
if w==1:
    print("Water bottle         = 20.0")
if k==1:
    print("Ketchup Packets       = 25.0")
if s==1:
    print("Soft Drinks            =75.0")
if i==1:
    print("Take Away Charges  = 20.0")
print("___________________________")
gst = 0.18 * cost
total = gst + cost
print("Total Cost                 =",float(cost))
print("GST Charges @18             = ",gst)
print("___________________________")
print("Net Amount Payable   =",total)
