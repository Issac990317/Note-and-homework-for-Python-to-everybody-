def computepay(h, r):
    if h <= 40:
        return h * r
    else:
         return 40 * r + (h - 40) * r * 1.5

h = float(input("Enter Hours: "))
r = float(input("dollar for per hour: "))
p = computepay(h, r)
print("Pay", p)