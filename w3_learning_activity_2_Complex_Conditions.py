large_loan = int(input('How large is the loan? ' ))
credit_history = int(input('How good is your credit history? '))
high_income = int(input('How high is your  income? '))
down_payment = int(input('How large is your down payment? '))

should_loan = False

if large_loan >= 5: 
    if credit_history >= 7 and high_income >= 7:
        should_loan = True
    elif credit_history >= 7 or high_income >= 7:
        if down_payment >= 5:
            should_loan = True
        else:
            should_loan = False
else:
    if credit_history < 4:
        should_loan = False
    elif high_income >= 7 or down_payment >= 7:
        should_loan = True
    elif high_income >= 4 and down_payment >= 4:
        should_loan = True
    else:
        should_loan = False


if should_loan:
    print()
    print('****************************************')
    print('Loan Decision: Yes. This is a goog loan.')
    print('****************************************')
    print()
else:
    print()
    print('**************************************************')
    print('Loan Decision: No. You should not loan this loan.')
    print('**************************************************')
    print()