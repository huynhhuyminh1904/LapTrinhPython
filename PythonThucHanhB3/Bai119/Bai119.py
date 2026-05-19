def sieve(limit):
    is_p = [True] * limit
    if limit > 0: is_p[0] = False
    if limit > 1: is_p[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            for j in range(i*i, limit, i):
                is_p[j] = False
    return is_p

def rot(s, ext=False):
    m = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    if ext:
        m.update({'2': '2', '5': '5'})
    res = []
    for c in reversed(s):
        if c not in m: return None
        res.append(m[c])
    return "".join(res)

is_prime = sieve(1000000)

# câu a
ans_a = []
for i in range(1000000):
    s = str(i)
    if rot(s, ext=False) == s:
        ans_a.append(i)
print("a:", ans_a)

# câu b
ans_b = []
for i in range(1000000):
    s = str(i)
    if rot(s, ext=False) == s and is_prime[i]:
        ans_b.append(i)
print("b:", ans_b)

# câu c
ans_c = []
for i in range(1000000):
    s = str(i)
    if rot(s, ext=True) == s:
        ans_c.append(i)
print("c:", ans_c)

# câu d
ans_d = []
for i in range(1000000):
    s = str(i)
    if rot(s, ext=True) == s and is_prime[i]:
        ans_d.append(i)
print("d:", ans_d)

# câu e
ans_e = []
for i in range(1000000):
    s = str(i)
    r = rot(s, ext=False)
    if r is not None and r != s and not is_prime[i]:
        r_val = int(r)
        if r_val < 1000000 and is_prime[r_val]:
            ans_e.append(i)
print("e:", ans_e)