### String é o tipo de dado que representa uma seqüência de caracteres ###
### Usamos "aspas duplas" ou 'aspas simples' ou `crase` ###

empresa = 'Google'
print(empresa)
empresa = "Google"
print(empresa)
### empresa = 'Let's Code'
### print(empresa)
empresa = "Let's Code"
print(empresa)

### STRINGS PARTE 2 ###
### frase = "O professor Pietro da Let's Code disse: "Hoje a pizza é por minha conta!"
### Podemos usar um caracter de escape, ou seja, contra-barra ###
frase = "O professor Pietro da Let's Code disse: \"Hoje a pizza é por minha conta!\""
print(frase)

### SLICE pode ser usado nas STRs também... ###
empresa = 'Google'
print(empresa[0])
print(empresa[:3])

nomes_cidades = "São Paulo, Belo Horizonte, Rio de Janeiro, Brasília"
type(nomes_cidades) ### STR

### Método .split retorna a alteração feita na str, espaço é o default de separação ###
nomes_cidades = nomes_cidades.split(', ') ### vírgula espaço separam os elementos ###
print(nomes_cidades)
type(nomes_cidades) ### Retorna como uma LIST ###

### Método .strip é bom pra separar dados sujos com espaços antes e após os caracteres ###
cabecalho = "            MENU PRINCIPAL         "
print(cabecalho.strip()) ### "MENU PRINCIPAL"

nome_cidade = "rIo DE jaNeirO"

print(nome_cidade.title()) ### Rio De Janeiro
print(nome_cidade.capitalize()) ### Rio de janeiro
print(nome_cidade.lower()) ### rio de janeiro
print(nome_cidade.upper()) ### RIO DE JANEIRO

nome_cidade = input(('Que cidade do Brasil é conhecida como cidade maravilhosa? '))
nome_cidade = nome_cidade.strip()
while nome_cidade.lower() != 'rio de janeiro': ### Vai continuar no loop até acertarem a resposta! ###
    print('Tenta de novo, vai...')
    nome_cidade = input('Que cidade do Brasil é conhecida como cidade maravilhsoa? ')
print('Booa, campeão!')

mensagem = 'Você viu o que o Pietro disse na sala ontem?'
fui_citado = 'Pietro' in mensagem ### True/False verificando se houve uma menção ao texto em questão... ### 
print(fui_citado)


### Operadores aritméticos podem funcionar com STRs também! ###
cumprimento = 'Olá, '
nome = 'Felipe'
print(cumprimento + nome)

print(nome*5)
nome = 'Felipe'
idade = 35 ### Teremos de transformar INT para STR ###
n_filhos = 2 ### Teremos de transformar INT para STR ###
print(nome + str(idade) + str(n_filhos))

print(nome + ' tem ' + str(idade) + ' anos de idade e ' + str(n_filhos) + ' filhos.')
print('{} tem {} anos e {} filhos.'.format(nome, idade, n_filhos))
preco_gasolina = 3.476
print('O preço da gasolina hoje subiu e está em R$ {:.2f}'.format(preco_gasolina)) ### o índice .2f mostrando uma FLAG e usando 2 casas de FLOAT (casas decimais arredondando) ###


