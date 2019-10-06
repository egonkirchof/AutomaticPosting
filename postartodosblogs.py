# -*- coding: utf-8 -*-

import wordpresslib
import random
import time
import infoblogs


def postarEmtodos(blog,titulo,descricao,link,foto="",categorias=["Tecnologia da Informação"],tags=["Tecnologia da Informação"],perc=0.8):

    
    for x in range(0,len(blogs)):
        if random.random()>perc:
            print blogs[x]+".wordpress.com"
        
            url = 'https://'+blogs[x]+'.wordpress.com/xmlrpc.php'
            wp = wordpresslib.WordPressClient(url,'pessoal'+str(x+1)+'@egonkirchof.com.br','pessoal123')
            wp.selectBlog(0)

            # VER NUMERO DA IMAGEM
            if foto != "":
                arquivo = foto #'blogimg3.jpg'
                imageSrc = wp.newMediaObject('c:\\users\\egon\\downloads\\'+arquivo)
                #VER ANO E MES
                img = 'http://'+blogs[x]+'.files.wordpress.com/2016/05/'+arquivo

            while True: # escolhe parceiro
                idx = random.randint(0,len(blogs)-1)
                if idx != x:
                    break
            
            parceiro = "https://"+blogs[idx]+".wordpress.com"
            nome = nomes[idx]

        
            post = wordpresslib.WordPressPost()
            post.title = titulo
            desc=descricao
            if foto != "":
                desc = desc + "<br><p><img src='"+img+"'/>"
                
            txt = saibamais[random.randint(0,len(saibamais)-1)]
            desc = desc+"<br><p>"+txt+"<a href='"+link+"'> clicando aqui</a>"
            txt = visite[random.randint(0,len(visite)-1)]
            desc = desc+"<br><p>"+txt+"<a href='"+parceiro+"'>"+nome+"</a>"
            post.description = desc
            
            post.tags = tags
            post.categories = categorias
            #idp = wp.newPost(post,True)
            # print "(pausa)"
            time.sleep(1)
        
    print "...fim"







        


