def push(data):
    global SIZE, stack, top
    if top < SIZE - 1:
        top += 1
        stack[top] = data
    else:
        print("Stack Overflow")

def pop():
    global SIZE, stack, top
    if top >= 0:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data
    else:
        print("Stack Underflow")
        return None

def postfix(infix):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    global SIZE, stack, top, outlist

    for i in infix:
        if i.isalnum():
            outlist.append(i)
        elif i == '(':
            push(i)
        elif i == ')':
            while stack[top] != '(':
                outlist.append(pop())
            pop()  # pop the '(' from the stack
        else:  # 연산자일 경우
            while top != -1 and stack[top] != '(' and precedence[stack[top]] >= precedence[i]:
                outlist.append(pop())
            push(i)
    
    while top != -1:
        outlist.append(pop())

# 전역 변수
SIZE = 100
stack = [None for _ in range(SIZE)]
outlist = []
top = -1

if __name__ == "__main__":
    mathExpression =input("Infix 수식을 입력하세요")
    postfix(mathExpression)
    print('Postfix:', ''.join(outlist))
