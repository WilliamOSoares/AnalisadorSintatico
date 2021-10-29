#coding: utf-8
import os
import shutil

countArq = 1
countLinha = 1
estado = "Q0"
buffer = ""
linhaCoMF = 1
space = False #Caso pegue o espaço ou Tab 
skip = False #Usado para pular linha
endRead = False #Acaba a leitura de arquivos
pre = ["algoritmo","variaveis","constantes","registro","funcao","retorno","vazio","se","senao","enquanto","para","leia","escreva","inteiro","real","booleano","char","cadeia","verdadeiro","falso"]
erros = []
siglaErro = ["SIB","SII","CMF","NMF","CaMF","CoMF","OpMF","CmdMF"]
dados = []
tuplas = []
iterador = 0
linha = "01"

# Abertura do arquivo
def input():
    global countArq, endRead
    f=""
    try:
        f = open ("input/entrada%d.txt" %countArq, "r")        
    except: 
        endRead = True
        print("Arquivo nao encontrado!")        
    return f

# Escreve uma nova linha no arquivo de saída
def output(linha, code, buffer):
    global countArq, erros, siglaErro, dados, tuplas
    f = open("output/saida%d.txt" %countArq,"a")
    if(code == "ERRO"): 
        #f.write("\n")
        if erros:
            for x in erros:
                f.write(x)
                f.write("\n")
        else:
            f.write("SUCESSO!")
    else:
        if(linha<10):
            linhaSaida = "0" + str(linha) + " " + code +" " + buffer
            tuplas.append("0" + str(linha))
            tuplas.append(code)
            tuplas.append(buffer)
        else:
            linhaSaida = str(linha) + " " + code +" " + buffer
            tuplas.append(str(linha))
            tuplas.append(code)
            tuplas.append(buffer)
        flagER = False
        for x in siglaErro:
            if(x==code):
                flagER = True
        if(flagER):
            erros.append(linhaSaida)
            tuplas = []
        else:
            #f.write(linhaSaida)
            #f.write("\n")
            dados.append(tuplas)
            tuplas = []
    f.close()

# Verifica se é uma palavra reservada ou identificador
def PREouIDE(palavra, linha):
    global pre
    flagPRE = False
    for x in pre:
        if(x==palavra):
            flagPRE = True
    if(flagPRE):
        output(linha,"PRE",buffer)
    else:
        output(linha,"IDE",buffer)

########################################## Máquina de Estados Finitas #############################################################################################################################
def maqEstados(caractere,entrada, linha):
    global buffer, estado
    
    if(estado =="Q0"):
        estadoQ0(caractere, entrada, linha)
    elif(estado == "Q1"):
        estadoQ1(caractere, entrada, linha)
    elif(estado == "Q2"):
        estadoQ2(linha)
    elif(estado == "Q3"):
        estadoQ3(caractere, entrada, linha)
    elif(estado == "Q4"):
        estadoQ4(caractere, entrada, linha)
    elif(estado == "Q5"):
        estadoQ5(caractere, entrada, linha)
    elif(estado == "Q6"):
        estadoQ6(caractere, entrada, linha)
    elif(estado == "Q7"):
        estadoQ7(caractere, entrada, linha)
    elif(estado == "Q8"):
        estadoQ8(linha)
    elif(estado == "Q9"):
        estadoQ9(caractere, entrada, linha)
    elif(estado == "Q10"):
        estadoQ10(linha)
    elif(estado == "Q11"):
        estadoQ11(caractere, entrada, linha)
    elif(estado == "Q12"):
        estadoQ12(caractere, entrada, linha)
    elif(estado == "Q13"):
        estadoQ13(caractere, entrada, linha)
    elif(estado == "Q14"):
        estadoQ14(linha)
    elif(estado == "Q15"):
        estadoQ15(linha)
    elif(estado == "Q16"):
        estadoQ16(caractere, entrada, linha)
    elif(estado == "Q17"):
        estadoQ17(linha)
    elif(estado == "Q18"):
        estadoQ18(caractere, entrada, linha)
    elif(estado == "Q19"):
        estadoQ19(linha)   
    elif(estado == "Q20"):
        estadoQ20()   
    elif(estado == "Q21"):
        estadoQ21(caractere, entrada, linha)  
    elif(estado == "Q22"):
        estadoQ22(caractere, entrada)  
    elif(estado == "Q23"):
        estadoQ23(caractere, entrada)  
    elif(estado == "Q24"):
        estadoQ24() 
    elif(estado == "Q25"):
        estadoQ25(caractere, entrada, linha) 
    elif(estado == "Q26"):
        estadoQ26(linha) 
    elif(estado == "Q27"):
        estadoQ27(caractere, entrada, linha)   
    elif(estado == "Q28"):
        estadoQ28(caractere, entrada, linha)   
    elif(estado == "Q29"):
        estadoQ29(linha)   
    elif(estado == "Q30"):
        estadoQ30(caractere, entrada, linha)  
    elif(estado == "Q31"):
        estadoQ31(linha) 
    elif(estado == "Q32"):
        estadoQ32(caractere, entrada, linha)
    elif(estado == "Q33"):
        estadoQ33(caractere, entrada, linha)
    elif(estado == "Q34"):
        estadoQ34(caractere, entrada, linha)   
    elif(estado == "Q35"):
        estadoQ35(linha)   
    elif(estado == "Q36"):
        estadoQ36(caractere, entrada, linha)   
    elif(estado == "Q37"):
        estadoQ37(linha)   
    elif(estado == "Q38"):
        estadoQ38(caractere, entrada, linha) 
    elif(estado == "Q39"):
        estadoQ39(caractere, entrada, linha) 
    else:
        print("Bugou o estado")

############################################### Estados ########################################################################################################################################
'''O estado 0 é reponsavel por analisar o caractere e fazer a transição para o estado responsavel em
classifcar o caractere, verificando o decimal equivalenta na tabela ascii'''
def estadoQ0(caractere,entrada, linha):
    global buffer, estado, space
    buffer=buffer+entrada
    if(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122):
        estado = "Q1" 
    elif(caractere == 44 or caractere == 40 or caractere == 41 or caractere == 46 or caractere == 59 or caractere == 91 or caractere == 93 or caractere == 125):
        estado = "Q2"
    elif(caractere >= 48 and caractere <= 57):
        estado = "Q3"    
    elif(caractere == 124):
        estado = "Q7"
    elif(caractere == 38):
        estado = "Q9"
    elif (caractere >=60 and caractere <= 62 ):
        estado = "Q11"
    elif(caractere == 33):
        estado = "Q13"
    elif(caractere == 47):
        estado = "Q14"    
    elif(caractere == 42):
        estado = "Q15"
    elif(caractere == 45):
        estado = "Q16"
    elif(caractere == 43):
        estado = "Q18"    
    elif(caractere == 37):
        estado = "Q20" 
    elif(caractere == 123):
        estado = "Q21" 
    elif(caractere == 36 or caractere == 92 or caractere == 126 or caractere == 58 or caractere == 63 or caractere == 64 or caractere >=94 and caractere <= 96 or caractere == 35):
        estado = "Q25"
    elif(caractere == 34):
        estado = "Q27" 
    elif(caractere == 39):
        estado = "Q32"    
    else:
        if(not(caractere == 10 or caractere == 194 or caractere == 195 or caractere == 32 or caractere == 3 or caractere ==9 or caractere ==11)):
            estado = "Q26"
        else:
            buffer=""
            space = True

# Estado responsavel por classificar em identificador o caractere
def estadoQ1(caractere,entrada, linha):
    global buffer, estado
    if(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122 or caractere >=48 and caractere <= 57 or caractere ==95):
        buffer=buffer+entrada
        estado = "Q1"
    elif(caractere == 35 or caractere == 36 or caractere == 58 or caractere == 63 or caractere == 64 or caractere == 92 or caractere == 94 or caractere == 96 or caractere == 126 or caractere == 33 or caractere == 34 or caractere == 39):
        buffer=buffer+entrada
        estado = "Q38"
    else:
        estado = "Q0"
        PREouIDE(buffer, linha)
        buffer=""

# Estado responsavel por classificar em delimitador o caractere
def estadoQ2(linha):
    global buffer, estado
    estado = "Q0"
    output(linha, "DEL", buffer)
    buffer=""

# Do estadoQ3 ao estadoQ6 é responsavel por anlisar se é um numero, um numero flutuante ou 
# se há um erro de numero mal formado
def estadoQ3(caractere, entrada, linha):
    global buffer, estado
    if(caractere >= 48 and caractere <= 57):
        buffer = buffer + entrada
        estado = "Q3"
    elif(caractere == 46):
        buffer = buffer + entrada
        estado = "Q4"
    elif(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122 or caractere ==95 or caractere == 35 or caractere == 36 or caractere == 58 or caractere == 63 or caractere == 64 or caractere == 92 or caractere == 94 or caractere == 96 or caractere == 126):
        buffer = buffer + entrada
        estado = "Q6"
    else:
        estado = "Q0"
        output(linha, "NRO", buffer)
        buffer="" 

def estadoQ4(caractere, entrada, linha):
    global buffer, estado
    if(caractere >= 48 and caractere <= 57):
        buffer = buffer + entrada
        estado = "Q5"
    elif(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122 or caractere ==95 or caractere == 35 or caractere == 36 or caractere == 58 or caractere == 63 or caractere == 64 or caractere == 92 or caractere == 94 or caractere == 96 or caractere == 126 or caractere == 46):
        buffer = buffer + entrada
        estado = "Q6"
    else:
        output(linha, "NMF", buffer)
        estado = "Q0"
        buffer = ""

# Estado responsavel por classificar se é um numero flutante os caracteres ou se é um possivel numero mal formado 
def estadoQ5(caractere, entrada, linha):
    global buffer, estado
    if(caractere >= 48 and caractere <= 57):
        buffer = buffer + entrada
        estado = "Q5"
    elif(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122 or caractere ==95 or caractere == 35 or caractere == 36 or caractere == 58 or caractere == 63 or caractere == 64 or caractere == 92 or caractere == 94 or caractere == 96 or caractere == 126 or caractere == 46):
        buffer = buffer + entrada
        estado = "Q6"
    else:
        estado = "Q0"
        output(linha,"NRO",buffer)
        buffer = ""

# Estado que calssifica que é um numero mal formado os caracteres
def estadoQ6(caractere, entrada, linha):
    global buffer, estado
    if(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122 or caractere == 46 or caractere >= 48 and caractere <= 57):
        buffer = buffer + entrada
        estado = "Q6"
    else:
        estado = "Q0"
        output(linha,"NMF",buffer)
        buffer = ""

# Estado responsavel por analisar se o caractere é um possivel operador logico(||) ou um operador mal formado,
# caso volte para o estadoQ0 e classificado como operador mal formado
def estadoQ7(caractere,entrada, linha):
    global buffer, estado
    if(caractere == 124):
        buffer=buffer+entrada
        estado = "Q8"
    else:
        estado = "Q0"
        output(linha,"OpMF",buffer)
        buffer=""

# Estado que classifica o caractere em operador logico(&&)
def estadoQ8(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"LOG",buffer)
    buffer=""

# Estado responsavel por analisar se o caractere é um possivel operador logico(&&) ou um operador mal formado,
# caso volte para o estadoQ0 e classificado como operador mal formado
def estadoQ9(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 38):
        buffer = buffer+entrada
        estado = "Q10"
    else:
        estado = "Q0"
        output(linha,"OpMF",buffer)
        buffer=""

# Estado que classifica o caractere em operador logico(||)
def estadoQ10(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"LOG",buffer)
    buffer=""

# Estado que analisa se é um operador relacional do tipo > ou < ou = ou se é um possivel 
# operador relacional do tipo ==
def estadoQ11(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 61):
        buffer=buffer+entrada
        estado = "Q12"
    elif (caractere == 60 or caractere == 62):
        buffer=buffer+entrada
        estado = "Q39"
    else:
        estado = "Q0"
        output(linha,"REL",buffer)
        buffer=""

# Estado que classifica em operador relacional (==)
def estadoQ12(caractere, entrada, linha):
    global buffer, estado
    if (caractere >= 60 and caractere <= 62):
        buffer=buffer+entrada
        estado = "Q39"
    else:
        estado = "Q0"
        output(linha,"REL",buffer)
        buffer=""

# Estado que analisa se é um operador logico(!) ou um possivel operador relacional(!=)
def estadoQ13(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 61):
        buffer=buffer+entrada
        estado = "Q12"
    else:
        estado = "Q0"
        output(linha,"LOG",buffer)
        buffer=""

# Estado que classifica em operador artimetico (/)
def estadoQ14(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"ART",buffer)
    buffer=""

# Estado que classifica em operador artimetico (*)
def estadoQ15(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"ART",buffer)
    buffer=""

# Estado que anlisa se é um possivel operador artimetico do tipo -- ou de se é um operador aritimetico -
def estadoQ16(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 45):
        buffer=buffer+entrada
        estado = "Q17"
    else:
        estado = "Q0"
        output(linha,"ART",buffer)
        buffer=""

# Estado que classifica em operador artimetico (--)
def estadoQ17(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"ART",buffer)
    buffer=""

# Estado que anlisa se é um possivel operador artimetico do tipo ++ ou de se é um operador aritimetico +
def estadoQ18(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 43):
        buffer=buffer+entrada
        estado = "Q19"
    else:
        estado = "Q0"
        output(linha,"ART",buffer)
        buffer=""

# Estado que classifica em operador artimetico (++)
def estadoQ19(linha):
    global buffer, estado
    estado = "Q0"
    output(linha,"ART",buffer)
    buffer=""

# Estado que classifica como comentario de linha e ignora da linha e pula para proxima linha
def estadoQ20():
    global buffer, estado, skip
    estado = "Q0"
    buffer=""
    skip = True

# Estado que analisa se é um possivel comentario de bloco ou se é um delimitador ({).
# Do estado Q21 ao Q24 analisa o possivel comentario de bloco
def estadoQ21(caractere, entrada, linha):
    global buffer, estado, linhaCoMF
    if(caractere == 35):
        linhaCoMF = linha
        buffer=buffer+entrada
        estado = "Q22"
    else:
        estado = "Q0"
        output(linha,"DEL",buffer)
        buffer=""

def estadoQ22(caractere, entrada):
    global buffer, estado, linhaCoMF
    if(caractere == 3):
        estado = "Q0"
        output(linhaCoMF,"CoMF",buffer)
        buffer=""
    elif(caractere == 35):
        buffer=buffer+entrada
        estado = "Q23"
    else:
        if(caractere == 10):
            buffer=buffer+" "
            estado = "Q22"
        else:
            buffer=buffer+entrada
            estado = "Q22"

def estadoQ23(caractere, entrada):
    global buffer, estado, linhaCoMF
    if(caractere == 3):
        estado = "Q0"
        output(linhaCoMF,"CoMF",buffer)
        buffer=""
    elif(caractere == 35):
        buffer=buffer+entrada
        estado = "Q23"
    elif(caractere == 125):
        buffer=buffer+entrada
        estado = "Q24"
    else:
        if(caractere == 10):
            buffer=buffer+" "
            estado = "Q22"
        else:
            buffer=buffer+entrada
            estado = "Q22"

# Estado que classifica em comentario de bloco é ignora todos os caracteres que estão dentro desse comentario
# bem formado
def estadoQ24():
    global buffer, estado
    estado = "Q0"
    buffer=""

# Estado que classifica o caracter em simbolo ($ ou ` ou ~ ou ^ ou : ou ? ou @ ou _ ou \ ou #)
def estadoQ25(caractere, entrada, linha):
    global buffer, estado
    if(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122 or caractere >=48 and caractere <= 57 or caractere ==95 or caractere == 35 or caractere == 36 or caractere == 58 or caractere == 63 or caractere == 64 or caractere == 92 or caractere == 94 or caractere == 96 or caractere == 126 or caractere == 33 or caractere == 34 or caractere == 39):
        buffer=buffer+entrada
        estado = "Q38"
    else:
        estado = "Q0"
        output(linha,"SIB",buffer)
        buffer=""

# Estado que classifica em simbolos invalidos todos os caracteres que não pertencem ao intervalo
# de 32 a 126 da tabela ascii e que não seja final de linha, fim de arquivo, espaço, quebra de texto
# e tabulação
def estadoQ26(linha):
    global buffer, estado
    estado = "Q0"
    output(linha, "SII", buffer)
    buffer=""

# Do estadoQ27 ao estadoQ31 analisa a cadeia de caracteres
def estadoQ27(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 34):
        buffer=buffer+entrada
        estado = "Q29"
    elif(caractere == 92):
        buffer=buffer+entrada
        estado = "Q28"
    elif(caractere >=32 and caractere <= 126 and not(caractere == 39)):
        buffer=buffer+entrada
        estado = "Q27"
    elif(caractere == 10 or caractere == 3):
        estado = "Q0"
        output(linha,"CMF",buffer)
        buffer=""
    elif(caractere == 39):
        buffer=buffer+entrada
        estado = "Q30"
    else:
        buffer=buffer+entrada
        estado = "Q30"

def estadoQ28(caractere, entrada, linha):
    global buffer, estado
    if(caractere >=32 and caractere <= 126):
        buffer=buffer+entrada
        estado = "Q27"
    elif(caractere == 10 or caractere == 3):
        estado = "Q0"
        output(linha,"CMF",buffer)
        buffer=""
    elif(caractere == 39):
        buffer=buffer+entrada
        estado = "Q30"
    else:
        buffer=buffer+entrada
        estado = "Q30"

# Estado que classifica em cadeia de caractere
def estadoQ29(linha):
    global buffer, estado
    output(linha,"CAD",buffer)
    estado = "Q0"
    buffer=""

# Estado que classifica em cadeia mal formada caso não encontre o simbolo que finaliza a cadeia 
# e encontre simbolos invalidos ou apenas não encontre o simbolo que a finaliza
def estadoQ30(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 34):
        buffer=buffer+entrada
        estado = "Q31"
    elif(caractere == 10 or caractere == 3):
        estado = "Q0"
        output(linha,"CMF",buffer)
        buffer=""
    else:
        buffer=buffer+entrada
        estado = "Q30"

# Estado que classifica em cadeia mal formada caso encontre um simbolo invalido mesmo que encontre 
# simbolo que finaliza a cadeia de caracteres
def estadoQ31(linha):
    global buffer, estado
    output(linha,"CMF",buffer)
    estado = "Q0"
    buffer=""

# Do estadoQ32 ao estadoQ37 analisa se eh um caractere simples
def estadoQ32(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 92):
        buffer=buffer+entrada
        estado = "Q34"
    elif(caractere >=32 and caractere <= 126 and not(caractere == 39) and not(caractere == 34)):
        buffer=buffer+entrada
        estado = "Q33"
    elif(caractere == 10 or caractere == 3):
        estado = "Q0"
        output(linha,"CaMF",buffer)
        buffer=""
    else:
        buffer=buffer+entrada
        estado = "Q36"

def estadoQ33(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 39):
        buffer=buffer+entrada
        estado = "Q35"
    elif(caractere == 10 or caractere == 3):
        estado = "Q0"
        output(linha,"CaMF",buffer)
        buffer=""
    else:
        buffer=buffer+entrada
        estado = "Q36"

def estadoQ34(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 39 or caractere == 34 or caractere == 92):
        buffer=buffer+entrada
        estado = "Q33"
    elif(caractere == 10 or caractere == 3):
        estado = "Q0"
        output(linha,"CaMF",buffer)
        buffer=""
    else:
        buffer=buffer+entrada
        estado = "Q36"

# Estado que classifica em caractere simples
def estadoQ35(linha):
    global buffer, estado
    output(linha,"CAR",buffer)
    estado = "Q0"
    buffer=""

# Estado que classifica em caractere simples mal formado caso não ache o simbolo que finaliza ou
# encontre um simbolo invalido e tambem não encontre o simbolo que finaliza o caractere simples
def estadoQ36(caractere, entrada, linha):
    global buffer, estado
    if(caractere == 39):
        buffer=buffer+entrada
        estado = "Q37"
    elif(caractere == 10 or caractere == 3):
        estado = "Q0"
        output(linha,"CaMF",buffer)
        buffer=""
    else:
        buffer=buffer+entrada
        estado = "Q36"

# Estado que classifica em caractere simples mal formado caso encontre um simbolo invalido e
# encontre o simbolo que finaliza o caractere simples
def estadoQ37(linha):
    global buffer, estado
    output(linha,"CaMF",buffer)
    estado = "Q0"
    buffer=""

##################### NOVOS ESTADOS ATUALIZADOS NA ETAPA DA IMPLEMENTAÇÃO DA SINTATICA ###################

# Estado responsavel por classificar em identificador o caractere
def estadoQ38(caractere,entrada, linha):
    global buffer, estado
    if(caractere >=65 and caractere <= 90 or caractere >=97 and caractere <= 122 or caractere >=48 and caractere <= 57 or caractere ==95 or caractere == 35 or caractere == 36 or caractere == 58 or caractere == 63 or caractere == 64 or caractere == 92 or caractere == 94 or caractere == 96 or caractere == 126):
        buffer=buffer+entrada
        estado = "Q38"
    else:
        output(linha,"SIB",buffer)
        estado = "Q0"
        buffer=""
# Estado responsavel por classificar em identificador o caractere
def estadoQ39(caractere,entrada, linha):
    global buffer, estado
    if(caractere >=60 and caractere <= 62):
        buffer=buffer+entrada
        estado = "Q39"
    else:
        output(linha,"OpMF",buffer)
        estado = "Q0"
        buffer=""        

#############################################################################################################

def proxToken():
    global dados, tuplas, iterador
    if(iterador<len(dados)):
        tuplas = [dados[iterador][0], dados[iterador][1],dados[iterador][2]]
        iterador = iterador + 1
    else:
        tuplas = [0, "END", "$"]

def mantemToken():
    global dados, tuplas, iterador
    if(iterador<len(dados)):
        tuplas = [dados[iterador-1][0], dados[iterador-1][1],dados[iterador-1][2]]
    else:
        tuplas = [0, "END", "$"]

########################################### Analise Sintatica ###############################################

def START():
    global tuplas, buffer
    if(tuplas[2] == "algoritmo"):
        proxToken()
        i = ALGORITMO()
    else:
        output(int(tuplas[0]), "CmdMF", tuplas[2])
        mantemToken()


def ALGORITMO():
    global tuplas, buffer
    if(tuplas[2]=="{"):
        proxToken()
        i = CONTEUDO()
        return i
        

def CONTEUDO():
    global tuplas, iterador, dados, buffer, linha   ### COLOCAR O BUFFER GLOBAL PARA PERGAR DO INICIO DO ERRO ATÉ O FINAL "LEIA"
    errado = False
    retorno = 0
    while(iterador-1<len(dados)):
        if(tuplas[2] == "}"):
            i = 0
            if(errado):
                output(int(tuplas[0]), "CmdMF", buffer)
                mantemToken()
                buffer = ""
                i = 1
            buffer = buffer + " " + tuplas[2]
            proxToken()
            return i
        elif(tuplas[2] == "escreva"):
            if(errado):
                output(int(tuplas[0]), "CmdMF", buffer)
                mantemToken()
                buffer = ""
                errado = False
            buffer = buffer + " " + tuplas[2]
            linha = tuplas[0]
            proxToken()            
            i = ESCREVA()
            if(i == 1):
                output(int(tuplas[0]), "CmdMF", buffer)
                mantemToken()
            buffer = ""
        #usar if ao inveis de elif para tratar erros,caso volte a recursão e ocorra erro, 
        # deve sempre testar todas as condições
        elif(tuplas[2] == "leia"): 
            if(errado):
                output(int(tuplas[0]), "CmdMF", buffer)
                mantemToken()
                buffer = ""
                errado = False
            buffer = buffer + " " + tuplas[2]
            linha = tuplas[0]
            proxToken()            
            i = LEIA()
            if(i == 1):
                output(int(tuplas[0]), "CmdMF", buffer)
                mantemToken()
            buffer = ""
        elif(tuplas[2] == "constantes"):
            if(errado):
                output(int(tuplas[0]), "CmdMF", buffer)
                mantemToken()
                buffer = ""
                errado = False
            buffer = buffer + " " + tuplas[2]
            proxToken()            
            CONSTANTES()
            buffer = ""
        elif(tuplas[2] == "variaveis"):
            if(errado):
                output(int(tuplas[0]), "CmdMF", buffer)
                mantemToken()
                buffer = ""
                errado = False
            buffer = buffer + " " + tuplas[2]
            proxToken()            
            VARIAVEIS()
            buffer = ""
        else:
            errado = True
            buffer = buffer + " " + tuplas[2]
            proxToken()            
    if(iterador<10):
        aux = "0"+str(iterador)
        output(int(aux), "CmdMF", "Fim do arquivo / falta o '}'")
    else:    
        output(iterador, "CmdMF", "Fim do arquivo / falta o '}'")
    mantemToken()
    return retorno

########## Escreva ########

def ESCREVA():
    global tuplas, buffer, linha
    if(tuplas[2] == '(' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = ESCONT()
        if(i == 0):
            if(tuplas[2] == ';'and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                return 0
            else:
                return 1
        else:
            return i
    else:
        return 1

def ESCONT():
    global tuplas, buffer, linha
    if(tuplas[1] == "IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = ACESSOVAR()
        if(i == 0):
             i = ESFIM()
             return i
        else:
            return i
    if(tuplas[1] == "CAR" or tuplas[1] == "CAD" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = ESFIM()
        return i
    else:
        return 1

def ESFIM():
    global tuplas, buffer, linha
    if(tuplas[2] == ")" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return 0
    elif(tuplas[2] == "," and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = ESCONT()
        return i
    else:
        return 1    

######## Leia #########

def LEIA():
    global tuplas, buffer, linha
    if(tuplas[2] == '(' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = LEIACONT()
        if(i == 0):
            if(tuplas[2] == ';' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                return 0
            else:
                return 1
        else:
            return i
    else:
        return 1

def LEIACONT():
    global tuplas, buffer, linha
    if(tuplas[1] == "IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = ACESSOVAR()
        if(i == 0):
             i = LEIAFIM()
             return i
        else:
            return i
    else:
        return 1

def LEIAFIM():
    global tuplas, buffer, linha
    if(tuplas[2] == ")" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return 0
    elif(tuplas[2] == "," and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = LEIACONT()
        return i
    else:
        return 1

########### Acesso Var ##########

def ACESSOVAR():
    global tuplas, buffer, linha
    if(tuplas[2] == '.' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if(tuplas[1] == 'IDE' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()
            if(tuplas[2] == '[' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                if(tuplas[1] == 'NRO' and linha == tuplas[0]):
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
                    if(tuplas[2] == ']' and linha == tuplas[0]):
                        buffer = buffer + " " + tuplas[2]
                        proxToken()
                        i = ACESSOVARCONT()
                        return i
                    else:
                        return 1
                else:
                    return 1
            return 0
        else:
            return 1
    elif(tuplas[2] == '[' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if(tuplas[1] == 'NRO' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()
            if(tuplas[2] == ']' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                i = ACESSOVARCONT()
                return i
            else:
                return 1
        else:
            return 1
    return 0

def ACESSOVARCONT():
    global tuplas, buffer, linha
    if(tuplas[2] == '[' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if(tuplas[1] == 'NRO' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()
            if(tuplas[2] == ']' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                i = ACESSOVARCONTB()
                return i
            else:
                return 1
        else:
            return 1
    return 0

def ACESSOVARCONTB():
    global tuplas, buffer, linha
    if(tuplas[2] == '[' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if(tuplas[1] == 'NRO' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()
            if(tuplas[2] == ']' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                return 0
            else:
                return 1
        else:
            return 1
    return 0

########## Constantes e Variaveis##########

def CONSTANTES():
    global tuplas, buffer, linha, iterador
    if(tuplas[2]=="{"):
        buffer = buffer + " " + tuplas[2]
        proxToken()        
        print(tuplas)
        i = CONST()
        if(i == 1):            
            output(int(linha), "CmdMF", buffer)
            buffer = ""
            mantemToken()
            errado = False
            while(tuplas[2]!="$"):
                if(tuplas[2]=="}"):
                    if(errado):
                        output(int(linha), "CmdMF", buffer)
                        mantemToken()
                        buffer = ""
                    return 0
                elif(tuplas[2] == ";"):
                    if(errado):
                        output(int(linha), "CmdMF", buffer)
                        mantemToken()
                        buffer = ""
                    tuplas[2] = "{"
                    return CONSTANTES()
                elif(linha != tuplas[0]):
                    if(errado):
                        output(int(linha), "CmdMF", buffer)
                        mantemToken()
                        buffer = ""
                    print(tuplas)
                    iterador = iterador-1
                    tuplas[2] = "{"
                    print(tuplas)
                    return CONSTANTES()
                else:               
                    errado = True
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
        return i
    return 1

def CONST():
    global tuplas, buffer, linha
    buffer = ""
    linha = tuplas[0]
    i = TIPO()
    if(i==0):
        return CONSTALT()
    else:
        return i

def CONSTCONT(): 
    global tuplas, buffer
    if(tuplas[2]== "," and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return CONSTALT()
    elif(tuplas[2]== ";" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return CONSTFIM()
    else:
        return 1

def CONSTALT():
    global tuplas, buffer, linha
    if(tuplas[1]=="IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = VARINIT()
        if(i == 0):
            return CONSTCONT()
        else:
            return i
    else:
        return 1 

def CONSTFIM():
    global tuplas, buffer
    if(tuplas[2]=="}"):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return 0
    else:
        return CONST()

def VARIAVEIS():
    global tuplas, buffer
    if(tuplas[2]=="{"):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = VAR()
        if(i == 1):
            output(int(linha), "CmdMF", buffer)
            buffer = ""
            mantemToken()
        return i
    return 1

def VAR():
    global tuplas, buffer, linha
    buffer = ""
    linha = tuplas[0]
    i = TIPO()
    if(i==0):
        return VARALT()
    else:
        return i

def VARALT():
    global tuplas, buffer, linha
    if(tuplas[1]=="IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        i = VARCONT()
        return i
    else:
        return 1 

def VARCONT():
    global tuplas, buffer
    if(tuplas[2]== "," or tuplas[2]== ";"): #Conjunto first
        return VARFINAL()        
    else:
        i = VARINIT()
        if(i == 0):
            return VARFINAL()
        else:
            return i
        
def VARFINAL():
    global tuplas, buffer, linha
    if(tuplas[2]== "," and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return VARALT()
    elif(tuplas[2]== ";" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return VARFIM()
    else:
        return 1

def VARFIM():
    global tuplas, buffer
    if(tuplas[2]=="}"):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return 0
    else:
        return VAR()

def TIPO():
    global tuplas, buffer, linha
    if(tuplas[2]== "inteiro" or tuplas[2]=="real" or tuplas[2]=="booleano" or tuplas[2]=="cadeia" or tuplas[2]=="char" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return 0
    elif(tuplas[1]=="IDE" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return ACESSOVAR()
    else:    
        return 1

def VARINIT():
    global tuplas, buffer, linha
    if(tuplas[2] == '=' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return VALOR()
    elif(tuplas[2] == '[' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if(tuplas[1] == 'NRO' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()
            if(tuplas[2] == ']' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                i = VARINITCONT()
                return i
            else:
                return 1
        else:
            return 1
    return 0

def VARINITCONT():
    global tuplas, buffer, linha
    if(tuplas[2] == '=' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if(tuplas[2] == '{' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()
            return VETOR()
        else:
            return 1 
    elif(tuplas[2] == '[' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if(tuplas[1] == 'NRO' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()
            if(tuplas[2] == ']' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                i = VARINITCONTMATR()
                return i
            else:
                return 1
        else:
            return 1
    return 0

def VARINITCONTMATR():
    global tuplas, buffer, linha
    if(tuplas[2] == '=' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if(tuplas[2] == '{' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()
            i = VETOR()
            if(tuplas[2] == ',' and i ==0 and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                if(tuplas[2] == '{'):
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
                    return VETOR()
                else:
                    return 1 
            else:
                return 1 
        else:
            return 1 
    elif(tuplas[2] == '[' and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if(tuplas[1] == 'NRO' and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()
            if(tuplas[2] == ']' and linha == tuplas[0]):
                buffer = buffer + " " + tuplas[2]
                proxToken()
                if(tuplas[2] == '=' and linha == tuplas[0]):
                    buffer = buffer + " " + tuplas[2]
                    proxToken()
                    if(tuplas[2] == '{' and linha == tuplas[0]):
                        buffer = buffer + " " + tuplas[2]
                        proxToken()
                        i = VETOR()
                        if(tuplas[2] == ',' and i ==0 and linha == tuplas[0]):
                            buffer = buffer + " " + tuplas[2]
                            proxToken()
                            if(tuplas[2] == '{' and linha == tuplas[0]):
                                buffer = buffer + " " + tuplas[2]
                                proxToken()
                                i = VETOR()
                                if(tuplas[2] == ',' and i ==0 and linha == tuplas[0]):
                                    buffer = buffer + " " + tuplas[2]
                                    proxToken()
                                    if(tuplas[2] == '{' and linha == tuplas[0]):
                                        buffer = buffer + " " + tuplas[2]
                                        proxToken()
                                        return VETOR()
                                    else:
                                        return 1 
                                else:
                                    return 1 
                            else:
                                return 1 
                        else:
                            return 1 
                    else:
                        return 1 
                else:
                    return 1
            else:
                return 1
        else:
            return 1
    return 0
def VETOR():
    global tuplas, buffer
    i = VALOR()
    if(i == 0):
        return VETORCONT()
    return 1
def VETORCONT():
    global tuplas, buffer, linha
    if(tuplas[2]=="}" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return 0
    elif(tuplas[2]=="," and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return VETOR()
    else:
        return 1
    
def VALOR():
    global tuplas, buffer, linha
    if(tuplas[1]== "NRO" or tuplas[1]=="IDE" or tuplas[1]=="CAR" or tuplas[1]=="CAD" or tuplas[2]=="verdadeiro" or tuplas[2]=="falso" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        return 0
    elif(tuplas[2]== "-" and linha == tuplas[0]):
        buffer = buffer + " " + tuplas[2]
        proxToken()
        if(tuplas[1]== "NRO" and linha == tuplas[0]):
            buffer = buffer + " " + tuplas[2]
            proxToken()
            return 0
        return 1
    #proxToken()
    return 0

################################################# MAIN ####################################################
# Verifica se a existe a pasta input
flag = True
try:
    shutil.rmtree("output")
    os.mkdir("output")        
except:    
    print("Erro na manipulação da pasta output!")
pastas = os.listdir()
for x in pastas:
	if(x == "input"):
		flag = False
if(flag):
    print("Pasta input nao encontrada")
else:    
    while(not(endRead)):
        entrada = input()
        if(not(entrada=="")):
            flagSintax = True
            while 1:
                linha = entrada.readline()	
                i = 0
                if linha=='':
                    countLinha-=1
                    maqEstados(3, " ", countLinha)
                    break
                while i+1<=len(linha):
                    caractere = ord(linha[i])
                    maqEstados(caractere, linha[i], countLinha)
                    if(not(estado=="Q0") or space):
                        i+=1
                        space = False
                    if(skip):
                        skip = False
                        break
                countLinha+=1
            entrada.close()
        countLinha=1
        buffer=""
        if(flagSintax):
            proxToken()
            START()
            flagSintax = False
            output(0,"ERRO","")
            erros.clear()
        countArq+=1
        erros.clear()
        dados.clear()
        tuplas.clear()