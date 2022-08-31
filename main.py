# Lucas Kreutzer de Jesus

'''
Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a linguagem de programação que desejar, que seja capaz de validar expressões de lógica propisicional escritas em latex e definir se são expressões gramaticalmente corretas. Você validará apenas a forma da expressão (sintaxe).

A entrada será fornecida por um arquivo de textos que será carregado em linha de comando,
com a seguinte formatação:
1. Na primeira linha deste arquivo existe um número inteiro que informa quantas expressões lógicas estão no arquivo.
2. Cada uma das linhas seguintes contém uma expressão lógica que deve ser validada.
A saída do seu programa será no terminal padrão do sistema e constituirá de uma linha de saída para cada expressão lógica de entrada contendo ou a palavra valida ou a palavra inválida e nada mais.

Gramática:
Formula=Constante|Proposicao|FormulaUnaria|FormulaBinaria.
Constante="T"|"F".
Proposicao=[a−z0−9]+
FormulaUnaria=AbreParen OperadorUnario Formula FechaParen
FormulaBinaria=AbreParen OperatorBinario Formula Formula FechaParen
AbreParen="("
FechaParen=")"
OperatorUnario="¬"
OperatorBinario="∨"|"∧"|"→"|"↔"

Cada  expressão  lógica  avaliada  pode  ter  qualquer  combinação  das  operações  de  negação, conjunção, disjunção, implicação e bi-implicação sem limites na combiação de preposições e operações.
Os valores lógicos True e False estão representados na gramática e, como tal, podem ser usados em qualquer expressão de entrada.
'''

# Função responsável por checar se a quantidade de parênteses fechados é igual à quantidade de parênteses abertos.
def qtd_parenteses(expressao):
  qtdAberta = qtdFechada = 0
  for digito in expressao:
      if check_parenteses(digito) == 'A':
        qtdAberta += 1
      if check_parenteses(digito) == 'F':
        qtdFechada += 1
  return qtdAberta - qtdFechada


# Responsável por checar se um dígito específico é uma proposição (de acordo com a linguagem).
def check_proposicao(digito):
    if digito.isalpha() and digito.lower() == digito or digito.isnumeric():
        return True
    return False


# Responsável por checar se determinado dígito é uma constante.
def check_constante(expressao):
    if expressao == 'T' or expressao == 'F':
        return True
    return False


# Responsável por checar se o elemento compreende a alguma das variações de parênteses.
def check_parenteses(digito):
    if digito == ')':
        return 'F'
    elif digito == '(':
        return 'A'
    return ''


# Responsável por definir se há alguma barra na expressão passada.
def check_barra(expressao):
    for i in range(len(expressao)):
        if expressao[i] == '\\':
            return True
    return False


# Responsável por checar se um dígito específico é um espaço em branco.
def check_espaco(digito):
  if digito == ' ':
      return True
  return False


# Função responsável por realizar a checagem dos operadores lógicos, retornando seu tamanho e seu tipo.
def check_operador(expressao, i):
    tamanhoOperador = 0
    tipoOperador = "B"

    try:
        if expressao[i + 1] == 'v' and expressao[i + 2] == 'e' and expressao[i + 3] == 'e':
            tamanhoOperador = 3
        elif expressao[i + 1] == 'n' and expressao[i + 2] == 'e' and expressao[i + 3] == 'g':
            tamanhoOperador = 3
            tipoOperador = "U"
        if (expressao[i + 1] == 'w' and expressao[i + 2] == 'e' and expressao[i + 3] == 'd' and
                expressao[i + 4] == 'g' and expressao[i + 5] == 'e'):
            tamanhoOperador = 5
        if (expressao[i + 1] == 'r' and expressao[i + 2] == 'i' and expressao[i + 3] == 'g' and
                expressao[i + 4] == 'h' and expressao[i + 5] == 't' and expressao[i + 6] == 'a' and
                expressao[i + 7] == 'r' and expressao[i + 8] == 'r' and expressao[i + 9] == 'o' and
                expressao[i + 10] == 'w'):
            tamanhoOperador = 10
        if (expressao[i + 1] == 'l' and expressao[i + 2] == 'e' and expressao[i + 3] == 'f' and
                expressao[i + 4] == 't' and expressao[i + 5] == 'r' and expressao[i + 6] == 'i' and
                expressao[i + 7] == 'g' and expressao[i + 8] == 'h' and expressao[i + 9] == 't' and
                expressao[i + 10] == 'a' and expressao[i + 11] == 'r' and expressao[i + 12] == 'r' and
                expressao[i + 13] == 'o' and expressao[i + 14] == 'w'):
            tamanhoOperador = 14
    except:
        return 0, ""
    return tamanhoOperador, tipoOperador


# Função que irá checar se um caracter, ou uma sequência de caracteres, correspondem a uma fórmula válida.
# Para tal, essa função age de maneira recursiva, chamando a função principal para a nova fórmula definida.
def check_formula(expressao, i, tipoOperador):
    tamanhoFormula = -1
    expressaoAux = ""
    contadorAbertura = contadorFechamento = 0

    if tipoOperador == "U":
      if check_constante(expressao[i]):
          digito = expressao[i+1]
          if check_parenteses(digito) == 'F':    
            tamanhoFormula += 1
            return True, tamanhoFormula
          else:
            return False, -1
      
      for j in range(i, len(expressao)-1):
        if check_parenteses(expressao[i]) == 'A':
            if check_parenteses(expressao[j]) == 'A':
              contadorAbertura += 1
            elif check_parenteses(expressao[j]) == 'F':
              contadorFechamento += 1
              if contadorFechamento == contadorAbertura:
                break
        else:
            if check_parenteses(expressao[j]) == 'F' and not check_espaco(expressao[j+1]):
              break

        expressaoAux = expressaoAux + expressao[j]
        tamanhoFormula += 1

    elif tipoOperador == "B":
      for j in range(i, len(expressao)):
        if check_parenteses(expressao[i]) == 'A':
            if check_parenteses(expressao[j]) == 'A':
              contadorAbertura += 1
            elif check_parenteses(expressao[j]) == 'F':
              contadorFechamento += 1
              if contadorFechamento == contadorAbertura:
                break          
        else:
            if check_espaco(expressao[j]) or check_parenteses(expressao[j]) == 'F':
              break

        expressaoAux = expressaoAux + expressao[j]
        tamanhoFormula += 1


    if check_parenteses(expressao[i]) == 'A':
        expressaoFinal = expressaoAux + ")"
        tamanhoFormula += 1
    else:
        expressaoFinal = expressaoAux

    resultadoFormula = check_string(expressaoFinal)

    return resultadoFormula, tamanhoFormula


# Função principal, responsável por receber uma das palavras do arquivo desejado e efetuar a checagem de sua estrutura.
def check_string(expressao):
    resultado = True
    tipoOperador = ""
    secaoExpressao = 1

    if qtd_parenteses(expressao) != 0:
      return False
      
    if check_barra(expressao):
        i = 0
        while i < len(expressao):
            digito = expressao[i]
            if secaoExpressao == 1:
                if check_parenteses(digito) != 'A':
                    return False
                secaoExpressao += 1
              
            elif secaoExpressao == 2:
                tamanhoOperador, tipoOperador = check_operador(expressao, i)
                if tamanhoOperador == 0:
                    return False
                i = i + tamanhoOperador
                secaoExpressao += 1

            elif secaoExpressao == 3:
                if not check_espaco(digito):
                    return False
                secaoExpressao += 1             

            elif secaoExpressao == 4:
                resultadoFormula, tamanhoFormula = check_formula(expressao, i, tipoOperador)
                i += tamanhoFormula
              
                if resultadoFormula:
                  if tipoOperador == "B":
                      secaoExpressao += 1
                  elif tipoOperador == "U":
                      return True
                else:
                  return False

            elif secaoExpressao == 5:
                if check_espaco(digito):
                    secaoExpressao += 1
                else:
                    return False

            elif secaoExpressao == 6:
                resultadoFormula, tamanhoFormula = check_formula(expressao, i, tipoOperador)
                i += tamanhoFormula

                if not resultadoFormula:
                    return False
                return True

            i += 1
    else:
        for i in range(len(expressao)):
            retornoConstante = check_constante(expressao)
            retornoProposicao = check_proposicao(expressao[i])

            if not retornoConstante and not retornoProposicao:
                return False

    return resultado


# Variável que irá armazenar o nome do arquivo que será lido.
# Portanto, para realizar os testes, é necessário alterar o valor aqui.
arquivo = "expressoes1.txt"

# Importante notar que eu direcionei a abertura de arquivos dentro da pasta 'Arquivos'. Então, peço que mova qualquer arquivo novo desejado para a pasta indicada, ou altere o caminho no parâmetro abaixo.
# A estrutura 'with' efetua o fechamento automático do arquivo após seu uso.
with open("Arquivos/%s" % arquivo) as dados:
    nomes = dados.readlines()
    qtd_palavras = int(nomes[0])

    # Checando se o inteiro passado na primeira linha do arquivo bate com a quantidade de palavras existentes nas linhas seguintes.
    if len(nomes) == qtd_palavras + 1:
        contador = 1
        # Loop para checar cada palavra dentro do arquivo.
        while contador <= qtd_palavras:
            # Retirando o caracter adicional '\n' e chamando a função de checagem.
            palavra = nomes[contador].strip('\n')
            resposta = check_string(palavra)

            # Realizando o print do resultado de acordo com o retorno da função.
            if resposta:
                print("válida")
            else:
                print("inválida")
            contador += 1
    else:
        print("Quantidade de palavras não corresponde.")