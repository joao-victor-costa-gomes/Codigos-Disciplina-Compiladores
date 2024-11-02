# Vetor homogêneo de inteiros
vetor_homogeneo = [1, 2, 3, 4]
puts vetor_homogeneo  # Exibe [1, 2, 3, 4]
puts vetor_homogeneo.class  # Exibe "Array"

# Matriz (array de arrays) homogênea
matriz_homogenea = [[1, 2], [3, 4]]
puts matriz_homogenea.inspect  # Exibe [[1, 2], [3, 4]]
puts matriz_homogenea[0][1]  # Exibe 2 (elemento na posição 0,1)

# Vetor heterogêneo (com diferentes tipos)
vetor_heterogeneo = [1, "Ruby", true]
puts vetor_heterogeneo.inspect  # Exibe [1, "Ruby", true]

# Hash (funcionando como um registro)
registro = { nome: "João", idade: 30, profissao: "Desenvolvedor" }
puts registro  # Exibe {:nome=>"João", :idade=>30, :profissao=>"Desenvolvedor"}
puts registro[:nome]  # Exibe "João"
puts registro[:idade]  # Exibe 30
