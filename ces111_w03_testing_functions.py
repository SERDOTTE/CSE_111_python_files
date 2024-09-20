def deposit(amount):
    # In order for this program to work correctly and
    # for the bank records to be correct, we must not
    # allow someone to deposit a zero or negative amount.
    assert amount > 0