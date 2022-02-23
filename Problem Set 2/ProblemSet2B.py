current_savings = 0
annual_return = .04


total_cost = int(input("What is the cost of your dream home: "))
portion_saved = float(input("What percentage of your salary do you want to save: "))
total_salary = int(input("What are you making every year: "))
semi_annual_raise = float(input("Expected 6 month raise rate: "))
portion_down_payment = total_cost/4

total_months = 0

while current_savings < portion_down_payment:
    current_savings = current_savings + current_savings*annual_return/12
    current_savings = current_savings + ((total_salary/12)*portion_saved)
    total_months = total_months + 1
    if total_months % 6 == 0 :
        total_salary = total_salary * (1+semi_annual_raise)
    print(current_savings)

print(total_months)

