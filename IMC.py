

print("Calculadora de IMC")
print("Coloque os seus dados na calculadora e calcule o seu IMC:")

peso = float(input("\nEscolha o peso: \n"))
altura = float(input("Escolha a altura: \n"))

imc = peso /(altura * altura)

print("Esse é o seu IMC(Índice de massa corporal):\n%.2f"% imc)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc <= 24.9:
    print("Você está no peso ideal.")
elif imc <= 29.9:
    print("Levemente acima do peso.")
elif imc <= 34.9:
    print("Obesidade grau 1")
elif imc <= 39.9:
    print("Obesidade grau 2 (Severa).")
else:
    print("Obesidade grau 3 (Mórbida).")