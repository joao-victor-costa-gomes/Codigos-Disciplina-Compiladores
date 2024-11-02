# Índices de números inteiros
(0|-?[1-9][0-9]*)

# Índices de intervalos de números inteiros
(((0|[1-9][0-9]*):(0|[1-9][0-9]*))|((-[1-9][0-9]*):(-[1-9][0-9]*)))

# Índices de nomes
(\"[\w\s]+\"|'[\w\s]+')

# Índices de intervalos de nomes
((\"[\w\s]+\"|'[\w\s]+'):(\"[\w\s]+\"|'[\w\s]+'))

# Expressão final (União de todas as expressões)
(0|-?[1-9][0-9]*)|(((0|[1-9][0-9]*):(0|[1-9][0-9]*))|((-[1-9][0-9]*):(-[1-9][0-9]*)))|(\"[\w\s]+\"|'[\w\s]+')|((\"[\w\s]+\"|'[\w\s]+'):(\"[\w\s]+\"|'[\w\s]+'))