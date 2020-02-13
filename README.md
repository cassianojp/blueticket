# Desafio
Web service de tradução de número por extenso.

_"Na linguagem de sua preferência, crie um servidor HTTP que, para cada requisição GET, retorne um JSON cuja chave extenso seja a versão por extenso do número inteiro enviado no path. Os números podem estar no intervalo [-99999, 99999].
Não esqueça dos "e"s separando milhares, centenas e dezenas (vide exemplo): "noventa e quatro mil e quinhentos e oitenta e sete". Esse não é o padrão da norma culta da língua portuguesa, e isso é intencional.
É esperado que você implemente o algoritmo de tradução."_

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


