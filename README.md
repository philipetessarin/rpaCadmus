# Projeto para o teste de RPA - CADMUS :computer:

## Descrição do Projeto :newspaper:

> A área de Recursos Humanos é responsável pelo processo de recrutamento dentro de uma determinada empresa.
Para mensurar a efetividade e desempenho da equipe de recrutamento o Gerente de Recursos Humanos atribuiu
a tarefa de gerar um relatório analítico de vagas abertas da empresa ao Assistente Administrativo. Diariamente
o Assistente Administrativo acessa o endereço [https://cadmus.com.br/vagas-tecnologia/](https://cadmus.com.br/vagas-tecnologia/){:target="_blank"} através do navegador
para extrair as vagas em aberto e compilar os dados em uma planilha do excel que contém minimamente três colunas
**(nome, local e descrição)**. Com a planilha formatada o Assistente Administrativo encaminha o 
documento por e-mail para o Gerente de Recursos Humanos para que seja feita a análise desejada.

## Solução

Para minimizar as tarefas repetitivas na área de Recursos Humanos com relação ao relatório analítico de vagas abertas, foi implementado um sistema usando a linguagem de programação Python, que visa automatizar a coleta de dados e também a geração e o envio por e-mail de uma planilha em Excel  para o Gerente de Recursos Humanos  contendo todas as vagas disponíveis no site.

## Funcionalidades

* **Coletar Vagas** - Tem por objetivo acessar o endereço [https://cadmus.com.br/vagas-tecnologia/](https://cadmus.com.br/vagas-tecnologia/)  e fazer a coleta de todos os nomes dos cargos, locais e  descrições.

![Página de vagas da Cadmus](https://uploaddeimagens.com.br/images/003/754/554/full/tela-01.png?1646414016)

* **Criar planilha** -  Tem por objetivo criar uma planilha em Excel e inserir todos os dados coletados nas colunas: Nome, Local e Descrição.

![Planilha analítica de vagas abertas](https://uploaddeimagens.com.br/images/003/754/589/full/tela-02.png?1646414922)

* **Enviar planilha por e-mail** - Tem por objetivo enviar a planilha criada em anexo por e-mail, para o Gerente de Recursos Humanos contendo no título e no corpo da mensagem,  a data na qual a mesma foi coletada e enviada.

![Planilha de e-mail Gmail](https://uploaddeimagens.com.br/images/003/754/635/full/tela-03.png?1646415919)

![Planilha de e-mail Gmail](https://uploaddeimagens.com.br/images/003/754/645/full/tela-04.png?1646416029)

## Rodando o projeto :bulb:

Python: Versão 3.10.2 | Chromedriver: Versão 99.0.4844.51

#### Clone este repositório
```
git clone https://github.com/philipetessarin/rpaCadmus
```

#### Acesse a pasta do projeto no terminal/cmd
```
cd rpaCadmus
```

#### Crie um ambiente virtualenv
```
virtualenv venv
```


#### Ative a virtualenv
````
venv/Scripts/Activate
````

#### Instale os pacotes que estão no arquivo requirements.txt
```
pip install -r requirements.txt
```

> Pronto! Execute o arquivo main.py no seu editor de preferência e verifique a planilha que foi enviada no e-mail rpa.cadmus@gmail.com. 


