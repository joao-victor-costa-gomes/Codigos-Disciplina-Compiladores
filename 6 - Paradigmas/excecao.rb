# Conceito: O tratamento de exceções permite capturar e lidar com erros inesperados no código,
# evitando que o programa falhe abruptamente. Ele também garante que certos blocos de código sejam sempre executados.
begin
    raise "Um erro!"  # O método `raise` lança uma exceção, simulando um erro no código.
  rescue => e  # O bloco `rescue` captura a exceção lançada e a armazena na variável `e`.
    puts "Ocorreu um erro: #{e.message}"  # Exibe a mensagem da exceção capturada.
  ensure
    puts "Este código sempre é executado"  # O bloco `ensure` é sempre executado, independentemente de um erro ter ocorrido.
  end
  