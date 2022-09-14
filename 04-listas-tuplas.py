### LIST ###

nomes_paises = ['Brasil', 'Argentina', 'China', 'Canadá', 'Japão']
print(nomes_paises)

print('Tamanho da lista:', len(nomes_paises)) """len(x) retorna o tamanho dos elementos da lista com base 0"""

print('País:', nomes_paises[4]) """Japão no último dado"""
print('País:', nomes_paises[-1]) """Japão também no último dado, contando regressivamente"""
nomes_paises[4] = 'Colômbia' """Troca de Japão por Colômbia"""
print('País:', nomes_paises[4]) 
print(nomes_paises)

nomes_paises[5] = 'Chile' """Não permite adicionar um dado se não tiver o espaço existente na lista..."""

print(nomes_paises[1:3]) ### Do índice 1 ao 3 não inclusivo ###
print(nomes_paises[1:-1]) ### Do índice 1 ao último não inclusivo ###
print(nomes_paises[2:]) ### Da posição índice 2 até o final ###
print(nomes_paises[:3]) ### Do inicial ao valor final 3 não inclusivo ###
print(nomes_paises[:]) ### Do inicial ao final não especificando ###
print(nomes_paises[::2]) ### Do inicial ao final, pulando de 2 em 2 (step) ###
print(nomes_paises[::-1]) ### Lista com incremento negativo (inverso da ordem lista) ###
print("Brasil" in nomes_paises) ### Resultado Bool True/False ###
print("Canadá" not in nomes_paises) ### Resultado Bool sendo != ###

### Métodos que podemos usar nas listas! ###

lista_capitais =[]
lista_capitais.append('Brasilia')
lista_capitais.append('Buenos Aires')
lista_capitais.append('Pequim')
lista_capitais.append('Bogotá')
print(lista_capitais)
lista_capitais.insert(2, 'Paris') ### Adiciona no índice 2 o dado Paris ###
print(lista_capitais)
lista_capitais.remove('Buenos Aires') ### Remove o dado especificado da lista ###
print(lista_capitais)

removido = lista_capitais.pop(2) ### A função .pop ela retira e retorna um dado, então podemos atribuir uma var ###
print(lista_capitais)
print(removido)

### TUPLA - Listas são flexíveis, Tuplas não são permitidas alterações, porém tem operações especiais e possui armazenamento menor ###

nomes_paises = ('Brasil', 'Argentina', 'China', 'Canadá', 'Japão')
print(nomes_paises)
type(nomes_paises)

nomes_paises = 'Brasil', 'Argentina', 'China', 'Canadá', 'Japão'
print(nomes_paises)
type(nomes_paises)

nome_estado = 'São Paulo', ### a vírgula entende tupla de 1 elemento ###
print(nome_estado, type(nome_estado))

len(nomes_paises)
nomes_paises[0]

### As tuplas possuem operação de UNPACKING! Transformando cada elemento em uma nova variável ###
### Usando apenas as iniciais dos nomes como variáveis, podemos ter... ###

b, a, c, ca, j = nomes_paises
print(b, c, j)
print(*nomes_paises) ### Imprime apenas as variáveis UNPACKED e não a lsita de dados ###
