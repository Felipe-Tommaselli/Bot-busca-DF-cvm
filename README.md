# Bot-busca-DF-cvm
Programa de automatização em python com o objetivo de buscar as Demonstraçoes Financeiras (DF) de uma certa empresa pelo site da CVM. Os criterios de pesquisa podem ser facilmente alterados devido a divisão do código em "blocos" de busca.

# Instalação
Simples assim. Apenas é necessario ter o Google Chrome e o python instalado, alem disso o chromeriver.exe deixado no repositório tambem deve ser executado. 
As bibliotecas usadas podem ser instaladas pelos comandos no temrinal, ele pode ser acessado pesquisando prompt de comando na barra de pesquisa do windows:
pip install selenium
pip install time
pip install datetime
https://www.treinaweb.com.br/blog/gerenciando-pacotes-em-projetos-python-com-o-pip/

* Caso não seja possivel fazer sua instalação, devido a algum erro, pelo arquivo fornecido acredito que o site https://chromedriver.chromium.org/downloads. 
* Outra possivel fonte de erro (apenas caso não tenha funcionado o arquivo disponilizado) é uma incopatibilidade de versão. Acessando os tres pontinhos no canto superior direito do chrome > clicando em "Configurações" > descendo a barra até "Sobre o Google Chrome" é possivel ver a versão do seu google chrome. Desse modo, caso perceba que sua versão não condiz com o chrome driver fornecido, apenas instale a versão igual no site deixado acima.
* Uma outra possivel fonte de erro é a incompatibilidade com o PATH, nesse caso é recomendado que o chromedriver e o bot.py sejam colocados na mesma pasta dentro do computador. Essa simples realocação pode resolver o problema relacionado ao PATH sem mudanças no codigo.

**Não se preocupe! Não temos acesso aos seus dados, eles ficam salvos no seu computador**

# Uso do bot
É necessario apenas rodar o script em python (lembre que seu computador deve ter o python 3 instalado para isso). Para isso, com o arquivo ja adicionado ao seu computador, apenas sera necessario clicar em seu icone ou através do prompt de comando. https://cursos.alura.com.br/forum/topico-executar-o-programa-em-python3-pelo-prompt-de-comando-83408#

O programa fara algumas perguntas como o nome da empresa, e esta deve ser digitada corretamente caso contrario pode ocorrer uma busca incorreta, e a data de inicio da procura. Alem disso, sera necessario fazer algumas confirmações com quanto ao tipo de arquivo procurado, por default DFP. Logo após isso o bot abrirá as janelas e realizará as instruções, forneceno a pagina final, onde o usuario pode escolher como proceder com as informações. Alem disso, caso a pagina fique aberta por mais de 30 segundos, o bot perguntara se o usuario gostaria que o arquivo em .zip com as informações seja salvo.

# Para desenvolvedores:
* O código em Python esta no repositório em bot_code.py;
* Você precisará baixar o chromedriver e colocar ele na pasta em que estiver rodando o código (ou adicionar ao PATH);
* As bibliotecas de python necessárias são a **selenium**, **time** e  **datetime**. Use o pip install para a instalação delas;
* O codigo foi estruturado em um formato de blocos try/except, dessa forma é possivel identificar em que momento o bot esta exibindo algum erro sem interromper seu funcionamento;
