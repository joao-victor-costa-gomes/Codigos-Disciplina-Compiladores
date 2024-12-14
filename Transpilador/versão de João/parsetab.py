
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND COMMENT DIVIDE EQUALS FALSE FLOAT IDENTIFIER LPAREN MINUS NUMBER OR PLUS RPAREN STRING TIMES TRUEstatements : statements statement\n                  | statementstatement : IDENTIFIER EQUALS expressionstatement : COMMENTexpression : expression PLUS term\n                  | expression MINUS term\n                  | expression AND term\n                  | expression OR termexpression : termterm : term TIMES factor\n            | term DIVIDE factorterm : factorfactor : NUMBER\n              | FLOAT\n              | STRING\n              | TRUE\n              | FALSEfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'IDENTIFIER':([0,1,2,4,5,7,8,9,10,11,12,13,14,23,24,25,26,27,28,29,],[3,3,-2,-4,-1,-3,-9,-12,-13,-14,-15,-16,-17,-5,-6,-7,-8,-10,-11,-18,]),'COMMENT':([0,1,2,4,5,7,8,9,10,11,12,13,14,23,24,25,26,27,28,29,],[4,4,-2,-4,-1,-3,-9,-12,-13,-14,-15,-16,-17,-5,-6,-7,-8,-10,-11,-18,]),'$end':([1,2,4,5,7,8,9,10,11,12,13,14,23,24,25,26,27,28,29,],[0,-2,-4,-1,-3,-9,-12,-13,-14,-15,-16,-17,-5,-6,-7,-8,-10,-11,-18,]),'EQUALS':([3,],[6,]),'NUMBER':([6,15,16,17,18,19,20,21,],[10,10,10,10,10,10,10,10,]),'FLOAT':([6,15,16,17,18,19,20,21,],[11,11,11,11,11,11,11,11,]),'STRING':([6,15,16,17,18,19,20,21,],[12,12,12,12,12,12,12,12,]),'TRUE':([6,15,16,17,18,19,20,21,],[13,13,13,13,13,13,13,13,]),'FALSE':([6,15,16,17,18,19,20,21,],[14,14,14,14,14,14,14,14,]),'LPAREN':([6,15,16,17,18,19,20,21,],[15,15,15,15,15,15,15,15,]),'PLUS':([7,8,9,10,11,12,13,14,22,23,24,25,26,27,28,29,],[16,-9,-12,-13,-14,-15,-16,-17,16,-5,-6,-7,-8,-10,-11,-18,]),'MINUS':([7,8,9,10,11,12,13,14,22,23,24,25,26,27,28,29,],[17,-9,-12,-13,-14,-15,-16,-17,17,-5,-6,-7,-8,-10,-11,-18,]),'AND':([7,8,9,10,11,12,13,14,22,23,24,25,26,27,28,29,],[18,-9,-12,-13,-14,-15,-16,-17,18,-5,-6,-7,-8,-10,-11,-18,]),'OR':([7,8,9,10,11,12,13,14,22,23,24,25,26,27,28,29,],[19,-9,-12,-13,-14,-15,-16,-17,19,-5,-6,-7,-8,-10,-11,-18,]),'RPAREN':([8,9,10,11,12,13,14,22,23,24,25,26,27,28,29,],[-9,-12,-13,-14,-15,-16,-17,29,-5,-6,-7,-8,-10,-11,-18,]),'TIMES':([8,9,10,11,12,13,14,23,24,25,26,27,28,29,],[20,-12,-13,-14,-15,-16,-17,20,20,20,20,-10,-11,-18,]),'DIVIDE':([8,9,10,11,12,13,14,23,24,25,26,27,28,29,],[21,-12,-13,-14,-15,-16,-17,21,21,21,21,-10,-11,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,],[1,]),'statement':([0,1,],[2,5,]),'expression':([6,15,],[7,22,]),'term':([6,15,16,17,18,19,],[8,8,23,24,25,26,]),'factor':([6,15,16,17,18,19,20,21,],[9,9,9,9,9,9,27,28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statements statement','statements',2,'p_statements','parser.py',6),
  ('statements -> statement','statements',1,'p_statements','parser.py',7),
  ('statement -> IDENTIFIER EQUALS expression','statement',3,'p_statement_assign','parser.py',15),
  ('statement -> COMMENT','statement',1,'p_statement_comment','parser.py',20),
  ('expression -> expression PLUS term','expression',3,'p_expression_binop','parser.py',25),
  ('expression -> expression MINUS term','expression',3,'p_expression_binop','parser.py',26),
  ('expression -> expression AND term','expression',3,'p_expression_binop','parser.py',27),
  ('expression -> expression OR term','expression',3,'p_expression_binop','parser.py',28),
  ('expression -> term','expression',1,'p_expression_term','parser.py',39),
  ('term -> term TIMES factor','term',3,'p_term_binop','parser.py',43),
  ('term -> term DIVIDE factor','term',3,'p_term_binop','parser.py',44),
  ('term -> factor','term',1,'p_term_factor','parser.py',51),
  ('factor -> NUMBER','factor',1,'p_factor_number','parser.py',55),
  ('factor -> FLOAT','factor',1,'p_factor_number','parser.py',56),
  ('factor -> STRING','factor',1,'p_factor_number','parser.py',57),
  ('factor -> TRUE','factor',1,'p_factor_number','parser.py',58),
  ('factor -> FALSE','factor',1,'p_factor_number','parser.py',59),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','parser.py',64),
]
