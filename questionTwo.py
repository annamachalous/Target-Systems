def contar_a(texto):
    # Conta as ocorrências de 'a' e 'A' na string
    contagem = texto.lower().count('a')
    
    # Verifica se a letra 'a' foi encontrada e exibe o resultado
    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

# Entrada do usuário
texto = input("Digite uma string: ")
contar_a(texto)
