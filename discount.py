# a Function to calculate discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price
# ask for inuts from the user
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))
# Calculate final price
final_price = calculate_discount(original_price, discount_percentage)
# Output the result
if discount_percentage >= 20:
    print(f"Final price after {discount_percentage}% discount: {final_price}")
else:
    print(f"No discount applied. Original price: {final_price}")
