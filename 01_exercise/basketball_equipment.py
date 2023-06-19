
yearly_tax = int(input())

basketball_shoes = yearly_tax - (yearly_tax * 40 / 100)
basketball_clothes = basketball_shoes - (basketball_shoes * 20 / 100)
basketball_ball = basketball_clothes / 4
basketball_accessories = basketball_ball / 5

total_price = yearly_tax + basketball_shoes + basketball_clothes + basketball_ball + basketball_accessories

print(total_price)
