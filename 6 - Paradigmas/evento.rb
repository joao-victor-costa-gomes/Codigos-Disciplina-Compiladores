# Conceito: O padrão de design "Observer" permite que um objeto (observável) notifique outros objetos (observadores)
# sobre mudanças em seu estado, facilitando a programação orientada a eventos.
require 'observer'  # Carrega o módulo 'observer', que implementa o padrão Observer em Ruby.

# Classe que atua como a fonte do evento (observável).
class EventSource
  include Observable  # O módulo `Observable` permite que a classe notifique seus observadores sobre mudanças.

  # Método que aciona um evento.
  def trigger_event
    changed  # Marca que houve uma mudança, preparando os observadores para serem notificados.
    notify_observers("Evento acionado")  # Notifica todos os observadores passando a mensagem "Evento acionado".
  end
end

# Observador 1, que reage ao evento de maneira específica.
class Observador1
  def update(message)  # O método `update` é chamado automaticamente quando o evento é acionado.
    puts "Observador 1 recebeu a mensagem: #{message}"  # Exibe a mensagem recebida.
  end
end

# Observador 2, que também reage ao evento de maneira diferente.
class Observador2
  def update(message)  # O método `update` é chamado automaticamente para este observador.
    puts "Observador 2 recebeu a mensagem: #{message}"  # Exibe a mensagem recebida.
  end
end

# Criação da fonte de eventos (observável).
event_source = EventSource.new

# Criação dos observadores.
obs1 = Observador1.new
obs2 = Observador2.new

# Adicionando os observadores à fonte de eventos.
event_source.add_observer(obs1)  # Observador 1 será notificado quando o evento ocorrer.
event_source.add_observer(obs2)  # Observador 2 também será notificado.

# Acionamento do evento. Ambos os observadores serão notificados e reagirão.
event_source.trigger_event
