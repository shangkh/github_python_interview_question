s = ["ab", "abc", "a", "asda"]
b = sorted(s, key=lambda x: len(x))
print(s)
print(b)

s.sort(key=len)
print(s)
