# PASSAGEM POR VALOR

def alterar_valor(a)
    a = a + 10
end
  
x = 5
alterar_valor(x)
puts x  # Saída: 5 (não foi alterado)
  

# PASSAGEM POR REFERÊNCIA
def alterar_lista(lista)
    lista << 10
end
  
minha_lista = [1, 2, 3]
alterar_lista(minha_lista)
puts minha_lista.inspect  
# Saída: [1, 2, 3, 10]


