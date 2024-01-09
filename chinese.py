# Function to mimic print()
def 打印(*args, **kwargs):
    print(*args, **kwargs)

# Function to mimic len()
def 长度(x):
    return len(x)

# Function to mimic input()
def 输入(prompt=""):
    return input(prompt)

# Function to mimic range()
def 范围(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    result = []
    current = start
    while (step > 0 and current < stop) or (step < 0 and current > stop):
        result.append(current)
        current += step
    return result

# Function to mimic sum()
def 总和(iterable, start=0):
    total = start
    for element in iterable:
        total += element
    return total

# Function to mimic any()
def 任一(iterable):
    for element in iterable:
        if element:
            return True
    return False

# Function to mimic all()
def 全部(iterable):
    for element in iterable:
        if not element:
            return False
    return True

# Function to mimic sorted()
def 排序(iterable, key=None, reverse=False):
    return sorted(iterable, key=key, reverse=reverse)

# Function to mimic reversed()
def 反转(iterable):
    return reversed(iterable)

# Function to mimic zip()
def 拉链(*iterables):
    return zip(*iterables)

# Function to mimic enumerate()
def 枚举(sequence, start=0):
    return enumerate(sequence, start=start)

# Function to mimic abs()
def 绝对值(x):
    return abs(x)

# Function to mimic round()
def 四舍五入(number, ndigits=None):
    return round(number, ndigits)

# Function to mimic min()
def 最小值(*args):
    if len(args) == 1 and hasattr(args[0], '__iter__'):
        args = args[0]
    return min(args)

# Function to mimic max()
def 最大值(*args):
    if len(args) == 1 and hasattr(args[0], '__iter__'):
        args = args[0]
    return max(args)

# Function to mimic format()
def 格式化(string, *args, **kwargs):
    if args:
        return string.format(*args, **kwargs)
    elif kwargs:
        return string.format(**kwargs)
    else:
        return string

