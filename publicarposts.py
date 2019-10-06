 # -*- coding: utf-8 -*-
#
# este é o arquivo principal para publicar nos blogs

import infoblogs
import postar
import random
import os.path
import time
import codecs
import artigos
import artigosSites



def estatisticas():

    total=0

    for idx in range(0,len(artigos.artigos)):
        arq = nomearq(idx)
        if os.path.isfile(arq):
            with open(arq,'r') as f:
                linhas = f.readlines()
                #print "Artigo ",idx,":",len(linhas)
                total=total+len(linhas)
    print "Total de artigos postados: ",total
                
import re
def nomearq(artigo):
    return 'postados\\'+re.sub('[^\w\s-]','',artigos.artigos[artigo][0])+".txt"
    

def japostou(artigo,blog):
  
    if not os.path.isfile(nomearq(artigo)):
        return False

    with open(nomearq(artigo), 'r') as f:
        for l in f.readlines(): # compara por numero e nome
            if (str(blog)==l.rstrip()) or (infoblogs.blogs[blog]==l.rstrip()):
                return True
        return False
    
def jaPostado(blog,artigo): # marca artigo como ja postado no blog
    try:
        with open(nomearq(artigo),"a") as f:
            f.write(infoblogs.blogs[blog]+"\n")
    except:
        print "erro ao acessar arquivo "+nomearq(artigo)
                    

def postarArtigo(blog,artigo):
    a = artigos.artigos[artigo]
    print "postando "+a[0]+" em "+infoblogs.blogs[blog]

    postar.novopost(blog,a[0],a[5],a[1],a[2],a[4],a[3])

    
    
def fazerposts(someus=False,meussempre=False,perc=0.9):
    meuspostados=0
    postados=0
    for blog in range(0,len(infoblogs.blogs)):
        time.sleep(3)
        if infoblogs.blogs[blog]=="":
            continue        
        tentativas = 1000
        print "(",
        while tentativas>=0:            
            if someus:
                artigo = artigos.meus[random.randint(0,len(artigos.meus)-1)]
            else:
                artigo = random.randint(0,len(artigos.artigos))       
                if artigo==0:
                    break
                    # print "não vai postar no blog ",blog    
                artigo=artigo-1
            if artigos.artigos[artigo][0]=="": # artigo removido
                artigo = 0
                break
            if japostou(artigo,blog) and not (meussempre and (artigo in artigos.meus)):
                #print "ja postou artigo",artigo," no blog ",blog
                tentativas=tentativas-1
                continue
            break
        
        if (artigo==0) or (tentativas==-1):
            continue
        if artigo in artigos.meus:
            meuspostados = meuspostados+1
        # print artigos.artigos[artigo][0][0:64] ,":"
        
           
        print "-",
        try:
            postarArtigo(blog,artigo)
            jaPostado(blog,artigo)
            postados=postados+1
        except:
            print "(erro ao postar)",
        print ".",
        # time.sleep(random.randint(1,3))
   
    print "\nfim posts."
    print "Artigos postados: ",postados
    print "Meus artigos: ",meuspostados
    

def tente5(funcao):
    print "Executando funcao ",funcao
    for i in range(0,5):
        try:
            return funcao()
        except:
            print "Erro executando funcao ",funcao
            continue
    return []

artsTemp = list(artigos.artigos)

def lerArtigossites():
    
    
    artigos.artigos = list(artsTemp)
    artigos.artigos.extend( tente5(artigosSites.artigosExame) )
    artigos.artigos.extend( tente5(artigosSites.artigosPcworld) )
    artigos.artigos.extend( tente5(artigosSites.artigosTecmundo) )
    artigos.artigos.extend( tente5(artigosSites.artigosComputerworld) )
    artigos.artigos.extend( tente5(artigosSites.artigosOficinadanet) )

            
estatisticas()

#try:

#except:
#    print "erro ao ler artigos."


print "Total artigos final: ",len(artigos.artigos)
print "Verificar ano/mes em imagem!"

for vezes in range(0,100):
    
    lerArtigossites()
    fazerposts(meussempre=True)
    time.sleep(8)
    
# fazerposts(someus=True)



