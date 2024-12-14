from lexer import lexer
from parser import parser

def transpile(code):
    result = parser.parse(code, lexer=lexer)
    return result

if __name__ == "__main__":
    with open("codigo_entrada.txt", "r") as file:
        code = file.read()

    ruby_code = transpile(code)
    print("Código Ruby gerado:")
    print(ruby_code)
