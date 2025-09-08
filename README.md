# Seminário de Programação Orientada a Objetos (IFSC 02/2025)

Um repositório para guardar o nosso progresso no seminário de Progamação Orientada a Objetos 

## Funcionamento

Vejamos a funcionalidade de cada bloco de código e sua função na calculadora

~~~python
import math

def calculadora():
    print("\n=== Mini Calculadora ===")
    print("Operações: +  -  *  /  sqrt  pow  log  sin  cos  tan")
~~~
Criada a função responsável por manter o programa ativo. Podemos entendê-la como o coração do sistema.   
Aqui também importamos a biblioteca `math`, que nos ajudará a realizar operações matemáticas mais complexas, como raiz quadrada, logaritmo e etc.     
Além disso, temos um `print` que exibe o título da calculadora e as operações disponíveis para o usuário.

~~~python
try:
    operacao = input("Digite a operação: ").strip().lower()
~~~    
Salvando na variável `operação` o que o usuário deseja fazer.   

~~~python
# um numero
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
~~~
O primeiro bloco do `try`. Aqui tratamos todas as operações que utilizam **um número**, usando a biblioteca [math](https://docs.python.org/3/library/math.html).   
Isso deixa o código mais simples e garante cálculos mais precisos.    
Note também que temos dois `raise`, vejamos:
- O primeiro `raise` captura o erro de raiz quadrada de número negativo.    
- O segundo `raise` captura o erro de logaritmo de número negativo ou zero.   
Ambos retornam um erro de valor com uma mensagem personalizada para o usuário.

~~~python
# 2 numeros
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
        resultado = math.pow(num1, num2)  # potência
else:
    raise ValueError("Operação inválida.")
~~~
No segundo bloco nós tratamos as operações que exigem **dois números.**
Note o `raise` que aponta que a divisão por zero não é permitida, retornando uma mensagem de erro personalizada.
Já o último `raise` é responsável por capturar operações inválidas, informando ao usuário que a **operação digitada não existe.**

~~~python
print(f"Resultado: {resultado:.4f}")
~~~
O resultado é exibido apenas se o cálculo for realizado com sucesso. O formato `.4f` **garante 4 casas decimais.**

~~~python
except ValueError as ve:
    print("Entrada ou operação inválida:", ve)

except ZeroDivisionError as zde:
    print("Erro:", zde)
        
except Exception as e:
    print("Erro inesperado:", e)
~~~
Após o `try` temos o tratamento de exceções.   
- O primeiro `except` captura erros de valor (ex: letras em vez de números ou operações inválidas).    
- O segundo captura especificamente **divisão por zero**.   
- O último é um capturador genérico para **qualquer outro erro inesperado** que possa ocorrer.   

~~~python
if __name__ == "__main__":
    while True:
        calculadora()
        if input("Deseja continuar? (s/n): ").strip().lower() == "s":
            print("Continuando...")
        else:
            print("Encerrando a calculadora. Até mais!")
            break
~~~
Este bloco final mantém o programa em execução contínua, perguntando ao usuário se ele deseja realizar novos cálculos. 

## Controle Versional (GIT)

O projeto segue o seguinte padrão de sufixos:

| Sufixo    | Descrição                                                                  |
| --------- | -------------------------------------------------------------------------- |
| [WORK]    | Versão em desenvolvimento, sujeita a alterações.                           |
| [ADD]     | Adição de algo novo para o projeto, sem remoções consideráveis.            |
| [RE-WORK] | Alteração considerável no projeto, com muitas remoções e alterações.       |
| [DEL]     | Remoção de pastas, linhas de código, imagens, etc.                         |
| [UPDATE]  | Melhorias de performance, refatorações, etc.                               |
| [PATCH]   | Correção de algo que funcionava, mas de forma inadequada.                  |
| [INFO]    | Alterações de informações, como README ou conteúdo textual do site.        |
| [FIX]     | Correção de falhas.                                                        |
| [DEPLOY]  | Relacionado ao primeiro o deploy do projeto. Pode ser usado uma vez só.    |
| [FINAL]   | Versão final do projeto, sem mais alterações e/ou remoções significativas. |

## Responsáveis

[Igor Gonçalves](https://igdeveloper.com.br)   
[Eduardo Dutra](https://github.com/000Eduard000)   