semi_annual_raise = .07
annual_return = .04
cost_of_home = 1000000
portion_down_payment = cost_of_home/4
current_savings = 0

print("Attempting to find the best rate of savings for $1m, assumed 4% monthly investment return, and a twice a year 7% raise")
total_salary = int(input("Enter your salary: "))

for i in range(1, 10000):
    current_savings = 0
    total_months = 0
    total_salary_per_iter = total_salary
    while current_savings < portion_down_payment:
        current_savings = current_savings + current_savings*annual_return/12
        current_savings = current_savings + ((total_salary_per_iter/12)*(i/10000))
        total_months = total_months + 1
        if total_months % 6 == 0 :
            total_salary_per_iter = total_salary_per_iter * (1+semi_annual_raise)
        print(current_savings)
    if total_months < 36:
        print(i/10000)
        break
print(total_months)
