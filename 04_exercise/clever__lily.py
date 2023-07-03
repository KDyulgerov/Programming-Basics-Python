# Read User Input

age = int(input())
price_washing_mqchine = float(input())
price_toy = int(input())

cash = 10
saved_money = 0
count_toys = 0
# Logic
for i in range(1, age + 1):
    if i % 2 == 0:
        saved_money += (cash - 1)
        cash += 10
    else:
        count_toys +=1

price_toys = count_toys * price_toy
total_price = price_toys + saved_money
diff = abs(total_price - price_washing_mqchine)

# Output
if total_price >= price_washing_mqchine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")