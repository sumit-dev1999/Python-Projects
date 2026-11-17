# Project 03: Shop Billing System

# Indian Rupees Symbol
rupees = "\u20b9"

# Product Information
product_name = input("Enter Product Name: ")

# Product Price
price = float(input(f"Enter Product Price: {rupees} "))

# Product Quantity
quantity = int(input("Enter Quantity: "))

# GST Rate
gst_rate = float(input("Enter GST Rate (%): "))

# Total Amount Calculation
total_amount = price * quantity

# GST Calculate
gst_amount = total_amount * gst_rate

# Final Amount
final_amount = total_amount + gst_amount

# Display Invoice Report
print("\n========== SHOP INVOICE ==========")

print(f"Product Name: {product_name}")
print(f"Price: {rupees} {price:,.2f}")
print(f"Quantity: {quantity:,.0f}")

print("-" * 35)

print(f"Total Amount: {rupees} {total_amount:,.0f}")
print(f"GST Rate: {gst_rate}%")
print(f"GST Amount: {rupees} {gst_amount:,.2f}")

print("-" * 35)

print(f"Final Amount: {rupees} {final_amount:,.2f}")

print("-" * 35)