# Bot_busca_DF_cvm
Programa de automatização em python com o objetivo de buscar as Demonstraçoes Financeiras (DF) de uma certa empresa pelo site da CVM. Os criterios de pesquisa podem ser facilmente alterados devido a divisão do código em "blocos" de busca.

# Instalação
Simples assim. Apenas é necessario ter o Google Chrome instalado e o chromeriver.exe deixado no repositório. 
* Caso não seja possivel fazer sua instalação, devido a algum erro, pelo arquivo fornecido acredito que o site < https://chromedriver.chromium.org/downloads >. 
* Outra possivel fonte de erro (apenas caso não tenha funcionado o arquivo disponilizado) é uma incopatibilidade de versão. Acessando os tres pontinhos no canto superior direito do chrome > clicando em "Configurações" > descendo a barra até "Sobre o Google Chrome" é possivel ver a versão do seu google chrome. Desse modo, caso perceba que sua versão não cofdiz com o chrome driver fornecido, apenas instale a versão igual no site deixado acima.
**Não se preocupe! Não temos acesso aos seus dados, eles ficam salvos no seu computador**

# Uso do bot
É necessario apenas rodar o arquivo .bat fornecido, ou rodar o script em python (lembre que seu computador deve ter o python 3 instalado para isso).
O programa fara algumas perguntas como o nome da empresa, e esta deve ser digitada corretamente caso contrario pode ocorrer uma busca incorreta, e a data de inicio da procura. Alem disso, sera necessario fazer algumas confirmações com quanto ao tipo de arquivo procurado, por default DFP. Logo após isso o bot abrirá as janelas e realizará as instruções, forneceno a pagina final, onde o usuario pode escolher como proceder com as informações. Alem disso, caso a pagina fique aberta por mais de 30 segundos, o bot perguntara se o usuario gostaria que o arquivo em .zip com as informações seja salvo.

# Para desenvolvedores:
* Os códigos do Python estão na pasta PythonScripts;
* Você precisará baixar o chromedriver e colocar ele na pasta em que estiver rodando o código (ou adicionar ao PATH);
* As bibliotecas de python necessárias são a **selenium**, **time** e  **datetime**. Use o pip install para a instalação delas;
* O codigo foi estruturado em um formato de blocos try/except, dessa forma é possivel identificar em que momento o bot esta exibindo algum erro sem interromper seu funcionamento;
