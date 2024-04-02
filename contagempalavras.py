frase = "Convite especial para toda a família! Junte-se a nós no Temperani e descubra a deliciosa Pizza de Páscoa criada por nosso Chef Antônio Maiolica!"
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
