N_inp = int(input("Введите число: "))
S = 0
if N_inp < 0:
    N = N_inp * -1
for i in range (1, N+1):
    S = S+i
print(f"Сумма всех чисел в числе {N_inp} равна {S}")
