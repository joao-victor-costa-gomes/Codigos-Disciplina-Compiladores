# parser.py

import ply.yacc as yacc
from tokens import tokens

# Definição de precedência para operadores
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NE', 'GT', 'LT', 'GE', 'LE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),  # Suporte para operador unário
)

# Tabela de símbolos para rastrear variáveis definidas
symbol_table = set()

# Regra inicial
def p_program(p):
    '''program : statements'''
    p[0] = p[1]

# Regras para múltiplas declarações
def p_statements_multiple(p):
    '''statements : statements statement'''
    p[0] = f"{p[1]}\n{p[2]}"

def p_statements_single(p):
    '''statements : statement'''
    p[0] = p[1]

# Regras para atribuição ou print
def p_statement_assign_or_print(p):
    '''statement : IDENTIFIER EQUALS expression
                 | PRINT LPAREN expression RPAREN'''
    if p[1] == 'print':
        p[0] = f"puts {p[3]}"
    else:
        symbol_table.add(p[1])  # Adiciona a variável à tabela de símbolos
        p[0] = f"{p[1]} = {p[3]}"

# Regras para operadores compostos (e.g., +=)
def p_statement_compound_assign(p):
    '''statement : IDENTIFIER PLUS_EQUALS expression
                 | IDENTIFIER MINUS_EQUALS expression
                 | IDENTIFIER TIMES_EQUALS expression
                 | IDENTIFIER DIVIDE_EQUALS expression'''
    var = p[1]
    operador = p[2][0]  # '+' de '+=', '-' de '-=', etc.
    if var not in symbol_table:
        print(f"Warning: Variável '{var}' usada antes de ser definida na linha {p.lineno(1)}")
    p[0] = f"{var} {operador}= {p[3]}"

# Regras para comentários
def p_statement_comment(p):
    '''statement : COMMENT'''
    # Transforma o comentário de Python (# ...) em comentário de Ruby (# ...)
    p[0] = p[1]

# Regras para expressões lógicas
def p_expression_or(p):
    '''expression : expression OR and_expression'''
    p[0] = f"{p[1]} || {p[3]}"

def p_expression_and(p):
    '''and_expression : and_expression AND comparison'''
    p[0] = f"{p[1]} && {p[3]}"

def p_expression_and_single(p):
    '''and_expression : comparison'''
    p[0] = p[1]

def p_expression_and_expression(p):
    '''expression : and_expression'''
    p[0] = p[1]

# Regras para comparações
def p_comparison_gt(p):
    '''comparison : arithmetic_expression GT arithmetic_expression'''
    p[0] = f"{p[1]} > {p[3]}"

def p_comparison_lt(p):
    '''comparison : arithmetic_expression LT arithmetic_expression'''
    p[0] = f"{p[1]} < {p[3]}"

def p_comparison_ge(p):
    '''comparison : arithmetic_expression GE arithmetic_expression'''
    p[0] = f"{p[1]} >= {p[3]}"

def p_comparison_le(p):
    '''comparison : arithmetic_expression LE arithmetic_expression'''
    p[0] = f"{p[1]} <= {p[3]}"

def p_comparison_eq(p):
    '''comparison : arithmetic_expression EQ arithmetic_expression'''
    p[0] = f"{p[1]} == {p[3]}"

def p_comparison_ne(p):
    '''comparison : arithmetic_expression NE arithmetic_expression'''
    p[0] = f"{p[1]} != {p[3]}"

def p_comparison_arithmetic(p):
    '''comparison : arithmetic_expression'''
    p[0] = p[1]

# Regras para expressões aritméticas
def p_arithmetic_expression_plus(p):
    '''arithmetic_expression : arithmetic_expression PLUS term'''
    p[0] = f"{p[1]} + {p[3]}"

def p_arithmetic_expression_minus(p):
    '''arithmetic_expression : arithmetic_expression MINUS term'''
    p[0] = f"{p[1]} - {p[3]}"

def p_arithmetic_expression_uminus(p):
    '''arithmetic_expression : MINUS arithmetic_expression %prec UMINUS'''
    p[0] = f"-{p[2]}"

def p_arithmetic_expression_term(p):
    '''arithmetic_expression : term'''
    p[0] = p[1]

# Regras para termos
def p_term_times(p):
    '''term : term TIMES factor'''
    p[0] = f"{p[1]} * {p[3]}"

def p_term_divide(p):
    '''term : term DIVIDE factor'''
    p[0] = f"{p[1]} / {p[3]}"

def p_term_factor(p):
    '''term : factor'''
    p[0] = p[1]

# Regras para fatores
def p_factor_number(p):
    '''factor : NUMBER
              | FLOAT
              | STRING
              | TRUE
              | FALSE'''
    p[0] = p[1]

def p_factor_identifier(p):
    '''factor : IDENTIFIER'''
    if p[1] not in symbol_table:
        print(f"Warning: Variável '{p[1]}' usada antes de ser definida na linha {p.lineno(1)}")
    p[0] = p[1]

def p_factor_expr(p):
    '''factor : LPAREN expression RPAREN'''
    p[0] = f"({p[2]})"

def p_factor_call(p):
    '''factor : IDENTIFIER LPAREN args RPAREN'''
    p[0] = f"{p[1]}({p[3]})"

# Regras para argumentos de funções
def p_args_multiple(p):
    '''args : expression COMMA args'''
    p[0] = f"{p[1]}, {p[3]}"

def p_args_single(p):
    '''args : expression'''
    p[0] = p[1]

def p_args_empty(p):
    '''args : empty'''
    p[0] = ''

# Adicionar regra para tratar expressões como declarações
def p_statement_expression(p):
    '''statement : expression'''
    p[0] = p[1]

# Regras para condicionais
def p_statement_if_else(p):
    '''statement : IF expression COLON statements ELSE COLON statements'''
    p[0] = f"if {p[2]}\n  {indent(p[4])}\nelse\n  {indent(p[7])}\nend"

def p_statement_if(p):
    '''statement : IF expression COLON statements'''
    p[0] = f"if {p[2]}\n  {indent(p[4])}\nend"

# Regras para loops while
def p_statement_while(p):
    '''statement : WHILE expression COLON statements'''
    p[0] = f"while {p[2]}\n  {indent(p[4])}\nend"

# Regras para loops for
def p_statement_for(p):
    '''statement : FOR IDENTIFIER IN expression COLON statements'''
    p[0] = f"for {p[2]} in {p[4]}\n  {indent(p[6])}\nend"

# Regras para definição de funções
def p_statement_function(p):
    '''statement : DEF IDENTIFIER LPAREN params RPAREN COLON statements'''
    p[0] = f"def {p[2]}({p[4]})\n  {indent(p[7])}\nend"

# Regras para parâmetros de funções
def p_params_multiple(p):
    '''params : IDENTIFIER COMMA params'''
    p[0] = f"{p[1]}, {p[3]}"

def p_params_single(p):
    '''params : IDENTIFIER'''
    p[0] = p[1]

def p_params_empty(p):
    '''params : empty'''
    p[0] = ''

# Função auxiliar para indentação
def indent(text, num_spaces=2):
    indented = ""
    for line in text.split('\n'):
        indented += ' ' * num_spaces + line + '\n'
    return indented.rstrip()

# Produção vazia
def p_empty(p):
    '''empty :'''
    p[0] = ''

# Regra de erro
def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno} perto de '{p.value}'")
    else:
        print("Erro de sintaxe no EOF")

# Construção do parser
parser = yacc.yacc(debug=False, write_tables=False)
