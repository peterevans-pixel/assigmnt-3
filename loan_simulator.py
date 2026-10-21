def get_number(prompt, allow_zero=False):
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")
            continue

        if value < 0 or (value == 0 and not allow_zero):
            if allow_zero:
                print("Please enter a number that is at least 0.")
            else:
                print("Please enter a number greater than 0.")
            continue

        return value


def simulate_repayment(loan_amount, annual_interest_rate, monthly_payment):
    monthly_rate = annual_interest_rate / 100 / 12

    if monthly_payment <= loan_amount * monthly_rate:
        print("That monthly payment is not enough to pay off the loan.")
        print("Increase the payment and run the simulator again.")
        return

    balance = loan_amount
    months = 0

    while balance > 0:
        interest = balance * monthly_rate
        balance += interest
        balance -= monthly_payment
        months += 1

        if balance < 0:
            balance = 0

    print(f"It will take {months} months to pay off the loan.")


loan_amount = get_number("Loan amount: $")
annual_interest_rate = get_number("Annual interest rate (%): ", allow_zero=True)
monthly_payment = get_number("Monthly payment: $")

simulate_repayment(loan_amount, annual_interest_rate, monthly_payment)
