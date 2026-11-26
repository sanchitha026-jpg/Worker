
name = input("Enter employee name: ")
wage = float(input("Enter daily wage: "))
days = int(input("Enter working days: "))

total = wage * days
total = total + 200

print("Employee Name:", name)
print("Total Wages Payable: Rs.", total)