s = input()
if s == s[::-1]:
    print(True)
else:
    print(False)

s = input()
n = len(s)
print(s[:-1:-(n//2)-1])
print('---')
print(s[:- (n//2)-1:-1])
first = s[:n//2]
last = s[:- (n//2)-1:-1]
if first == last:
    print(True)
else:
    print(False)