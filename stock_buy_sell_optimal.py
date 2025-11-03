prices = [7, 2, 1, 5, 6, 4,8]
min_price = float("inf")
#profit = 0 
max_profit = 0
for i in prices:
    min_price = min(min_price, i)
    max_profit = max(max_profit, i - min_price)

print(max_profit)


