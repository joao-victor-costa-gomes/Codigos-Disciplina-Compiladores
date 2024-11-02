catch :desvio_incondicional do
  puts "Antes do desvio"
  throw :desvio_incondicional  # Desvia o fluxo de controle para fora do bloco
  puts "Este código não será executado"
end
puts "Depois do desvio"
