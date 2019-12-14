# -*- coding: utf-8 -*-

articles = []
mine = []
article = []
mine_id = "(meu)"

def a(s): # monta o artigo
    global article
    article.append(s)

def c(): # fecha o artigo
    global articles,article
    if len(article) != 6:
        print( "!!!! Article ",len(articles), ", wrong format:")
        print( article )
        print( "!!!!")
    if article[0][0:len(mine_id)]==mine_id:
        article[0] = article[0][len(mine_id):]
        mine.append(len(articles))
        
    articles.append(article)
    article=[]
    
# [youtube link]
    
# titulo
# link
# imagem
# tags
# categoria
# texto

# 5/1/17


### MEUS

a("(meu)Tutorial básico para aprender BPMN")
a("http://egonkirchof.com.br/Aprenda-Bpmn/index.html")
a("")
a(["BPMN","Modelagem","Processos de negócios","Youtube","Ensino"])
a(["Tecnologia da informação"])
a("Uma nova fonte de informação para quem precisa aprender a desenhar processos de negócios utilizando BPMN")
c()

a("(meu)Tutorial BPMN: piscina")
a("http://egonkirchof.com.br/Aprenda-Bpmn/Tutorial-Bpmn-Piscina.html")
a("")
a(["BPMN","Modelagem","Processos de negócios","Youtube","Ensino"])
a(["Tecnologia da informação"])
a("Se precisa utilizar BPMN para criar processos de negócios, este novo tutorial pode ser de ajuda.")
c()

a("(meu)Tutorial para aprender BPMN - raia")
a("http://egonkirchof.com.br/Aprenda-Bpmn/Tutorial-Bpmn-Raia.html")
a("")
a(["BPMN","Modelagem","Processos de negócios","Youtube","Ensino"])
a(["Tecnologia da informação"])
a("Uma nova fonte de informação para quem precisa aprender a desenhar processos de negócios utilizando BPMN. Neste link, você encontrará como funciona o objeto raia.")
c()


a("(meu)Tutorial BPMN: eventos")
a("http://egonkirchof.com.br/Aprenda-Bpmn/Tutorial-Bpmn-Eventos.html")
a("")
a(["BPMN","Modelagem","Processos de negócios","Youtube","Ensino"])
a(["Tecnologia da informação"])
a("Veja como utilizar eventos dentro de um processo de negócios, neste novo tutorial sobre BPMN.")
c()

a("(meu)Tutorial BPMN: tarefas")
a("http://egonkirchof.com.br/Aprenda-Bpmn/Tutorial-Bpmn-Tarefas.html")
a("")
a(["BPMN","Modelagem","Processos de negócios","Youtube","Ensino"])
a(["Tecnologia da informação"])
a("Nesta página do tutorial sobre BPMN, aprenda como utilizar as tarefas no seu diagrama.")
c()

a("(meu)Tutorial BPMN: linhas de fluxo, mensagem e associação")
a("http://egonkirchof.com.br/Aprenda-Bpmn/Tutorial-Bpmn-Linhas.html")
a("")
a(["BPMN","Modelagem","Processos de negócios","Youtube","Ensino"])
a(["Tecnologia da informação"])
a("Para que o seu diagrama BPMN possa representar com toda propriedade o processo de negócio, vocë vai precisar saber como utilizar as linhas que conectam os objetos."
  "Nesta parte do tutorial, veja para que servem as linhas de fluxo, de mensagem e associação")
c()


a("(meu)Tutorial BPMN: decisões")
a("http://egonkirchof.com.br/Aprenda-Bpmn/Tutorial-Bpmn-Decisoes.html")
a("")
a(["BPMN","Modelagem","Processos de negócios","Youtube","Ensino"])
a(["Tecnologia da informação"])
a("Dentro de um processo de negócios, muitas vezes precisamos tomar caminhos diferentes, de acordo com eventos ou condiç$oes relevantes para o processo."
  "<br>Aprenda como utilizar os objetos de decisões, para poder desenhar corretamente processos com a BPMN.")
c()


a("(meu)Tutorial BPMN: artefatos")
a("http://egonkirchof.com.br/Aprenda-Bpmn/Tutorial-Bpmn-Artefatos.html")
a("")
a(["BPMN","Modelagem","Processos de negócios","Youtube","Ensino"])
a(["Tecnologia da informação"])
a("Veja neste tutorial de BPMN como utilizar os objetos chamados artefatos, objetos de dados, grupos e anotações.")
c()


a("(meu)Tutorial BPMN: sub-processos")
a("http://egonkirchof.com.br/Aprenda-Bpmn/Tutorial-Bpmn-Subprocessos.html")
a("") 
a(["BPMN","Modelagem","Processos de negócios","Youtube","Ensino"])
a(["Tecnologia da informação"])
a("Quando seu diagrama de processo de negócio se torna muito cheio, talvez seja o momento de colocar certas tarefas dentro de um sub-processo."
  "<br>O uso de sub-processos melhora a visibilidade do diagrama, além de poder prover maior compreensão do que está sendo executado."
  "<br>Neste tutorial de BPMN, entenda como utilizar objetos de sub-processos.")
c()


a("(meu)Tutorial BPMN: transações")
a("http://egonkirchof.com.br/Aprenda-Bpmn/Tutorial-Bpmn-Transacoes.html")
a("")
a(["BPMN","Modelagem","Processos de negócios","Youtube","Ensino"])
a(["Tecnologia da informação"])
a("Neste tutorial sobre BPMN, você irá aprender como utilizar transações no seu diagrama de processo de negócio."
  "<br>As transações ajudam a manter a consistência durante a execução do processo, garantindo que certas tarefas que devem ser todas executadas para serem válidas ofereçam um mecanismo para reverter o estado do processo, em caso de falhas.")
c()




a("(meu)Aprenda BPMN em 5 minutos...")
a("https://youtu.be/udL59Ft3h5Y")
a("")
a(["BPMN","Modelagem","Processos de negócios","Youtube","Ensino"])
a(["Tecnologia da informação"])
a("Interessado em aprender como utilizar a BPMN para modelar processos de negócios, mas sem tempo para longos tutoriais?"
  "<br>Essa série de vídeos do youtube pretende ensinar em apenas 5 minutos partes essenciais do padrão BPMN."
  "<br>Neste vídeo, o elemento mais básico de qualquer diagrama: a piscina"
  "<p><br>[youtube https://youtu.be/udL59Ft3h5Y]<br>")
c()
  

a("(meu)Aprenda BPMN em 5 minutos: raias ou lanes")
a("https://youtu.be/vvAzRnzdOBA")
a("")
a(["BPMN","Modelagem","Processos de negócios","Bizagi","Youtube","Ensino"])
a(["Tecnologia da informação"])
a("Interessado em aprender como utilizar a BPMN para modelar processos de negócios, mas sem tempo para longos tutoriais?"
  "<br>Essa série de vídeos do youtube pretende ensinar em apenas 5 minutos partes essenciais do padrão BPMN."
  "<br>Neste vídeo, veja como funciona a raia (lane)"
  "<p><br>[youtube https://youtu.be/vvAzRnzdOBA]<br>")
c()

a("(meu)Aprenda BPMN em exemplos...")
a("")
a("imagemlivro1.jpg")
a(["BPMN","Modelagem","Procesos de negócios","Bizagi","Amazon","Aprendizado"])
a(["Tecnologia da Informação"])
a("Quer aprender como desenhar diagramas de processos de negócios?"
  "<br>Este livro pode ser uma ótima chance de começar a desenvendar o mundo da BPMN"
  "<br>Com linguagem clara, de fácil entendimento, ele te leva num passo a passo dos conceitos básicos aos mais sofitisticados necessários para modelar processos denegócios."
  "<br>Cheio de figuras explicativas, utiliza vários exemplos para que você entenda melhor o uso da BPMN."
  "<br>Pode ser útil também como um guia para o software Bizagi, muito utilizado para desenhar diagramas de processos usando BPMN."
  "<p>Confira mais, visitando o site da amazon, <a href='https://www.amazon.com.br/BPMN-exemplos-aprenda-modelar-processos-ebook/dp/B00WASBTU0/ref=sr_1_3?ie=UTF8&qid=1463340168&sr=8-3&keywords=egon+kirchof'>clicando aqui.</a>")

c()

a("(meu)SQL para iniciantes")
a("")
a("imagemlivro2.jpg")
a(["SQL","MySql","Aprendizado","Amazon","Iniciante","Leigos"])
a(["Tecnologia da Informação"])
a("Precisa de um guia de fácil uso e entendimento para aprender SQL?"
  "<br><p>Neste livro você vai aprender os conceitos fundamentais da linguagem SQL, utilizando o gerenciador de bancos de dados mySql."
  "Com informação detalhada, passo a passos dos comandos básicos do SQL, é uma ótima fonte de informações para quem está iniciando no mundo dos bancos de dados."
  "Veja mais detalhes no site da Amazon, basta <a href='https://www.amazon.com.br/SQL-para-iniciantes-Egon-Kirchof-ebook/dp/B010KAW0L6/ref=sr_1_1?ie=UTF8&qid=1463340168&sr=8-1&keywords=egon+kirchof'>clicar aqui.</a>")
c()

a("(meu)Aprendizado de Máquina com Microsoft Azure: introdução ao machine learning")
a("")
a("imagemlivro3.jpg")
a(["Machine learning","Aprendizado de máquina","Inteligência Artificial","Azure","Microsoft"])
a(["Tecnologia da Informação"])
a("Desde análise de mercados de ações até carros que se dirigem sozinhos, o aprendizado de máquina (machine learning) é um dos campos da inteligência artificial que mais floresceram nos últimos anos."
  "<br>A Microsoft, claro, não poderia ficar fora desse excitante mercado d TI e criou sua plataforma para desenvolver algoritmos de Machine Learning utilizando a cloud Microsoft - Azure."
  "<br>Se você gostaria de uma introdução suave mas bastante completa ao machine learning, utilizando o ambiente de desenvolvimento Microsoft Azure, este livro pode lhe ser bastante útil."
  "<br>Informe-se mais, visitando o site da amazon, através do link disponível <a href='https://www.amazon.com.br/Aprendizado-M%C3%A1quina-com-Microsoft-Azure-ebook/dp/B018BK1MEI/ref=sr_1_2?ie=UTF8&qid=1463340168&sr=8-2&keywords=egon+kirchof'>clicando aqui!</a>")
c()

a("(meu)Aprendizado de Máquina com Microsoft Azure")
a("https://www.youtube.com/watch?v=1VO8VFc0GDs")
a("")
a(["Machine learning","Aprendizado de máquina","Inteligência Artificial","Azure","Youtube","Microsoft"])
a(["Tecnologia da Informação"])
a("Veja neste vídeo como é fácil utilizar o ambiente cloud da Microsoft Azure para criar algoritmos de aprendizado d emáquina (machine learning)."
  "<br><p>[youtube https://www.youtube.com/watch?v=1VO8VFc0GDs]<br>")
c()


a("(meu)Como recuperar a senha de root do mySQL")
a("https://www.youtube.com/watch?v=VyB_j-4IErg")
a("")
a(["MySql","SQL","Youtube","Ensino"])
a(["Tecnologia da Informação"])
a("Se você perder a senha de root (administrador) da sua instalação do MySQl, não se desespere."
  "<br>Neste vídeo você verá como é fácil recuperar a senha de root do MySql."
  "<br><p>[youtube https://www.youtube.com/watch?v=VyB_j-4IErg]."
  "<br>Seus problemas acabaram :)")
c()

a("(meu)Aprenda BPMN em 5 minutos: eventos")
a("https://youtu.be/Wrd1MV3L6s8")
a("")
a(["BPMN","Modelagem","Processos de negócios","Bizagi","Youtube","Ensino"])
a(["Tecnologia da informação"])
a("Interessado em aprender como utilizar a BPMN para modelar processos de negócios, mas sem tempo para longos tutoriais?"
  "<br>Essa série de vídeos do youtube pretende ensinar em apenas 5 minutos partes essenciais do padrão BPMN."
  "<br>Neste vídeo, veja para que servem os eventos"
  "<p><br>[youtube https://youtu.be/Wrd1MV3L6s8]<br>")
c()

a("(meu)Aprenda BPMN em 5 minutos: tarefas")
a("https://youtu.be/0MWSakI5iaU")
a("")
a(["BPMN","Modelagem","Processos de negócios","Youtube","Ensino"])
a(["Tecnologia da informação"])
a("Interessado em aprender como utilizar a BPMN para modelar processos de negócios, mas sem tempo para longos tutoriais?"
  "<br>Essa série de vídeos do youtube pretende ensinar em apenas 5 minutos partes essenciais do padrão BPMN."
  "<br>Neste vídeo, aprenda o que são tarefas."
  "<p><br>[youtube https://youtu.be/0MWSakI5iaU]<br>")
c()

a("(meu)Aprenda BPMN em 5 minutos: gateways")
a("https://youtu.be/hp7RsKLzAHQ")
a("")
a(["BPMN","Modelagem","Processos de negócios","Youtube","Ensino"])
a(["Tecnologia da informação"])
a("Interessado em aprender como utilizar a BPMN para modelar processos de negócios, mas sem tempo para longos tutoriais?"
  "<br>Essa série de vídeos do youtube pretende ensinar em apenas 5 minutos partes essenciais do padrão BPMN."
  "<br>Neste vídeo, aprenda o que são gateways (decisões)."
  "<p><br>[youtube https://youtu.be/hp7RsKLzAHQ]<br>")
c()

    
  
    
print( "Total: ",len(articles))
print( "Mine: ",len(mine))






  



  
  

  
