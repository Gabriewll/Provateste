1) No selenium IDE é utilizado para automações que gravam os testes. Já no Selenium WebDriver é utilizado com alguma linguagem de programação, como por exemplo o python.

2) Um dos locators que podem ser utilizados é o “ID” que pega o id do elemento para ser manipulado. Outro exemplo é o “XPATH” que permite que o navegador execute um comando pelo seu XPATH
   
3) “navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/form/button').click()”    na linha de código acima tem um exemplo que vai apertar o botão do formulário procurando o  elemento pelo “find_element” usando o método “click()”
   
4) Quando tentamos interagir com um elemento que não foi carregado na página a automação para e ocorre um erro. Para resolver esse tipo de problema utilizamos o “time.sleep” e determinamos um tempo para ele carregar, por exemplo, “time.sleep(5)”.
   
5) Algumas das limitações encontradas na IDE é a falta de recursos para realizar uma manutenção no teste, outro tipo de limitação é por não suportar teste avançados
