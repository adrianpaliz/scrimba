sales_week_1 = [7, 3, 42, 19, 15, 35, 9]
sales_week_2 = [12, 4, 26, 10, 7, 28]
sales = []
unit_price = 1.5

last_day_week_2 = input("Number of lemonade sell at last day of week 2?: ")
sales_week_2.append(int(last_day_week_2))

sales = sales_week_1 + sales_week_2
print(sales)

best_day = max(sales) * 1.5
print(f"Your best day you earn {best_day} dollars")

worst_day = min(sales) * 1.5
print(f"Your worst day you earn {worst_day} dollars")

total = best_day + worst_day
print(f"In total you earn: {total} ")
