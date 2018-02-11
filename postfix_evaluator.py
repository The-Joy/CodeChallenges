'''Write a simple function to evaluate a
postix expression and return the result'''


def evaluate(input_text):
    '''Given a postfix input string, return the value'''
    ops = []
    for i in input_text:
        if str(i).isdigit():
            ops.append(i)
        else:
            val1 = ops.pop()
            val2 = ops.pop()
            ops.append(str(eval(val2 + i + val1)))
    return ops.pop()


def main():
    '''Entry point to fn'''
    val = '5 3 + 8 2 - *'
    print(evaluate(val.strip().split(' ')))  # returns 48


main()
