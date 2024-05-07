# Exercício 10

# Faça uma função lambda que recebe dois valores numéricos como parâmetro.
# Ao primeiro valor, sempre some 5. Em seguida multiplique ambos e retorne
# o resultado.

res = lambda x, y: (x+5) * y
print((res(5, 10)))
print((res(1, 2)))
print((res(10, 5)))
print((res(10, 10)))