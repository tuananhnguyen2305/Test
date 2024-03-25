def foo(cakeOrdered):
    
    ans = 0
    if cakeOrdered < 0 | cakeOrdered > 100:
        return "Input không hợp lệ"
    elif cakeOrdered < 10:
        return 20
    elif 10 <= cakeOrdered <= 50:
        ans = cakeOrdered + cakeOrdered * 0.2
    else:
        ans = cakeOrdered + cakeOrdered * 0.05
    return int(ans) if (ans == int(ans)) else int(ans) + 1
print(foo(-1)) # R1
print(foo(5)) # R2
print(foo(40)) # R3
print(foo(60)) # R4
print(foo(120)) # R5