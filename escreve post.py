import wordpresslib
url = 'https://aprendatecnologiablog.wordpress.com/xmlrpc.php'
wp = wordpresslib.WordPressClient(url,'pessoal2@egonkirchof.com.br','pessoal123')
wp.selectBlog(0)

arquivo = 'blog2.jpg'
imageSrc = wp.newMediaObject('c:\\users\\egon\\downloads\\'+arquivo)
img = 'http://aprendatecnologiablog.files.wordpress.com/2016/05/'+arquivo

post = wordpresslib.WordPressPost()
post.title = "3Cansado de procurar?"
post.description = "Achou!<br>"+'<img src="'+img+'"/>'
idp = wp.newPost(post,True)


