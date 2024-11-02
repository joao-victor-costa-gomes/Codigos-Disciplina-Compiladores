def imprimir(valor)
    puts "Inteiro: #{valor}"
end
  
def imprimir(valor, outro_valor)
    puts "Dois valores: #{valor}, #{outro_valor}"
end
  
imprimir(5)                # Erro: wrong number of arguments (given 1, expected 2)
imprimir(5, 10)            # Saída: Dois valores: 5, 10

