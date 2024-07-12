hours = input("Enter hours worked: ")
h = float(hours)

rate_per_hour = input("Enter rate per hour: ")
r = float(rate_per_hour)
if h <= 40:
    gross_pay = h * r
else:
    regular_pay = 40 * r
    overtime_pay = (h - 40) * (1.5 * r)
    gross_pay = regular_pay + overtime_pay

print("Gross pay :",gross_pay)