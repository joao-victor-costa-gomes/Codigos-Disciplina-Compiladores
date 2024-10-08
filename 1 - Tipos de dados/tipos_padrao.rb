# Símbolo (é imutável e usado como identificador)
simbolo = :nome
puts simbolo  # Exibe :nome
puts simbolo.class  # Exibe "Symbol"

# Range (intervalo de números)
intervalo = (1..5)
puts intervalo.to_a  # Exibe [1, 2, 3, 4, 5]
puts intervalo.include?(3)  # Exibe true

# Hash (estrutura chave-valor)
hash_exemplo = { nome: "Alice", idade: 25, cidade: "São Paulo" }
puts hash_exemplo[:cidade]  # Exibe "São Paulo"
