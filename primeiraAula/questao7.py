print("Calculadora da economia!")

valorCompra = float(input("Digite o valor da sua compra: "))

disconto = valorCompra %15
valorFinal = valorCompra - disconto

print("Sua compra era de ", valorCompra, " e você recebeu um disconto de ", disconto, "pagando apenas ", valorFinal)

