import ply.yacc as yacc
from lexer import tokens

# Regras para múltiplas declarações
def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 3:
        p[0] = f"{p[1]}\n{p[2]}"
    else:
        p[0] = p[1]

# Regra para declaração
def p_statement_assign(p):
    '''statement : IDENTIFIER EQUALS value'''
    p[0] = f"{p[1]} = {p[3]}"

# Regra para valores
def p_value(p):
    '''value : NUMBER
             | FLOAT
             | STRING'''
    p[0] = p[1]

# Tratamento de erros
def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno} perto de {p.value}")
    else:
        print("Erro de sintaxe no EOF")

parser = yacc.yacc()