import ply.lex as lex

# Lista de tokens
tokens = (
    'IDENTIFIER', 'EQUALS', 'NUMBER', 'FLOAT', 'STRING',
)

# Regras para tokens simples
t_EQUALS = r'='
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_FLOAT = r'\d+\.\d+'
t_NUMBER = r'\d+'
t_STRING = r'\"[^\"]*\"|\'[^\']*\'' # Strings com aspas duplas ou simples

# Ignorar espaços e tabulações
t_ignore = ' \t\n'

# Tratamento de erros
def t_error(t):
    print(f"Caractere inválido '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()