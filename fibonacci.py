def is_fibonacci(n):
    if n < 0:
        return False

    # Inicializando a sequência de Fibonacci
    a, b = 0, 1
    fibonacci_sequence = [a, b]

    # Gerando a sequência até o número ser maior ou igual ao informado
    while b < n:
        a, b = b, a + b
        fibonacci_sequence.append(b)

    # Verificando se o número pertence à sequência
    if n in fibonacci_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

# Teste do programa
numero = int(input("Informe um número: "))
print(is_fibonacci(numero))
