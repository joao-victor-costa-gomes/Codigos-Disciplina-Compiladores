# SEM PARÂMETRO
def saudacao
  "Olá, mundo!"
end

puts saudacao  # Saída: Olá, mundo!

# COM PARÂMETRO
def saudacao_com_nome(nome)
  "Olá, #{nome}!"
end

puts saudacao_com_nome("Ana")  # Saída: Olá, Ana!

def soma(a, b)
  return a + b
end

puts soma(3, 5)  # Saída: 8