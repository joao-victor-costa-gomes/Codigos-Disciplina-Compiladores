# if/elsif/else
idade = 20

if idade < 18
  puts "Menor de idade"
elsif idade >= 18 && idade < 60
  puts "Adulto"
else
  puts "Idoso"
end

# unless (executa o bloco se a condição for falsa)
nome = nil
unless nome
  puts "Nome não foi definido"
end

# case/when (semelhante ao switch)
dia = "segunda"

case dia
when "segunda"
  puts "Início da semana"
when "sexta"
  puts "Quase final de semana"
else
  puts "Outro dia da semana"
end
