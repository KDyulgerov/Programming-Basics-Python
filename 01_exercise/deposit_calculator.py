
deposit_sum = float(input())
deadline = int(input())
yearly_increase = float(input())


yearly_increase_total = deposit_sum * yearly_increase / 100

monthly_increase = yearly_increase_total / 12

total_price = deposit_sum + deadline * monthly_increase

print(total_price)