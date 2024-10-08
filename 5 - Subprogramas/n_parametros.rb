def listar_nomes(*nomes)
    nomes.join(", ")
  end
  
  puts listar_nomes("João", "Maria", "Pedro")  # Saída: João, Maria, Pedro

