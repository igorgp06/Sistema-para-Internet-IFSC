import math

def calculadora():
    print("\n=== Mini Calculadora ===")
    print("Operações: +  -  *  /  sqrt  pow  log  sin  cos  tan")

    try:
        operacao = input("Digite a operação: ").strip().lower()

        # um número
        if operacao in ["sqrt", "log", "sin", "cos", "tan"]:
            num = float(input("Digite o número: "))

            if operacao == "sqrt":
                if num < 0:
                    raise ValueError("Raiz quadrada não é definida para números negativos.")
                resultado = math.sqrt(num)  # raiz

            elif operacao == "log":
                if num <= 0:
                    raise ValueError("Logaritmo só é definido para números positivos.")
                resultado = math.log(num)  # logaritmo natural

            elif operacao == "sin":
                resultado = math.sin(math.radians(num))  # seno em graus

            elif operacao == "cos":
                resultado = math.cos(math.radians(num))  # cosseno em graus

            elif operacao == "tan":
                resultado = math.tan(math.radians(num))  # tangente em graus

        # dois numeros
        elif operacao in ["+", "-", "*", "/", "pow"]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2
            elif operacao == "pow":
                resultado = math.pow(num1, num2)  # potencia

        else:
            raise ValueError("Operação inválida.")

        print(f"Resultado: {resultado:.4f}")

    except ValueError as ve:
        print("Entrada ou operação inválida:", ve)

    except ZeroDivisionError as zde:
        print("Erro:", zde)

    except Exception as e:
        print("Erro inesperado:", e)

if __name__ == "__main__":
    while True:
        calculadora()
        if input("Deseja continuar? (s/n): ").strip().lower() == "s":
            print("Continuando...")
        else:
            print("Encerrando a calculadora. Até mais!")
            break
