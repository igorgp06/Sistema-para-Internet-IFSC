import math

def calculadora():
    print("=== Mini Calculadora ===")
    print("Operações disponíveis: +  -  *  /  sqrt  pow  log  sin  cos  tan")
    
    try:
        operacao = input("Digite a operação: ").lower()

        # 1 numero
        if operacao in ["sqrt", "log", "sin", "cos", "tan"]:
            num = float(input("Digite o número: "))

            if operacao == "sqrt":
                if num < 0:
                    raise ValueError("Não é possível calcular a raiz quadrada de número negativo.")
                resultado = math.sqrt(num)

            elif operacao == "log":
                if num <= 0:
                    raise ValueError("O logaritmo só é definido para números positivos.")
                resultado = math.log(num)

            elif operacao == "sin":
                resultado = math.sin(math.radians(num)) # muda pra graus (seno)

            elif operacao == "cos":
                resultado = math.cos(math.radians(num)) # coseno

            elif operacao == "tan":
                resultado = math.tan(math.radians(num)) # tangente

        # 2 numeros
        else:
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
                resultado = math.pow(num1, num2)

            else:
                raise ValueError("Operação inválida.")

        print(f"Resultado: {resultado}")

    except ValueError as ve:
        print("Entrada ou operação inválida:", ve)

    except ZeroDivisionError as zde:
        print("Erro:", zde)

    except Exception as e:
        print("Ocorreu um erro inesperado:", e)

if __name__ == "__main__":
    while True:
        calculadora()
        continuar = input("Deseja fazer outra operação? (s/n): ").lower()
        if continuar != "s":
            print("Encerrando a calculadora. Até mais!")
            break
