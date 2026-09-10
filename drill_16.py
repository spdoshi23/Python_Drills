def calculate_total(price, tax_rate):
    total = price + (tax_rate*price)
    return total

final_bill = calculate_total(100, 0.18)
print(f"Your final bill is: {final_bill}")