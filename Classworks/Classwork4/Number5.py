def check_bracket(bracket_string, i =0, balance=0, ):

    if i == len(bracket_string):
        return balance == 0

    bracket = bracket_string[i]

    if bracket == '(':
        balance += 1
    else:
        balance -= 1

    if balance < 0:
        return False

    return True and check_bracket(bracket_string, i + 1, balance)



print(check_bracket("(()())()"))
