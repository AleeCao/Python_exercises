aux = 0
fibo = aux
for i in range(0,51):
    if fibo == 0:
        fibo = 1
        print(fibo)
    else:
        fibo = aux + fibo
        aux = fibo - aux
        print(fibo)