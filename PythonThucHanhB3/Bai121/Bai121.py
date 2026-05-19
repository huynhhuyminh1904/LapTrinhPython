def gen_strobo(n, max_n, ext=False):
    if n == 0: return [""]
    if n == 1: 
        return ["0", "1", "8"] if not ext else ["0", "1", "2", "5", "8"]
    
    sub = gen_strobo(n - 2, max_n, ext)
    res = []
    for s in sub:
        if n != max_n:
            res.append("0" + s + "0")
        res.append("1" + s + "1")
        res.append("8" + s + "8")
        res.append("6" + s + "9")
        res.append("9" + s + "6")
        if ext:
            res.append("2" + s + "2")
            res.append("5" + s + "5")
    return res

n = int(input("Nhập n (2<=n<=10): "))

# câu a
ans_a = sorted([int(x) for x in gen_strobo(n, n, ext=False)])
print("a:", ans_a)

# câu b
ans_b = sorted([int(x) for x in gen_strobo(n, n, ext=True)])
print("b:", ans_b)