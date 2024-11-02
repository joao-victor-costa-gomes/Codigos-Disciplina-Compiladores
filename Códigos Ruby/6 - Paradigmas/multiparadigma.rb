# Conceito: Ruby suporta programação funcional, onde funções podem ser tratadas como objetos, passadas como argumentos ou retornadas por outras funções.
# As lambdas são uma forma de definir funções anônimas em Ruby.
soma = lambda { |a, b| a + b }  # Define uma função anônima (lambda) que recebe dois argumentos e retorna a soma deles.
puts soma.call(5, 10)  # Usa o método `call` para invocar a lambda com os argumentos 5 e 10, retornando 15.


# Conceito: Ruby suporta métodos de ordem superior como `map`, que aplicam uma função a cada elemento de uma coleção,
# retornando uma nova coleção com os resultados.
[1, 2, 3, 4].map { |x| x * 2 }  # Aplica a função { |x| x * 2 } a cada elemento da lista [1, 2, 3, 4], retornando [2, 4, 6, 8].


# Conceito: Metaprogramação é a capacidade de escrever código que gera ou modifica outro código em tempo de execução.
# Ruby permite isso com métodos como `define_method`, que permite criar métodos dinamicamente.
class Pessoa
    [:nome, :idade].each do |attr|
      define_method(attr) do  # Define um método dinamicamente para obter o valor de uma variável de instância.
        instance_variable_get("@#{attr}")  # Usa `instance_variable_get` para acessar o valor da variável de instância correspondente.
      end
  
      define_method("#{attr}=") do |val|  # Define um método dinamicamente para definir o valor de uma variável de instância.
        instance_variable_set("@#{attr}", val)  # Usa `instance_variable_set` para definir o valor da variável de instância correspondente.
      end
    end
  end
  
  p = Pessoa.new  # Cria um novo objeto da classe Pessoa.
  p.nome = "Maria"  # Usa o método dinamicamente definido para definir o valor da variável de instância `@nome`.
  puts p.nome  # Usa o método dinamicamente definido para acessar o valor de `@nome` e imprime "Maria".
  