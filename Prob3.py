def is_operand(char):
    return char.isalnum()

def postfix_to_infix(expression):
    stack = []
    for char in expression:
        if is_operand(char):
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append("(" + operand1 + char + operand2 + ")")

    return stack.pop()

if __name__ == "__main__":
    postfix_expression = input("Postfix 수식을 입력하세요: ")
    infix_expression = postfix_to_infix(postfix_expression)
    print("Infix 수식:", infix_expression)
