import re

# Expressão regular geral unificada
expressao_regular = r"(0|[1-9][0-9]*|-?[1-9][0-9]*)" \
                  r"|((0|[1-9][0-9]*|-?[1-9][0-9]*)\s*:\s*(0|[1-9][0-9]*|-?[1-9][0-9]*))" \
                  r"|(\"[\w\s]+\"|'[\w\s]+')" \
                  r"|((\"[\w\s]+\"|'[\w\s]+')\s*:\s*(\"[\w\s]+\"|'[\w\s]+'))"

# Exemplos para teste
cadeias = [
    "0", "10", "-2", "-0",                                          
    "0:5", "2:2", "-1:-5", "0:-5", "-5:0", "-2:6", "6:-2",                    
    "'Date'", '"New Column"', "'Date"+'"', '"Date'+"'", "'New Column"+'"', '"New Column'+"'",                                     
    "'Data':'State'", '"District":"Tested"', "'simples'"+":"+'"duplas"', '"duplas"'+":"+"'simples'",                           
]

# Função para exibir resultados com mensagem personalizada
def testar_expressao(expressao, testes):
    padrao = re.compile(expressao)
    resultados = []
    for teste in testes:
        match = padrao.fullmatch(teste)
        if match:
            resultados.append(f"{teste} é reconhecida")
        else:
            resultados.append(f"{teste} NÃO é reconhecida")
    return resultados

# Executando o teste
resultados_teste = testar_expressao(expressao_regular, cadeias)
for resultado in resultados_teste:
    print(resultado)
