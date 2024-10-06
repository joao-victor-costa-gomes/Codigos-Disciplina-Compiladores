# Conceito: A orientação a objetos (OO) organiza o código em "objetos", que combinam dados (atributos) e comportamentos (métodos).
# Em Ruby, tudo é um objeto, e as classes definem as estruturas de dados e os comportamentos desses objetos.
class Pessoa
    def initialize(nome)  # O método `initialize` é o construtor da classe, chamado quando criamos uma nova instância de `Pessoa`.
      @nome = nome  # A variável de instância `@nome` armazena o nome da pessoa, e está disponível para todos os métodos da instância.
    end
  
    def diga_ola  # Método de instância que exibe uma saudação.
      puts "Olá, #{@nome}!"  # Usa a variável de instância `@nome` para criar uma mensagem personalizada.
    end
  end
  
  pessoa = Pessoa.new("João")  # Cria uma nova instância da classe `Pessoa`, passando "João" como argumento.
  pessoa.diga_ola  # Chama o método `diga_ola` da instância, que imprime "Olá, João!".
  