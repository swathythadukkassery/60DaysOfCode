def isOp(i):
    return i.isalpha()
def precedence(i):
    preced={'+':1, '-':1, '*':2, '/':2, '^':3}
    return preced[i]

def infTopos(exp):
    res = []
    stack = []
    for i in exp:
        if isOp(i) :
            res.append(i)
        elif i =='(':
            stack.append(i)
        elif i==')':
            while stack[-1]!='(':
                res.append(stack.pop())
            stack.pop()
        else:
            while stack!=[] and stack[-1]!='(' and precedence(i)<=precedence(stack[-1]):
                res.append(stack.pop())

            if stack == [] or stack[-1]=='(' or precedence(i)>precedence(stack[-1]):
                stack.append(i)
    while stack:
        res.append(stack.pop())
    print(''.join(res))
exp = input()
infTopos(exp)
