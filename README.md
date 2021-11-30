# Avaliacão Módulo II

Foi criada uma API para obter informações sobre as escolas do sistema municipal de ensino do Recife.
Nesta primeira versão, é possível obter um json com as escolas por bairro, através do link:

http://127.0.0.1:5000/bairro/nome-do-bairro

onde nome-do-bairro deve ser substituído pelo bairro desejado.

Além de retornar um JSON com as informações das escolas, a API também salva um relatório, em JSON e CSV, com dados do número de escolas,
número de turmas, média de alunos e média de professores por tipo de escola (creche, cmei ou escola de ensino fundamental) no bairro selecionado.
É gerado também um boxplot da distribuição da quantidade de alunos nas escolas, comparando escolas que possuem biblioteca ou não, no bairro selecionado.

Para facilitar o uso da API, seguem alguns bairros do Recife que podem ser usados no teste da API:
VARZEA
COHAB
IBURA
CAMPO GRANDE
