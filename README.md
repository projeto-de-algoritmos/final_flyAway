# Fly Away

**Número da Lista**: X<br>
**Conteúdo da Disciplina**: XXXXXXXXXX<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 15/0135521 |  Leonardo dos S. S. Barreiros |
| 16/0124778 |  Ian Pereira de Sousa Rocha |

## Sobre 

<p align="justify">Normalmente quando vamos fazer uma viagem de longa distância observamos que é necessário pegar mais de um voo até chegar ao nosso destino,
na maioria dos casos e até mesmo aqui dentro do Brasil. Um exemplo seria ir para Lisboa, capital de Portugal, que para chegar até este destino, precisamos de um voo
daqui de Brasília para São Paulo e só então ir para Lisboa. Mas como poderiamos fazer isso de uma outra forma? talvés com um menor custo?

<p align="justify">Portanto, o objetivo deste projeto é atender ao módulo de grafos 2 com o tema de agendamento de voos. Trata-se de um webapp que utiliza uma API de voos e com base nos dados traçamos qual o melhor percurso em termos de custo e distância de um local para outro.

## Screenshots
Adicione 3 ou mais screenshots do projeto em funcionamento.

## Instalação

**Linguagem**: python<br>
**Framework**: FastApi<br>
Através do container docker terá acesso ao backend configurado, basta ter instalado docker e docker-compose.

**Linguagem**: javascript<br>
**Framework**: Vue.js v2<br>
É necessário ter o npm ou yarn para poder rodar o frontend.

## Uso 
Execute o container do backend com o comando:
```sh
$ docker-compose up --build
```

E para rodar o frontend basta executar em outro terminal o seguinte comando:
```sh
$ npm run serve
```
E acessar em seu navegador:

```sh
http://localhost:8080/ 

```

<p align="justify">Na tela principal basta inserir o local de onde deseja partir para o destino, então o algoritmo de Dijkstra irá retornar uma callback para ser renderizado em um canvas, informando os dados dos voos.


