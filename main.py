import string

# FUNÇÃO PRINCIPAL (TOP-LEVEL)
def main():
    dir_texto = "books/frankenstein.txt"
    texto = get_texto(dir_texto)
    print(f"-- Inicio do relatório, texto {dir_texto} --\n")
    print(f"{contador_palavras(texto)} palavras foram achadas no documento.\n")
    contagem_letras = contador_letras(texto)
    lista_contagem = [{'letra': chave, 'ocorrencias': valor} for chave, valor in contagem_letras.items()]
    lista_contagem.sort(reverse=True, key=lambda dict:dict["ocorrencias"])    
    print("Abaixo as ocorrencias de cada letra no texto, em ordem decrescente:\n")    
    for item in lista_contagem:
        print(f"A letra '{item["letra"]}' foi encontrada {item["ocorrencias"]} vezes.")
    print("\n-- Fim do relatório --")

    

# função que retorna todo o texto como uma string
def get_texto(path):
    with open(path) as f:
        return f.read()

# função que conta a quantidade de palavras do texto
def contador_palavras(texto):
    palavras = texto.split()    
    return len(palavras)

# função que conta a ocorrencia de cada letra dentro do texto
def contador_letras(texto):
    result = dict()
    texto_formatado = texto.replace(" ", "").lower()
    
    for caractere in texto_formatado:
        if caractere in string.ascii_lowercase:
            if caractere in result:
                result[caractere] += 1
            else:
                result[caractere] = 1
            
    return result

# execução da função principal
main()