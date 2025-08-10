# Calculate Discount Program

## Description
This Python program calculates the final price of an item after applying a discount.
If the discount percentage is **20% or higher**, the discount is applied; otherwise, the original price is returned.

##  Features
- Accepts original price and discount percentage from the user
- Applies discount only if it is **20% or more**
- Outputs the final price or the original price if discount is too small

## 🛠️ How It Works
1. The program defines a function **`calculate_discount(price, discount_percent)`**
2. If `discount_percent >= 20`, the function calculates the discount and subtracts it from the price.
3. Otherwise, it returns the original price without changes.

## 📋Example Usage
```
Enter the original price: 1000
Enter the discount percentage: 25
Final price after 25.0% discount: 750.0
```

```
Enter the original price: 500
Enter the discount percentage: 15
No discount applied. Original price: 500.0
```


