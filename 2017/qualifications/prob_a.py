lineNo = 0

for _ in range(int(input())):
    s, k = input().split()
    k = int(k)

    lineNo += 1
    n = 0
    length = len(s)
    for i in range(length - k + 1):
        if s[i] == '-':
            s = s[:i] + "".join("-+"[j == '-'] for j in s[i : i+k]) + s[i+k:]
            n += 1
    print("Case #{}: {}".format(lineNo, n if s[length - k:] == "+" * k else "IMPOSSIBLE"))