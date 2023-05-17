<h1>Seleção de Candidatos</h1>

> Projeto Individual Módulo 2 - Resilia Educação

> Status: Em Andamento ⚠️


Projeto desenvolvido com intuito de avaliação individual no curso intensivo de Data Analytics na Resilia Educação.

No mesmo, foi criado um código Python que contenha uma lista de candidatos à uma vaga e esses candidatos foram avaliados de quatro formas:

+ Entrevista
+ Teste Teórico
+ Teste Prático
+ Avaliação de Soft Skills

Suas notas em cada etapa são armazenadas em uma lista contento tuplas com as notas de cada candidato.

Após isso, o programa solicita que o usuário digite a nota que ele deseja para atender a vaga em questão. O usuário assim digitando, o programa retorna uma string no formato eX_tX_pX_sX sendo que cada X é substituído pela avaliação do candidato nas etapas do processo - entrevista(e), teste teórico(t), teste prático(p) e avaliação de soft skills(s).

## Exemplo

<table>
  <tr></tr>
    <td>CANDIDATO_1</td><td>e6_t8_p5_s1</td>
  <tr></tr>
  <tr></tr>
    <td>CANDIDATO_2</td><td>e9_t6_p7_s8</td>
  <tr></tr>
    <tr></tr>
    <td>CANDIDATO_3</td><td>e6_t8_p1_s0</td>
  <tr></tr>
</table>

Nesta tabela, o candidato recebe sua nota em formato de string e quando o usuário digitar as notas desejadas retornará também nesse formato. No final, se algum candidato foi selecionado segundo as notas que o usuário informou como entrada o programa retornará com a frase:
> Os candidatos selecionados foram (candidatos).

OU

> Nenhum candidato foi selecionado.
