# ==========================================
# 1. CALCULADORA SIMPLES
# ==========================================

print("--- 1. Calculadora ---")

numero1 = 10.0
numero2 = 2.0
operacao = '+'

if operacao == '+':
    print("Resultado da soma:", numero1 + numero2)

elif operacao == '-':
    print("Resultado da subtração:", numero1 - numero2)

elif operacao == '*':
    print("Resultado da multiplicação:", numero1 * numero2)

elif operacao == '/':
    if numero2 != 0:
        print("Resultado da divisão:", numero1 / numero2)
    else:
        print("Erro: Não é possível dividir por zero!")

else:
    print("Operação inválida.")


# ==========================================
# 2. PAR OU ÍMPAR
# ==========================================

print("--- 2. Teste de Par ou Ímpar ---")

numero = 7

if numero % 2 == 0: 
    print("O número", numero, "é Par!")
else:
    print("O número", numero, "é Ímpar!")

print("\n")

# ==========================================
# 3. FÓRMULA DE BHASKARA (Valores do quadro: 2, 1, 0)
# ==========================================

print("--- 3. Calculadora de Bhaskara ---")

valorA = 2
valorB = 1
valorC = 0

valorDelta = (valorB ** 2) - (4 * valorA * valorC)
print("O valor de Delta é:", valorDelta)


if valorDelta > 0:
    print("Delta > 0: 2 raízes reais.")
    raiz1 = (-valorB + (valorDelta ** 0.5)) / (2 * valorA)
    raiz2 = (-valorB - (valorDelta ** 0.5)) / (2 * valorA)
    print("Raiz 1:", raiz1)
    print("Raiz 2:", raiz2)
    
elif valorDelta == 0:
    print("Delta = 0: 1 raiz real.")
    raiz1 = -valorB / (2 * valorA)
    print("A raiz é:", raiz1)
    
else:
    print("Delta < 0: Não tem raiz real.")
