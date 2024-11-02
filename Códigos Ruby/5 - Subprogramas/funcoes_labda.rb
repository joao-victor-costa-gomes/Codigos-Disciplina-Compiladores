bom_dia = ->(param) { puts "Bom dia, #{param}!" }

bom_dia.call("João")  # Bom dia, João!

boa_noite = lambda { |param| puts "Boa noite, #{param}!" }

boa_noite.call("Maria")  # Boa noite, Maria!