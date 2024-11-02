# while loop
contador = 1
while contador <= 5
  puts "Contador: #{contador}"
  contador += 1
end

# until loop (executa enquanto a condição for falsa)
contador = 5
until contador == 0
  puts "Contagem regressiva: #{contador}"
  contador -= 1
end

# for loop (itera sobre um intervalo)
for i in 1..3
  puts "Iteração #{i}"
end

# each (iterador muito utilizado em Ruby)
[1, 2, 3].each do |numero|
  puts "Número: #{numero}"
end

# times (executa um bloco de código N vezes)
3.times do
  puts "Executando algo"
end
