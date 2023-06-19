
chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
delivery_price = 2.50

count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegan_menu = int(input())

price_chicken_menu = count_chicken_menu * chicken_menu
price_fish_menu = count_fish_menu * fish_menu
price_vegan_menu = vegan_menu * count_vegan_menu

menu_price = price_chicken_menu + price_fish_menu + price_vegan_menu
dessert_price = (menu_price * 20/100)
total_price_menu = menu_price + dessert_price + delivery_price
print(total_price_menu)
