"""
Projeto feito propositalmente sem a utilização de bibliotecas externas
"""

print("Cálculadora ineficiente\n")
print("Será necessário digitar dois números e \n\
qual operação deseja realizar")
num1 = str(input("Digite o primeiro número: "))
num2 = str(input("Digite o segundo número: "))
operacao = str(input("Qual operação deseja realizar? "))


def calcula(valor):
    # Função com objetivo de identificar qual operação foi digitada e executar uma função de acordo
    match valor:
        # a função match compara o valor e executa a função correspondente
        case "soma" | "somar" | "+":
            resultado = num1 + num2
            return resultado
        case "subtrair" | "diminuir" | "-":
            resultado = num1 - num2
            return resultado
        case "multiplicar" | "*":
            resultado = num1 * num2
            return resultado
        case "dividir" | "/":
            resultado = num1 / num2
            return resultado
        case _:
            raise ValueError("Operação inválida")


num1 = int(num1) if num1.isdigit() else float(num1)  # Determina se foi digitado um número e se é int ou float
num2 = int(num2) if num2.isdigit() else float(num2)


def status(result):
    # formata e imprime os valores calculados
    print(f"O resultado da operação é ", result)
    print(f"{result} é do tipo {type(result)}")
    print(f"{result} é um número positivo"
          if result >= 0 else
          f"{result} é um número negativo")
    print(f"O número {result}é par"
          if result % 2 == 0 else
          f"{result} é um número impar")


calcula(operacao)
status(calcula(operacao))
