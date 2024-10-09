# Criando uma Proc
minha_proc = Proc.new { |x| puts "Olá, #{x}!" }

# Chamando a Proc
minha_proc.call("Mundo")  # Saída: Olá, Mundo!


# Criando uma lambda
minha_lambda = ->(x) { puts "Olá, #{x}!" }

# Chamando a lambda
minha_lambda.call("Ruby")  # Saída: Olá, Ruby!


# Definindo um método
def saudacao(nome)
    puts "Olá, #{nome}!"
end
  
# Obtendo a referência ao método
minha_saudacao = method(:saudacao)
  
# Chamando o método através da referência
minha_saudacao.call("Carlos")  # Saída: Olá, Carlos!
  