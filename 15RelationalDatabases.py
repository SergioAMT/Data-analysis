# funcion que acepte una lista de string como parametro
# como segundo argumento opcional un booleano
# debe formatear la lista en operaciones matematicas en formato vertical
# debe devolver "Error: Too many problems" si son mas de 5 operaciones
# solo acepta suma y resta, "Error: Operator must be '+' or '-'"
# solo se acepta numeros, Error: Numbers must only contain digits
# Error: Numbers cannot be more than four digits.
import re


def arithmetic_arranger(problems, solve=False):
    if (len(problems) > 5):
        printrint("Error: Too many problems.") 

    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""
    for problem in problems:
        if (re.search("[^\s0-9.+-]", problem)):
            if (re.search("[/]", problem) or re.search("[*]", problem)):
                print( "Error: Operator must be '+' or '-'.")
            print("Error: Numbers must only contain digits.") 

        firstNumber = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        secondNumber = problem.split(" ")[2]

        if (len(firstNumber) >= 5 or len(secondNumber) >= 5):
            printrint("Error: Numbers cannot be more than four digits.") 

        sum = ""
        if (operator == "+"):
            sum = str(int(firstNumber) + int(secondNumber))
        elif (operator == "-"):
            sum = str(int(firstNumber) - int(secondNumber))

        length = max(len(firstNumber), len(secondNumber)) + 2
        top = str(firstNumber).rjust(length)
        bottom = operator + str(secondNumber).rjust(length - 1)
        line = ""
        res = str(sum).rjust(length)
        for s in range(length):
            line += "-"

        if problem != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumx += res + '    '
        else:
            first += top
            second += bottom
            lines += line
            sumx += res

    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second + "\n" + lines
    print(string) 
    
    
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)