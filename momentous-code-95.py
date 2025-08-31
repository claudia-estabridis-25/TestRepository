a, b, c, d = map(int, input().split())
producto = a*b*c*d
menor = min(a, b, c, d)
mayor = max(a, b, c, d)

if producto <= 250:
    print(producto)

else:
    if 10 in (a,b,c,d):
        producto //= menor
    else:
        producto //= mayor
    
    if producto >= 250:
        print("pierdes")
    else:
        print(producto)
