def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def solution(a, b):
    answer = 0

    deno = b // gcd(a, b)

    while deno % 2 == 0:
        deno = deno // 2

    while deno % 5 == 0:
        deno = deno // 5

    if deno == 1 or deno == 2 or deno == 5:
        return 1

    return 2