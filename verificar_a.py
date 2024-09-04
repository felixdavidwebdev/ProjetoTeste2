def contar_letra_a(s):
    s = s.lower()  # Converte a string para minúsculas
    count = s.count('a')
    
    if count > 0:
        return f"A letra 'a' aparece {count} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

# Teste do programa
string = input("Informe uma string: ")
print(contar_letra_a(string))