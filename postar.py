# -*- coding: utf-8 -*-

import wordpresslib
import random
import time
import infoblogs
import os.path

from wordpresslib import WordPressException

def novopost(nroblog,titulo,descricao,link,foto,categorias,tags):

    blog = infoblogs.blogs[nroblog]
    # print blog+".wordpress.com"        
    url = 'https://'+blog+'.wordpress.com/xmlrpc.php'
    wp = wordpresslib.WordPressClient(url,blog,'pessoal123')
    #'pessoal'+str(nroblog+1)+'@egonkirchof.com.br','pessoal123')
    wp.selectBlog(0)

    if foto != "":
        arquivo = foto
        caminho = 'c:\\users\\egon\\downloads\\imagens blog\\'+arquivo
        if not os.path.isfile(caminho):
            print "foto nao encontrada: "+foto
            foto = ""
        else:
            imageSrc = wp.newMediaObject(caminho)
            #VER ANO E MES
            img = 'http://'+blog+'.files.wordpress.com/2017/02/'+arquivo

    while True: # escolhe parceiro
        idx = random.randint(0,len(infoblogs.blogs)-1)
        if idx != nroblog:
            break
            
    parceiro = "https://"+infoblogs.blogs[idx]+".wordpress.com"
    nome = infoblogs.nomes[idx]
        
    post = wordpresslib.WordPressPost()
    post.title = titulo
    txt = infoblogs.antes[random.randint(0,len(infoblogs.antes)-1)]    
    desc=txt+"<br><p><p>"+descricao
    
    if foto != "":
       desc = desc + "<br><p><img src='"+img+"'/>"               
    
    #add link
    if link != "":
        txt = infoblogs.saibamais[random.randint(0,len(infoblogs.saibamais)-1)]
        desc = desc+"<br><p>"+txt+"<a href='"+link+"'> clicando aqui</a>"

    txt = infoblogs.visite[random.randint(0,len(infoblogs.visite)-1)]
    desc = desc+"<br><p>"+txt+"<a href='"+parceiro+"'>"+nome+"</a>"
    txt = infoblogs.depois[random.randint(0,len(infoblogs.depois)-1)]
    desc = desc+"<br><p><p>"+txt

    post.description = desc
            
    post.tags = tags
    post.categories = categorias
    try:
        idp = wp.newPost(post,True)
    except WordPressException as e:
        print "*** Erro ao postar: "+e.message
    
    
        




        


