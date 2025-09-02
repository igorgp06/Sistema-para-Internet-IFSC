def calculadora():
    print("=== Mini Calculadora ===")
    print("Operações disponíveis: +  -  *  /")
    
    try:
        
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
        
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            try:
                resultado = num1 / num2
            except ZeroDivisionError:
                print("Erro: divisão por zero não é permitida.")
                return
        else:
            print("Operação inválida. Use apenas +, -, * ou /.")
            return

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Entrada inválida! Digite apenas números válidos.")


if __name__ == "__main__":
    while True:
        calculadora()
        continuar = input("Deseja fazer outra operação? (s/n): ").lower()
        if continuar != "s":
            print("Encerrando a calculadora. Até mais!")
            break
