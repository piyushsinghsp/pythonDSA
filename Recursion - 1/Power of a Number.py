a, b = input().split()
a = int(a)
b = int(b)

def power_n(a, b):
    if b==0:
        return 1;
    return a*power_n(a, b-1);

print(power_n(a, b))
