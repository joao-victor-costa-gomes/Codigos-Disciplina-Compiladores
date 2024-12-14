import ply.lex as lex
from tokens import tokens

# Regras para tokens simples
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_FLOAT = r'\d+\.\d+'
t_NUMBER = r'\d+'
t_STRING = r'\"[^\"]*\"|\'[^\']*\''  # Strings com aspas duplas ou simples
t_COMMENT = r'\#.*'  # Comentários de uma linha

# Regras para valores booleanos
def t_TRUE(t):
    r'True'
    t.value = 'true'
    return t

def t_FALSE(t):
    r'False'
    t.value = 'false'
    return t

# Regras para ignorar espaços e tabulações
t_ignore = ' \t\n'

# Tratamento de erros
def t_error(t):
    print(f"Caractere inválido '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
