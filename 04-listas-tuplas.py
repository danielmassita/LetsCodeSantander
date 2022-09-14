nomes_paises = ['Brasil', 'Argentina', 'China', 'Canadá', 'Japão']
print(nomes_paises)

print('Tamanho da lista:', len(nomes_paises)) """len(x) retorna o tamanho dos elementos da lista com base 0"""

print('País:', nomes_paises[4]) """Japão no último dado"""
print('País:', nomes_paises[-1]) """Japão também no último dado, contando regressivamente"""
nomes_paises[4] = 'Colômbia' """Troca de Japão por Colômbia"""
print('País:', nomes_paises[4]) 
print(nomes_paises)

nomes_paises[5] = 'Chile' """Não permite adicionar um dado se não tiver o espaço existente na lista..."

