import ply.yacc as yacc
from tokens import tokens

# Regras para múltiplas declarações
def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 3:
        p[0] = f"{p[1]}\n{p[2]}"
    else:
        p[0] = p[1]

# Regra para declaração de atribuição
def p_statement_assign(p):
    '''statement : IDENTIFIER EQUALS expression'''
    p[0] = f"{p[1]} = {p[3]}"

# Regra para comentários
def p_statement_comment(p):
    '''statement : COMMENT'''
    p[0] = p[1]

# Regras para expressões aritméticas
def p_expression_binop(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    if p[2] == '+':
        p[0] = f"{p[1]}+{p[3]}"
    elif p[2] == '-':
        p[0] = f"{p[1]}-{p[3]}"

def p_expression_term(p):
    '''expression : term'''
    p[0] = p[1]

def p_term_binop(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''
    if p[2] == '*':
        p[0] = f"{p[1]}*{p[3]}"
    elif p[2] == '/':
        p[0] = f"{p[1]}/{p[3]}"

def p_term_factor(p):
    '''term : factor'''
    p[0] = p[1]

def p_factor_number(p):
    '''factor : NUMBER
              | FLOAT
              | STRING
              | TRUE
              | FALSE'''
    p[0] = p[1]

# Regra para expressões com parênteses
def p_factor_expr(p):
    '''factor : LPAREN expression RPAREN'''
    p[0] = f"({p[2]})"

# Tratamento de erros
def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno} perto de {p.value}")
    else:
        print("Erro de sintaxe no EOF")

parser = yacc.yacc()