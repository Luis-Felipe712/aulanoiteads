x = 17
y = 3.2

resultado_1 = x / 4 + y
print("a) x / 4 + y =", resultado_1)

resultado_2 = x * y ** 6
print("b) x * y ** 6 =", resultado_2)

resultado_1 = x % 4
resultado_2 = int(y * 10) // 4
resultado = (resultado_1, resultado_2)
print("c) (x % 4) , (((int) y * 10) // 4) =", resultado)

resultado = (x / 6 // x / 3) + 4
print("d) (x / 6 // x / 3) + 4 =", resultado)