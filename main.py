import pyfiglet as figlet

name = figlet.figlet_format("Himasnhu \n Singh \n Tomar \n Programming")
print(name)
i = 1
while i <= 3:
    customer = int(input("Enter product price :"))
    age = int(input("enter the age of customer :"))
    if customer > 1000:
        if age > 60:
            customer = customer - 200
        else:
            customer = customer - 100
    if customer < 1000:
        if age < 45:
            customer = customer - 50
    print(customer)
    i = i + 1

