def pertence_fibonacci(n):
    # Inicia a sequência de Fibonacci
    a, b = 0, 1
    # Gera a sequência até o valor de b ser maior ou igual a n
    while b < n:
        a, b = b, a + b
    # Verifica se o número informado pertence à sequência
    return b == n or n == 0

# Entrada do usuário
num = int(input("Informe um número para verificar se ele pertence à sequência de Fibonacci: "))

# Verifica e exibe o resultado
if pertence_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
