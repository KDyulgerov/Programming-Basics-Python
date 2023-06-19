
package_pen = 5.80
package_markers = 7.20
prep_liters = 1.20

count_package_pen = int(input())
count_package_markers = int(input())
count_prep_liters = int(input())
percentage_discount = int(input())

price_for_pen = count_package_pen * package_pen
price_for_markers = count_package_markers * package_markers
price_for_prep = count_prep_liters * prep_liters

total_price = price_for_pen + price_for_markers + price_for_prep

discount_price = total_price - (total_price * percentage_discount / 100)

print(discount_price)