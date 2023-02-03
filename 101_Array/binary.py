def is_sum_of_3_powers_of_2(n):
    if n < 3:
        return False

    powers = []
    for i in range(n):
        if 2**i <= n:
            powers.append(2**i)
        else:
            break

    for i in range(len(powers)):
        for j in range(i, len(powers)):
            for k in range(j, len(powers)):
                if powers[i] + powers[j] + powers[k] == n:
                    return True

    return False


def binaryToDecimal(n):
    return int(n, 2)
for i in range(int(input())):
    n = int(input())
    s = input()
    s=binaryToDecimal(s)
    if is_sum_of_3_powers_of_2(s) == "True":
        print("YES")
    else :
        print("NO")

