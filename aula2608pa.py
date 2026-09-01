
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

notaMaxima = max(nota1, nota2, nota3)

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    status = "Aprovado"
elif media < 5:
    status = "Reprovado"
else:
    status = "Substitutiva"

print("Nota máxima:", notaMaxima)
print("Média:", media)
print("Status:", status)