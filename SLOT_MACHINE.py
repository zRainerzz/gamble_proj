import random

MAX_LINES = 3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbols_count = {
    "🍀": 2,
    "⭐": 4,
    "🌑": 6,
    "👾": 8
}

symbols_value = {
    "🍀": 5,
    "⭐": 4,
    "🌑": 3,
    "👾": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines=[]
    for line in range(min(lines, ROWS)):  # Use min(lines, ROWS)
        symbol = columns[0][line]
        # ... rest of the logic

        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else: 
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    #symbols.items will give the value and the key.
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol) #add the symbol to the list
    columns=[]
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)   
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = (input("Enter amount to deposit: $"))
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a valid amount")
        else:
            print("Please enter a valid amount")
    return amount

def get_number_of_lines():
    while True:
        lines = (input("Enter the number of lines to bet on (1 - "+ str(MAX_LINES) + ")? "))
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= MAX_LINES and lines <= ROWS:  # Check against ROWS
                break
            else:
                print("Please enter a valid Number of lines.")                
        else:
            print("Please enter a valid amount")

    return lines


def get_bet():
    while True:
        amount = (input("What Would you like to bet? $ "))
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")  
        else:
            print("Please enter a valid amount")
            
    return amount

def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet() 
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    total_bet = bet * lines
    print(f'You are betting ${bet} on {lines} lines. Total balance is: ${total_bet}')
    
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_count)
    print(f"You won ${winnings} !")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f'Current balance is ${balance}')
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += game(balance)       
    print(f"You left with ${balance}")

if __name__ == "__main__": 
    main()