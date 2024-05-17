# Prova 1
## O que é?
Aqui está presente uma API com grau de maturidade nivel 2. Com essa API você é capaz de criar novos pedidos, visualizar todos os pedidos e pedidos especifico além de editar e deletar pedidos também.
## Como executar?
Para executar corretamente essa aplicação, basta ir até a pasta raiz:<br>
`cd/src`<br>
e executar o compose:<br>
`docker compose up`<br>
Prontinho! o projeto ta rodando.<br>
Para este projeto, utilizei o insomnia para fazer os requests. Foi disponibilizada a collection deles na pasta static.<br><br>
![image](https://github.com/gustavo-francisco/prova-1-m10/assets/99208114/e50df985-bc84-4737-b9cb-22a72ba7a39b)<br><br>
Para fazer os requests, basta ir até o método que você deseja e cumprir os requisitos dele. Sendo esses:<br>
**GET-ALL**: Basta enviar a requisição.<br>
**GET-SPECIFIC**: Basta enviar a requisição. *Não se esqueça de colocar o id do pedido que você quer visualizar na url.<br>
**POST**: Precisa de um body JSON com os campos "usuario", "email" e "descricao".<br>
**PUT**: Precisa de um body JSON com um ou mais dos campos acima.<br>
**DELETE**: Basta enviar a requisição. *Não se esqueça de colocar o id do pedido que você quer deletar na url.


