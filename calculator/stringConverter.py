def calculate(string):
    if string == '':
        return '-'
    y = string.split(' ')
    nums = []
    ops = []
    total = 0
    for i in range(0, len(y)):
        try:
            nums.append(float(y[i]))
        except:
            ops.append(y[i])
    a = len(ops)
    b = 0
    while b < a:
        if ops[b] == 'x':
            total = nums[b] * nums[b+1]
            nums[b] = total
            nums.pop(b+1)
            ops.pop(b)
            a -= 1
            b -= 1
        elif ops[b] == '÷':
            total = nums[b] / nums[b+1]
            nums[b] = total
            nums.pop(b+1)
            ops.pop(b)
            a -= 1
            b -= 1
        b += 1
    a = len(ops)
    b = 0
    while b < a:
        if ops[b] == '+':
            total = nums[b] + nums[b+1]
            nums[b] = total
            nums.pop(b+1)
            ops.pop(b)
            a -= 1
            b -= 1
        elif ops[b] == '-':
            total = nums[b] - nums[b+1]
            nums[b] = total
            nums.pop(b+1)
            ops.pop(b)
            a -= 1
            b -= 1
        b += 1
    total = round(nums[0], 6)
    if total % 1 == 0:
        total = int(total)
    return total

print(calculate(''))
