

class ParserError(Exception):
    """Exceção personalizada para erros de parser."""
    pass

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0  # Posição atual na lista de tokens

    def token_atual(self):
        """Retorna o token atual ou '$' se estiver no final."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return '$'

    def consumir(self, esperado):
        """
        Consome o token atual se corresponder ao esperado.
        Levanta um erro caso contrário.
        """
        if self.token_atual() == esperado:
            self.pos += 1
        else:
            raise ParserError(f"Esperado token '{esperado}', mas encontrado '{self.token_atual()}'.")

    def parse(self):
        """
        Inicia o processo de parsing.
        Retorna True se toda a entrada for analisada com sucesso, False caso contrário.
        """
        try:
            self.expr()
            if self.token_atual() == '$':
                return True
            else:
                raise ParserError(f"Token inesperado '{self.token_atual()}' após o parsing completo.")
        except ParserError:
            return False

    # Implementações das Regras da Gramática

    def expr(self):
        """
        expr → var '[' index ']'
        """
        self.var()
        self.consumir('[')
        self.index()
        self.consumir(']')

    def var(self):
        """
        var → v
        """
        self.consumir('v')

    def index(self):
        """
        index → nump | numn | str | nested | slice
        Decisão baseada no token atual.
        FIRST(index) = { p, n, s, v, ':' }
        """
        token = self.token_atual()
        if token == 'v':
            self.nested()
        elif token == 'p':
            # Verifica se o próximo token é ':' para decidir entre nump e slice
            if self.proximo_token() == ':':
                self.slice()
            else:
                self.nump()
        elif token == 'n':
            if self.proximo_token() == ':':
                self.slice()
            else:
                self.numn()
        elif token == 's':
            if self.proximo_token() == ':':
                self.slice()
            else:
                self.str_()
        elif token == ':':
            self.slice()
        else:
            raise ParserError(f"Token inesperado em index: '{token}'.")

    def nump(self):
        """
        nump → p
        """
        self.consumir('p')

    def numn(self):
        """
        numn → n
        """
        self.consumir('n')

    def str_(self):
        """
        str → s
        """
        self.consumir('s')

    def nested(self):
        """
        nested → var '[' index ']'
        """
        self.var()
        self.consumir('[')
        self.index()
        self.consumir(']')

    def slice(self):
        """
        slice → str ':' str 
               | str ':' 
               | ':' str 
               | ':' 
               | nump ':' nump 
               | nump ':' 
               | ':' nump 
               | numn ':' numn 
               | numn ':' 
               | ':' numn
        Decisão baseada no token atual.
        """
        token = self.token_atual()
        if token in ['p', 'n', 's']:
            initial_type = token
            if initial_type == 'p':
                self.nump()
            elif initial_type == 'n':
                self.numn()
            elif initial_type == 's':
                self.str_()

            if self.token_atual() == ':':
                self.consumir(':')
                if self.token_atual() in ['p', 'n', 's']:
                    # Enforce that the second type matches the first type
                    if self.token_atual() != initial_type:
                        raise ParserError(f"Tipo de slice não corresponde: esperado '{initial_type}', mas encontrado '{self.token_atual()}'.")
                    if initial_type == 'p':
                        self.nump()
                    elif initial_type == 'n':
                        self.numn()
                    elif initial_type == 's':
                        self.str_()
        elif token == ':':
            self.consumir(':')
            if self.token_atual() in ['p', 'n', 's']:
                self.consumir(self.token_atual())
        else:
            raise ParserError(f"Token inesperado em slice: '{token}'.")

    def proximo_token(self):
        """
        Olha o próximo token sem consumir o atual.
        Retorna o próximo token ou '$' se estiver no final.
        """
        if self.pos + 1 < len(self.tokens):
            return self.tokens[self.pos + 1]
        return '$'

def tokenizar(string_de_entrada):
    """
    Tokeniza a string de entrada em uma lista de tokens.
    Assume que os tokens estão separados por espaços.
    """
    import re
    # Adiciona espaços ao redor de colchetes e dois pontos
    string_de_entrada = re.sub(r'([\[\]:])', r' \1 ', string_de_entrada)
    return string_de_entrada.strip().split()

def testar_parser(string_de_entrada):
    """
    Testa o parser com a string de entrada fornecida.
    Imprime se a entrada é aceita ou rejeitada.
    """
    tokens = tokenizar(string_de_entrada)
    tokens.append('$')  # Adiciona marcador de fim
    parser = Parser(tokens)
    resultado = parser.parse()
    if resultado:
        print(f"A entrada '{string_de_entrada}' foi ACEITA.")
    else:
        print(f"A entrada '{string_de_entrada}' foi REJEITADA.")

if __name__ == "__main__":
    # Casos de Teste - Todos DEVEM SER ACEITAS
    entradas_teste_aceitas = [
        "v[p]",
        "v[n]",
        "v[s]",
        "v[p:p]",
        "v[n:n]",
        "v[:p]",
        "v[p:]",
        "v[:n]",
        "v[n:]",
        "v[:]",
        "v[v[p]]",
        "v[v[n]]",
        "v[v[s]]",
        "v[v[p:p]]",
        "v[v[n:n]]",
        "v[v[s:s]]",
        "v[v[p:]]",
        "v[v[:p]]",
        "v[v[n:]]",
        "v[v[:n]]",
        "v[v[s:]]",
        "v[v[:s]]"
    ]

    # Casos de Teste - Novos, DEVEM SER REJEITADAS
    entradas_teste_rejeitadas = [
        "v[p:n]",
        "v[n:p]",
        "v[p:s]",
        "v[s:p]",
        "v[n:s]",
        "v[s:n]",
        "v[v[n:p]]",
        "v[v[p:n]]",
        "v[v[s:p]]",
        "v[v[p:s]]",
        "v[v[s:n]]",
        "v[v[n:s]]"
    ]

    # Testando Entradas Aceitas
    print("=== Entradas que DEVEM SER ACEITAS ===")
    for entrada in entradas_teste_aceitas:
        testar_parser(entrada)

    # Testando Entradas Rejeitadas
    print("\n=== Entradas que DEVEM SER REJEITADAS ===")
    for entrada in entradas_teste_rejeitadas:
        testar_parser(entrada)
