def hisobla(a, b, amal="+"):
        if amal == "+":
        return a + b
    elif amal == "-":
        return a - b
    elif amal == "*":
        return a * b
    elif amal == "/":
        return a / b if b != 0 else "Nolga bo'lish mumkin emas"
    else:
        return "Noto'g'ri amal"
print(f"5 + 3 = {hisobla(5, 3, '+')}")
print(f"10 - 4 = {hisobla(10, 4, '-')}")
print(f"6 * 7 = {hisobla(6, 7, '*')}")
print(f"15 / 3 = {hisobla(15, 3, '/')}")
print(f"10 / 0 = {hisobla(10, 0, '/')}")
