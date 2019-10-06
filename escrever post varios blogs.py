# -*- coding: utf-8 -*-

import wordpresslib
import random

blogs = [
 "mundobpmn","aprendatecnologiablog",
 "desvendandoatecnologia","aprendavocemesmoti",
 "novidadesemtiblog","vidradosemtecnologia",
 "falandodetecnologiadainformacao","universotiblog",
 "tudosobretecnologiati","umpoucosobretudoti","colecaodeartigossobreti",
 "tudoqueexistesobreti","detudoumpoucoinformatica",
 "tiacessivel","mundodigitalatual","dicasetruquestecnologia",
 "tecnologiadoaaoz","cantinhodainformaticaetecnologia",
 "foradacasinhatecnologia","tempodeaprenderti",
 "aprendendosozinhoti","abcdatecnologiadainformacao",
 "blogdescomplicandoti","tiparatodosesemsegredos","mundodigitalaoseualcance",
 "nerdzoneti","mundogeekTI","tiparapessoascomuns",
 "maravilhasdatecnologia","odiariodeumnerd",
 "amantesdatecnologiati","zerobitsinformatica","tiemdoseshomeopaticas",
 "gotasdeti","tecnomundonovo","ozentismo","atualidadesti",
 "tecnoferas","fiquepordentroti","tidecaboarabo","liderancati",
 "100porcentoti","24por7pensandoti","viciadosemtecnologia2016",
 "ctrlaltdelinformatica","ctrlZtecnologia","sempanicoti",
 "somenteosnerdssaofelizes","sosnaoteminternet","anjosdati" ]


nomes = [ "Mundo BPMN","Aprenda Tecnologia",
          "Desevendando a Tecnologia","Aprenda Você Mesmo TI",
          "Novidades em TI","Vidrados em Tecnologia",
          "Falando de Tecnologia da Informação","Universo TI",
          "Tudo Sobre Tecnologia - TI","Um Pouco Sobre Tudo em TI",
          "Coleção de Artigos Sobre TI","Tudo que Existe Sobre TI",
          "De Tudo Um Pouco Informática","TI Acessível",
          "Mundo Digital Atual","Dicas e Truques - Tecnologia",
          "Tecnologia do A ao Z","Cantinho da Informatica e Tecnologia",
          "Fora da Casinha Tecnologia","Tempo de Aprender TI",
          "Aprendendo Sozinho TI","ABC da Tecnologia da Informação",
          "Blog Descomplicando TI","TI para Todos e Sem Segredos",
          "Mundo Digital ao Seu Alcance","Nerd Zone TI",
          "Mundo Geek TI","TI para Pessoas Comuns",
          "Maravilhas da Tecnologia","O Diario de um Nerd 2016",
          "Amantes da Tecnologia - TI","Zero Bits Informática",
          "TI em Doses Homeopáticas","Gotas de TI","Tecno Mundo Novo",
          "O Zen TIsmo","Atualidades TI","Tecno Feras",
          "Fique Por Dentro da TI","TI de Cabo a Rabo","Liderança em TI",
          "100% Tecnologia da Informação","24/7 Pensando em TI",
          "Viciados em Tecnologia 2016","CTRL+ALT+DEL Informática",
          "Ctrl+Z Tecnologia", "Sem Pânico! na TI",
          "Somente os Ners São Felizes", "S.O.S. Não tem Internet",
          "Anjos da TI" ]


for x in range(0,len(blogs)):
    if random.random()>0.8:
        print blogs[x]+".wordpress.com"
        
        url = 'https://'+blogs[x]+'.wordpress.com/xmlrpc.php'
        wp = wordpresslib.WordPressClient(url,'pessoal'+str(x+1)+'@egonkirchof.com.br','pessoal123')
        wp.selectBlog(0)

        # VER NUMERO DA IMAGEM
        arquivo = 'blogimg3.jpg'
        imageSrc = wp.newMediaObject('c:\\users\\egon\\downloads\\'+arquivo)
        #VER ANO E MES
        img = 'http://'+blogs[x]+'.files.wordpress.com/2016/05/'+arquivo

        while True:
            idx = random.randint(0,len(blogs)-1)
            if idx != x:
                break
            
        parceiro = "https://"+blogs[idx]+".wordpress.com"
        nome = nomes[idx]

        link = "http://exame.abril.com.br/tecnologia/noticias/se-pode-fazer-mais-contra-terrorismo-digital-diz-microsoft"
        
        post = wordpresslib.WordPressPost()

        post.title = "Podemos fazer mais contra terrorismo digital, diz Microsoft"
        

        post.description = (
            "A Microsoft informou na quarta-feira nas Nações Unidas que as companhias tecnológicas não podem evitar que os terroristas usem a internet, mas podem fazer mais contra o terrorismo digital."         
            "<br><p><img src='"+img+"'/>"
            "<br><p>Veja a matéria na íntegra "
            "<a href='"+link+"'> clicando aqui</a>"
            "<br><p>Visite também nosso blog parceiro: "
            "<a href='"+parceiro+"'>"+nome+"</a>")
        
        # MUDE OS TAGS TAMBEM!!!
        post.tags = ["Tecnologia da Informação","Notícia","Microsoft"]

        post.categories = ["Tecnologia da Informação"]
        
        idp = wp.newPost(post,True)

print "...fim"







        


