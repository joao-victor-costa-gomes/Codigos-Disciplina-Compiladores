class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self):
        if self.pos < len(self.tokens):
            self.pos += 1

    def expr(self):
        # A expressão começa com uma variável (v), seguido de um índice.
        if self.current_token() == 'v':
            self.var()  # Consome a variável (v)
            self.consume()  # Consome o '['
            self.index()  # Analisa o índice
            self.consume()  # Consome o ']'

            # Verifica se estamos no final da cadeia
            if self.current_token() is None:
                return True  # Cadeia válida e completamente processada
            else:
                raise SyntaxError(f"Unexpected token after ']'")

        return False  # Se não começar com 'v', não é válido

    def var(self):
        # A variável é representada por 'v'
        if self.current_token() == 'v':
            self.consume()

    def index(self):
        # O índice pode ser um número, uma string, uma variável ou um intervalo (slice).
        token = self.current_token()
        if token in ('p', 'n'):
            self.num()  # Número (positivo ou negativo)
        elif token == 's':
            self.str()  # String
        elif token == 'v':
            self.nested()  # Acesso aninhado a uma variável
        elif token == ':':
            self.slice()  # Intervalo (slice)
        else:
            raise SyntaxError(f"Unexpected token in index: {token}")

    def num(self):
        # O token 'p' ou 'n' representa um número positivo, zero ou negativo.
        if self.current_token() in ('p', 'n'):
            self.consume()
        else:
            raise SyntaxError("Expected number (p or n)")

    def str(self):
        # O token 's' representa uma string (nome de coluna).
        if self.current_token() == 's':
            self.consume()
        else:
            raise SyntaxError("Expected string (s)")

    def nested(self):
        # Acesso aninhado à variável (ex: v[ p ])
        if self.current_token() == 'v':
            self.var()
            self.consume()  # Consome o '['
            self.index()
            self.consume()  # Consome o ']'

    def slice(self):
        # Um intervalo é representado por dois índices separados por ':'.
        self.consume()  # Consome o ':'
        
        # O intervalo pode ser composto de números ou strings, e ambos podem ser opcionais.
        token = self.current_token()
        if token in ('p', 'n'):
            self.num()
        elif token == 's':
            self.str()
        
        # Agora, verificamos o segundo índice do slice (pode ser opcional)
        if self.current_token() in ('p', 'n', 's', None):
            if self.current_token():
                self.index()
        else:
            raise SyntaxError("Invalid slice format")


# Função para rodar o analisador e verificar se a cadeia é aceita
def run_parser(tokens):
    parser = Parser(tokens)
    try:
        if parser.expr():
            print("Cadeia aceita!")
        else:
            print("Cadeia não aceita!")
    except SyntaxError as e:
        print(f"Cadeia não aceita! Erro: {e}")

# Exemplo de uso
tokens1 = ['v', '[', 'v', '[', 'p', ':', 'p', ']', ']']
tokens2 = ['v', '[', 'p', ':', 's', ']']
tokens3 = ['v', '[', 's', ':', 's', ']']
tokens4 = ['v', '[', 'v', '[', 'n', ':', 'n', ']', ']']
tokens5 = ['v', '[', 'p', ':', 'n', ']']

print("Testando a cadeia 1:")
run_parser(tokens1)  # Esperado: "Cadeia aceita!"

print("\nTestando a cadeia 2:")
run_parser(tokens2)  # Esperado: "Cadeia aceita!"

print("\nTestando a cadeia 3:")
run_parser(tokens3)  # Esperado: "Cadeia aceita!"

print("\nTestando a cadeia 4:")
run_parser(tokens4)  # Esperado: "Cadeia aceita!"

print("\nTestando a cadeia 5:")
run_parser(tokens5)  # Esperado: "Cadeia aceita!"
