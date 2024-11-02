# Conceito: Vamos simular a execução de três tarefas que podem ocorrer ao mesmo tempo, usando threads.
# Cada thread vai executar uma tarefa diferente, e todas vão rodar "ao mesmo tempo", sem esperar uma pela outra.

# Função para simular uma tarefa que leva tempo para ser concluída
def tarefa(nome, tempo)
    puts "Iniciando tarefa: #{nome}"  # Indica que a tarefa começou.
    sleep(tempo)  # Simula uma tarefa demorada, "dormindo" por alguns segundos.
    puts "Tarefa #{nome} concluída!"  # Exibe quando a tarefa termina.
  end
  
  # Conceito: Vamos criar várias threads, cada uma rodando uma tarefa diferente.
  # Isso significa que as tarefas vão ser executadas de forma concorrente (ao mesmo tempo).
  
  threads = []  # Array para armazenar as threads.
  
  # Criando três threads, cada uma rodando uma tarefa com tempos diferentes.
  threads << Thread.new { tarefa("Tarefa 1", 2) }  # Tarefa 1 demora 2 segundos.
  threads << Thread.new { tarefa("Tarefa 2", 3) }  # Tarefa 2 demora 3 segundos.
  threads << Thread.new { tarefa("Tarefa 3", 1) }  # Tarefa 3 demora 1 segundo.
  
  # Conceito: O método `join` faz com que o programa principal espere que todas as threads terminem.
  threads.each(&:join)  # Aguarda a conclusão de todas as threads.
  
  puts "Todas as tarefas foram concluídas!"  # Mensagem final quando todas as threads terminarem.
  


# Conceito: Fibers são unidades leves de execução que permitem a suspensão e retomada de tarefas,
# útil para controlar manualmente a sequência de execução de um bloco de código sem a sobrecarga das threads.
fiber = Fiber.new do
    puts "Dentro do fiber"  # Executa este código na primeira vez que o Fiber é iniciado.
    Fiber.yield  # Suspende o fiber, retornando o controle ao ponto de chamada.
    puts "Voltando ao fiber"  # Executa esta parte quando o fiber é retomado.
  end
  fiber.resume  # Inicia a execução do fiber e imprime "Dentro do fiber".
  fiber.resume  # Retoma o fiber de onde foi suspenso e imprime "Voltando ao fiber".
  
  