import timeit as t

def soma1(n): 
    return (n * (n + 1)) // 2

tmp_inicial = t.default_timer()
soma = print("A soma dos números é: ", soma1(-00000000000000))
tmp_final = t.default_timer()
print(f"Tempo gasto: {tmp_final - tmp_inicial:.10f} segundos")