def prime_def():
    prime_set = set(range(1, 1001))
    for i in range(2, 101):
        if i in prime_set:
            prime_set -= set(range(2 * i, 1001, i))
    return prime_set


def is_prime_num(num):
    global PRIME_SET
    if not PRIME_SET:
        PRIME_SET = prime_def()
    return num in PRIME_SET


def dividers_num(num):
    result = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            result.append(i)
    return result+[num]


def prepare_prime_set(num):
    global PRIME_SET
    if not PRIME_SET:
        PRIME_SET = prime_def()
    prime_list = sorted(list(PRIME_SET))
    prime_list = [i for i in prime_list if i <= num]
    return prime_list


def biggest_simple_divider(num):
    prime_list = prepare_prime_set(num)
    for i in reversed(prime_list):
        if num % i == 0:
            return i


def list_simple_divider(num):
    prime_list = prepare_prime_set(num)
    result = []
    for i in reversed(prime_list):
        while num % i == 0:
            num //= i
            result.append(i)
        if num == 1:
            break
    return result


def max_divider(num):
    result = dividers_num(num)
    return result[-2]


PRIME_SET = set()
# print(biggest_simple_divider(1335))
# listt = list_simple_divider(609840)
# print(*[f'{i}^{listt.count(i)}' if listt.count(i) > 1 else i for i in set(listt)], sep=', ')
# print(max_divider(144))
# 2	3	5	7	11	13	17	19	23	29	31	37
# 41	43	47	53	59	61	67	71	73	79	83	89
# 97