
def calculate(s):
    s = s.strip().split(' ')
    operator = []
    nums = []
    i = 0
    while i < len(s):
        if s[i] == '+' or s[i] == '-':
            operator.append(s[i])
        elif s[i] == '*':
            res = nums.pop() * int(s[i + 1])
            nums.append(res)
            i += 1
        else:
            nums.append(int(s[i]))
        i += 1
    res = nums.pop(0)
    while operator != []:
        op = operator.pop(0)

        if op == '-':
            res -= nums.pop(0)
        else:
            res += nums.pop(0)
    return res


res = calculate("1 - 3 * 31 + 5")
print(res)
