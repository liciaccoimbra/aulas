# 1. Recebendo as notas (o 'float' garante que o programa entenda números com vírgula, como 7.5)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# 2. Encontrando a maior nota
# A função max() simplesmente olha para as variáveis e escolhe a maior
maior_nota = max(nota1, nota2, nota3)

# 3. Calculando a média
# É muito importante usar os parênteses para somar tudo ANTES de dividir por 3
media = (nota1 + nota2 + nota3) / 3

# 4. Definindo o status com a estrutura de decisão
if media >= 7:
    status = "Aprovado"
elif media < 5:
    status = "Reprovado"
else:
    # Se não é maior/igual a 7 nem menor que 5, só sobrou a opção do meio
    status = "Substitutiva"

# 5. Mostrando o resultado final
print("Maior Nota:", maior_nota)
print("Média:", round(media, 2))  # A função round() arredonda para 2 casas decimais
print("Status:", status)
