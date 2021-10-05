def get_discount(user_type):    
    # discount calculation
    if user_type == 'r':
        discount = 5   
    else:
        discount = 2   
        
    return discount


def invoice_print(total_bill_amount, discount):
        
    # Discount amount calculation
    discount_amount = discount * total_bill_amount / 100 
    
    # Total Amount to Pay
    amount_to_pay = total_bill_amount - discount_amount
    
    print("\n")
    print("############## Invoice ###########################")
    print(f"Total Bill:\t\t {total_bill_amount:10.2f}")
    print(f"Discount %{discount}:\t\t {discount_amount*-1:10.2f}")
    print("")
    print(f"Amount to Pay:\t\t {amount_to_pay:10.2f}")
    print("############## END ###############################")
    print("")
    

def main():
    user_type = input("Are you a regular user [Press r for Yes, and n for No]? : ").lower()
    total_bill = float(input("Enter the Total Bill Amount (in $): ")) 

    discount_percentage = get_discount(user_type)
    invoice_print(total_bill, discount_percentage)
    
    

if __name__ == "__main__":
    main()