# -*- coding: utf-8 -*-

#le artigos de Sites automaticamente
# VER TIPO DE CODIFICACAO DE CARS DA PAGINA SE NAO FOR UNICODE PRECISA CONVERTER!

import urllib2
import time

def artigosExame():
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    caminho = 'c:\\users\\egon\\downloads\\imagens blog\\'
    nImg = 1
    print "Lendo artigos de exame.com.br"
    l = []
    pagina = urllib2.urlopen("http://exame.abril.com.br/tecnologia/")
    lista = pagina.read()
    
    ps = lista.find('<li id="post-')
    if ps == -1:
        print "nao encontrou passo 1"
        return []
    
    while ps>-1:
        time.sleep(1)
        artigo = [0,1,2,3,4,5]

        psLink = lista.find('href="',ps)+6
        fimLink = lista.find('"',psLink)
        artigo[1] = lista[psLink:fimLink]
        #print artigo[1]

        psTitulo = lista.find('"',fimLink+1)+1
        fimTitulo = lista.find('"',psTitulo)
        artigo[0] = lista[psTitulo:fimTitulo]
        #print "artigo:",artigo[0]

        psImagem = lista.find('src="',fimTitulo)+5
        fimImagem = lista.find('"',psImagem)
        urlImg = lista[psImagem:fimImagem]
        nomeImg = "exame"+str(nImg)+".jpg"
        artigo[2] = nomeImg
        #print artigo[2]
        
        # salva arquivo img
        try:
            imgRequest = urllib2.Request(urlImg, headers=headers)
            imgData = urllib2.urlopen(imgRequest).read()    
            output = open(caminho + nomeImg,'wb')
            output.write(imgData)
            output.close()
            nImg = nImg + 1
        except:
            print "(erro ler foto)",
            artigo[2] = ""
        #       
        
        
        artigo[3] = ["Tecnologia"]
        artigo[4] = ["Tecnologia"]

        #ler um paragrafo do artigo
        
        try:
            pagina = urllib2.urlopen(artigo[1])        
            textoArtigo = pagina.read()
        except:
            print "(erro ler artigo)",
            textoArtigo = ""
            
        inicio = '</html>'
        psInicio = textoArtigo.find(inicio)
        if (psInicio==-1):
            print artigo[1],"pode ter problema! "        
        else:
            psInicio = textoArtigo.find("<p>",psInicio)+3
            psFim = textoArtigo.find("</p>",psInicio)
            if (psInicio==-1 ) or (psFim==-1):
                print artigo[1],"pode ter problema! "        
            else:
                textoChamada = textoArtigo[psInicio:psFim]
                psInicio = textoArtigo.find("<p>",psInicio)+3
                psFim = textoArtigo.find("</p>",psInicio)
                if (psInicio==-1 ) or (psFim==-1):
                    print artigo[1],"pode ter problema! "        
                else:
                    primeiroParagrafo = textoArtigo[psInicio:psFim]
                    artigo[5] = semTags(textoChamada)+"<p>"+semTags(primeiroParagrafo)
                    l.append(artigo)

        ps = lista.find('<li id="post-',ps+1)
        print " .",
            
    print "lidos."
    print "Total exame: ",len(l)
    return l
 
def artigosPcworld():
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    caminho = 'c:\\users\\egon\\downloads\\imagens blog\\'
    nImg = 1
    print "Lendo artigos de pcworld.com.br"
    l = []
    pagina = urllib2.urlopen("http://pcworld.com.br/noticias")
    lista = pagina.read()
    
    ps = lista.find('<ul class="listagem-dicas"')
    if ps == -1:
        print "nao encontrou passo 1"
        return []

    
    ps = lista.find('<a href="http://pcworld.com.br/noticias',ps)
    while ps>-1:
        time.sleep(1)
        artigo = [0,1,2,3,4,5]

        psLink = lista.find('"',ps)+1
        fimLink = lista.find('"',psLink)
        artigo[1] = lista[psLink:fimLink]
        #print artigo[1]

        psTitulo = lista.find('"',fimLink+1)+1
        fimTitulo = lista.find('"',psTitulo)
        artigo[0] = lista[psTitulo:fimTitulo]
        #print "artigo:",artigo[0]

        psImagem = lista.find('src="',fimTitulo)+5
        fimImagem = lista.find('"',psImagem)
        urlImg = lista[psImagem:fimImagem]
        nomeImg = "pcworld"+str(nImg)+".jpg"
        artigo[2] = nomeImg
        #print artigo[2]
        
        # salva arquivo img
        try:
            imgRequest = urllib2.Request(urlImg, headers=headers)
            imgData = urllib2.urlopen(imgRequest).read()    
            output = open(caminho + nomeImg,'wb')
            output.write(imgData)
            output.close()
            nImg = nImg + 1
        except:
            print "(erro ler foto)",
            artigo[2] = ""
        #        
        psChamada = lista.find('<p>',fimImagem)+3
        fimChamada = lista.find('</p>',psChamada)
        textoChamada = lista[psChamada:fimChamada]
        #print textoChamada
        
        artigo[3] = ["Tecnologia da Informação"]
        artigo[4] = ["Tecnologia da Informação"]

        #ler um paragrafo do artigo
        print " .",
        try:
            pagina = urllib2.urlopen(artigo[1])        
            textoArtigo = pagina.read()
        except:
            print "(erro ler artigo)",
            textoArtigo = ""

        inicio = '<p class="p1">'
        psInicio = textoArtigo.find(inicio)
        if psInicio == -1: # deve ser <div> no lugar de p
            inicio = "<div>"
            psInicio = textoArtigo.find(inicio)
            fim = "</div>"
        else:
            fim = "</p>"
        psFim = textoArtigo.find(fim,psInicio)
        if (psInicio==-1) or (psFim==-1):
            print artigo[1],"pode ter problema! "        
        else:
            psInicio = psInicio+len(inicio)
            primeiroParagrafo = textoArtigo[psInicio:psFim]
            artigo[5] = textoChamada+"<p>"+primeiroParagrafo
            l.append(artigo)

        ps = lista.find('<a href="http://pcworld.com.br/noticias',fimChamada)

            
    print "lidos."
    print "Total pcworld: ",len(l)
    return l





def artigosTecmundo():
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    caminho = 'c:\\users\\egon\\downloads\\imagens blog\\'
    nImg = 1
    print "Lendo artigos de tecmundo.com.br"
    l = []
    pagina = urllib2.urlopen("https://www.tecmundo.com.br/novidades")
    lista = pagina.read()
    ps = lista.find('</script><script id="json-script">')
    if ps == -1:
        print "nao encontrou passo 1"
        return []

    
    ps = lista.find(',"DateISO":',ps)
    ps = lista.find(',"Title":',ps)    
    while ps>-1:
        time.sleep(1)
        artigo = [0,1,2,3,4,5]
        psTitulo = lista.find(':"',ps)+2
        fimTitulo = lista.find('"',psTitulo)
        artigo[0] = lista[psTitulo:fimTitulo]
        
        psChamada = lista.find(':"',fimTitulo)+2
        fimChamada = lista.find('"',psChamada)
        textoChamada = lista[psChamada:fimChamada]

        psImagem = lista.find(':"',fimChamada)+2
        fimImagem = lista.find('"',psImagem)
        urlImg = lista[psImagem:fimImagem]
        nomeImg = "tecmundo"+str(nImg)+".jpg"
        artigo[2] = nomeImg
        # salva arquivo img
        try:
            imgRequest = urllib2.Request(urlImg, headers=headers)
            imgData = urllib2.urlopen(imgRequest).read()    
            output = open(caminho + nomeImg,'wb')
            output.write(imgData)
            output.close()
            nImg = nImg + 1
        except:
            print "(erro ler foto)",
            artigo[2] = ""
        #       
        
        psLink = lista.find(':"',fimImagem)+2
        fimLink = lista.find('"',psLink)
        artigo[1] = "https://www.tecmundo.com.br"+lista[psLink:fimLink]

        artigo[3] = ["Tecnologia da Informação"]
        artigo[4] = ["Tecnologia da Informação"]

        #ler um paragrafo do artigo
        print " .",
        try:
            pagina = urllib2.urlopen(artigo[1])        
            textoArtigo = pagina.read()
        except:
            print "(erro ler artigo)",
            textoArtigo = ""

        inicio = '<div class="article-text highlight p402_premium" itemprop="articleBody"><p>'
        psInicio = textoArtigo.find(inicio)    
        fim = "</p>"
        psFim = textoArtigo.find(fim,psInicio)
        if (psInicio==-1) or (psFim==-1):
            print artigo[1],"pode ter problema! "        
        else:
            psInicio = psInicio+len(inicio)
            primeiroParagrafo = textoArtigo[psInicio:psFim]
            artigo[5] = textoChamada+"<p>"+primeiroParagrafo
            l.append(artigo)

        
        ps = lista.find(',"DateISO":',ps)
        ps = lista.find(',"Title":',ps)
        
    print "lidos."
    print "Total tecmundo: ",len(l)
    return l


def artigosComputerworld():
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    caminho = 'c:\\users\\egon\\downloads\\imagens blog\\'
    nImg = 1
    print "Lendo artigos de Computerword.com.br"
    l = []
    pagina = urllib2.urlopen("http://computerworld.com.br/ultimas-noticias")
    lista = pagina.read()
    ps = lista.find("itemNoticia")
    while ps>-1:
        time.sleep(1)
        artigo = [0,1,2,3,4,5]
        psLink = lista.find("<a href",ps)
        fimLink = lista.find('">',psLink)
        artigo[1] = "http://computerworld.com.br"+ lista[psLink+9:fimLink]
        psImg = lista.find('src="',fimLink)+5
        fimImg = lista.find('"',psImg)
        urlImg = lista[psImg:fimImg]
        nomeImg = "computerworld"+str(nImg)+".jpg"
        artigo[2] = nomeImg
        # salva arquivo img
        try:
            imgRequest = urllib2.Request(urlImg, headers=headers)
            imgData = urllib2.urlopen(imgRequest).read()    
            output = open(caminho + nomeImg,'wb')
            output.write(imgData)
            output.close()
            nImg = nImg + 1
        except:
            print "(erro ler foto)",
            artigo[2] = ""
        #       
        psLink = lista.find("<a href",fimImg)
        psTitulo = lista.find('">',psLink)+2
        fimTitulo = lista.find("</a",psTitulo)
        artigo[0] = lista[psTitulo:fimTitulo]
        artigo[3] = ["Tecnologia da Informação"]
        artigo[4] = ["Tecnologia da Informação"]
        psCorpo = lista.find("<p",fimTitulo)+3
        fimCorpo = lista.find("</p",psCorpo)
        textoChamada = lista[psCorpo:fimCorpo]
        #ler um paragrafo do artigo
        print " .",
        try:
            pagina = urllib2.urlopen(artigo[1])        
            textoArtigo = pagina.read()
        except:
            print "(erro ler artigo)",
            textoArtigo = ""

        inicio = '<section class="corpoMateria"><p>'
        psInicio = textoArtigo.find(inicio)    
        fim = "</p>"
        psFim = textoArtigo.find(fim,psInicio)
        if (psInicio==-1) or (psFim==-1):
            print artigo[1],"pode ter problema! "
        else:
            psInicio = psInicio+len(inicio)
            primeiroParagrafo = textoArtigo[ psInicio:psFim]
            artigo[5] = "<h2>"+textoChamada+"</h2>"+primeiroParagrafo
            l.append(artigo)

        ps = lista.find("itemNoticia",fimCorpo)
        
    print "lidos."
    print "Total computerworld: ",len(l)
    return l
                
def artigosOficinadanet():
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    caminho = 'c:\\users\\egon\\downloads\\imagens blog\\'
    nImg = 1
    print "Lendo artigos de Oficinadanet"
    l = []
    pagina = urllib2.urlopen("https://www.oficinadanet.com.br/artigos/tecnologia")
    lista = pagina.read()
    lista = lista.decode('iso-8859-1').encode('utf8')
 
    ps = lista.find('<li class="wifl">')
    while ps>-1:
        time.sleep(1)
        artigo = [0,1,2,3,4,5]
        psLink = lista.find("<a href",ps)
        fimLink = lista.find('"',psLink+9)
        artigo[1] = lista[psLink+9:fimLink]
        
        psImg = lista.find('src="',fimLink)+5
        fimImg = lista.find('"',psImg)
        urlImg = lista[psImg:fimImg]
        nomeImg = "oficinadanet"+str(nImg)+".jpg"
        artigo[2] = nomeImg
        # salva arquivo img
        try:
            imgRequest = urllib2.Request(urlImg, headers=headers)
            imgData = urllib2.urlopen(imgRequest).read()    
            output = open(caminho + nomeImg,'wb')
            output.write(imgData)
            output.close()
            nImg = nImg + 1
        except:
            print "(erro ler foto)",
            artigo[2] = ""
        #       
        psTitulo = lista.find('alt="',psImg)+5
        fimTitulo = lista.find('"',psTitulo)
        artigo[0] = lista[psTitulo:fimTitulo]

        psTag = lista.find("<a href",fimTitulo)
        psTag = lista.find(">",psTag)+1
        fimTag = lista.find("<",psTag)        
        
        artigo[3] = [ lista[psTag:fimTag]]
        artigo[4] = ["Tecnologia"]
        
        #ler chamada e um paragrafo do artigo
        print " .",
        try:
            pagina = urllib2.urlopen(artigo[1])        
            textoArtigo = pagina.read().decode('iso-8859-1').encode('utf8')
        except:
            print "(erro ler artigo)",
            textoArtigo = ""
        item5 = ""
        inicio = "<p class='texto_description' itemprop='description'>"
        fim = "</p>"
        psInicio = textoArtigo.find(inicio)+len(inicio)
        psFim = textoArtigo.find(fim,psInicio)
        if (psInicio==-1) or (psFim==-1):
            print artigo[1],"pode ter problema! "
            salvarProblema(artigo)
        else:           
            item5 = "<h2>"+textoArtigo[ psInicio:psFim]+"</h2>"        
            ps = textoArtigo.find("</div><p>",psFim)+len("</div><p>")
            psFim = textoArtigo.find("</p>",ps)
            if (ps==-1) or (psFim==-1):
                print artigo[1],"pode ter problema! "
            else:    
                item5b = textoArtigo[ps:psFim]        
                artigo[5] = item5+semTags(item5b)
                l.append(artigo)
       
        ps = lista.find('<li class="wifl">',fimTag)
        
        
    print "lidos."
    print "Total oficinadanet: ",len(l)
    return l

def semTags(s):
    ps = s.find("<")
    if ps==-1:
        return s
    while ps>-1:        
        fim = s.find(">",ps)
        s = s[0:ps] + s[fim+1:] # retira o tag 
        ps = s.find("<",ps)
    
    return s


