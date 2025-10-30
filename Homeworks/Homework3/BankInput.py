"""
Bank Manager - Transaction Input Program
This program allows users to input bank transactions (deposits or withdrawals)
and saves them to a text file for later analysis.
"""



def get_transaction_type():
    while True:
        transaction_type = input("Enter transaction type (deposit/withdrawal): ").lower().strip()
        if transaction_type in ['deposit', 'withdrawal']:
            return transaction_type
        else:
            print("Invalid transaction type. Please enter 'deposit' or 'withdrawal'.")

def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: $"))
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

def save_transaction(transaction_type, amount, filename="transactions.txt"):
    
    # Use hardcoded filepath
    file_path = "transactions.txt"
    
    # Append transaction to file
    with open(file_path, 'a') as file:
        file.write(f"{transaction_type},{amount:.2f}\n")
    
    print(f"Transaction recorded: {transaction_type} of ${amount:.2f}")

def main():
    print("=== Bank Transaction Manager ===")
    print("Enter your bank transactions. Type 'quit' to exit.")
    
    while True:
        print("\n" + "-" * 40)
        
        # Check if user wants to quit
        user_input = input("Continue with new transaction? (yes/quit): ").lower().strip()
        if user_input in ['quit', 'q', 'exit', 'no']:
            print("Goodbye!")
            break
        
        # Get transaction details
        transaction_type = get_transaction_type()
        amount = get_amount()
        
        # Save transaction
        save_transaction(transaction_type, amount)
        
        print(f"Transaction saved successfully!")

if __name__ == "__main__":
    main()
