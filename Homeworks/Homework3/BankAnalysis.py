

import os

def analyze_transactions(filename="transactions.txt"):
    """Read and analyze transactions from file using simple variables."""
    file_path = os.path.join(os.path.dirname(__file__), filename)
    
    # Initialize counters and totals
    total_transactions = 0
    deposit_count = 0
    withdrawal_count = 0
    total_deposits = 0.0
    total_withdrawals = 0.0
    current_balance = 0.0
    largest_deposit = 0.0
    largest_withdrawal = 0.0
    
    try:
        with open(file_path, 'r') as file:
            print("Bank Statement Analysis")
            print("=" * 40)
            print("\nProcessing transactions...")
            
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        parts = line.split(',')
                        if len(parts) == 2:
                            transaction_type, amount_str = parts
                            amount = float(amount_str)
                            
                            # Update counters
                            total_transactions += 1
                            
                            if transaction_type == 'deposit':
                                deposit_count += 1
                                total_deposits += amount
                                current_balance += amount
                                if amount > largest_deposit:
                                    largest_deposit = amount
                            elif transaction_type == 'withdrawal':
                                withdrawal_count += 1
                                total_withdrawals += amount
                                current_balance -= amount
                                if amount > largest_withdrawal:
                                    largest_withdrawal = amount
                        else:
                            print(f"Warning: Invalid format on line {line_num}: {line}")
                    except ValueError:
                        print(f"Warning: Could not parse amount on line {line_num}: {line}")
                        continue
        
        # Display results
        if total_transactions > 0:
            print(f"\nTransaction Summary:")
            print(f"Total Transactions: {total_transactions}")
            print(f"Deposits: {deposit_count}")
            print(f"Withdrawals: {withdrawal_count}")
            
            print(f"\nFinancial Summary:")
            print(f"Total Deposits: ${total_deposits:.2f}")
            print(f"Total Withdrawals: ${total_withdrawals:.2f}")
            print(f"Current Balance: ${current_balance:.2f}")
            
            if current_balance >= 0:
                print("Status: Positive Balance")
            else:
                print("Status: Negative Balance (Overdrawn)")
            
            print(f"\nLargest Transactions:")
            print(f"Largest Deposit: ${largest_deposit:.2f}")
            print(f"Largest Withdrawal: ${largest_withdrawal:.2f}")
            
            # Calculate averages without using statistics module
            if deposit_count > 0:
                avg_deposit = total_deposits / deposit_count
                print(f"Average Deposit: ${avg_deposit:.2f}")
            
            if withdrawal_count > 0:
                avg_withdrawal = total_withdrawals / withdrawal_count
                print(f"Average Withdrawal: ${avg_withdrawal:.2f}")
            
        else:
            print("No transactions found to analyze.")
    
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        print("Please run BankInput.py first to create transactions.")

def main():

    analyze_transactions()

if __name__ == "__main__":
    main()