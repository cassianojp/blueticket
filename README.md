# Desafio
Web service de tradução de número por extenso.

_Obs.: o desenvolvimento da aplicação foi feita sob a versão 3.7.6 do Python._

## Pré-requisitos
São necessários os seguintes frameworks para executar a aplicação com sucesso:
### Flask (framework web)
Para instalar, execute o seguinte comando:
```
$ pip3 install flask
```

### Pytest (framework de testes) 
Para instalar, execute o seguinte comando:
```
$ pip3 install pytest
```

## Para executar a aplicação
No diretório raiz da aplicação, execute o seguinte comando:
```
$ python3 app.py
```
Para testar o funcionamento pode-se utilizar o comando curl na porta 3000. Exemplos:
```
$ curl http://localhost:3000/99635
```
```
$ curl http://localhost:3000/-12345
```
```
$ curl http://localhost:3000/13
```
Este README também pode ser visualizado digitando o seguinte link no seu web browser:
```
http://localhost:3000
```
Para parar o serviço pressione as teclas:
```
Ctrl+C
```

## Para aplicar os testes unitários de software
Altere o diretório para:
```
$ cd test/
```
e execute o seguinte comando:
```
$ pytest
```
Se tudo estiver correto no código, conforme os testes programados, uma mensagem de sucesso será apresentada.


