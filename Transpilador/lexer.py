# lexer.py

import ply.lex as lex
from tokens import tokens

# Operadores de comparação
t_GE = r'>='
t_LE = r'<='
t_EQ = r'=='
t_NE = r'!='

# Operadores compostos
t_PLUS_EQUALS = r'\+='
t_MINUS_EQUALS = r'-='
t_TIMES_EQUALS = r'\*='
t_DIVIDE_EQUALS = r'/='

# Operadores de um único caractere
t_GT = r'>'
t_LT = r'<'
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','

# Delimitadores
t_COLON = r':'

# Definição de strings com suporte a caracteres escapados
t_STRING = r'\"([^\\\"]|\\.)*\"|\'([^\\\']|\\.)*\''

# Identificadores
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z_0-9]*'

# Literais numéricos
t_FLOAT = r'\d+\.\d+'
t_NUMBER = r'\d+'

# Comentários
t_COMMENT = r'\#.*'

# Palavras-chave definidas como funções para retornar o token correspondente
def t_PRINT(t):
    r'print'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_FOR(t):
    r'for'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_DEF(t):
    r'def'
    return t

def t_IN(t):
    r'in'
    return t

def t_TRUE(t):
    r'True'
    t.value = 'true'
    return t

def t_FALSE(t):
    r'False'
    t.value = 'false'
    return t

def t_AND(t):
    r'and'
    t.value = '&&'
    return t

def t_OR(t):
    r'or'
    t.value = '||'
    return t

# Regra para quebras de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caractere a serem ignorados (espaços e tabulações)
t_ignore = ' \t'

# Regra para tratamento de erros
def t_error(t):
    print(f"Caractere inválido '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()
