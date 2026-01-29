# Projeto: Calculadora Desnecessária

Este documento descreve as tarefas de desenvolvimento para o projeto Calculadora Desnecessária, estruturado de uma forma que se assemelha a um sistema de gerenciamento de tarefas como Jira ou Trello.

## Épicos

Épicos são grandes corpos de trabalho que podem ser divididos em várias tarefas menores.

*   **E01: Funcionalidade Básica da Calculadora**
*   **E02: Interface Web**
*   **E03: Implantação**

## Histórias de Usuário e Tarefas

### Épico E01: Funcionalidade Básica da Calculadora

Este épico cobre a implementação da lógica principal da calculadora.

*   **US01: Como usuário, eu quero poder somar dois números.**
    *   [ ] T01: Criar uma função para somar dois números.
    *   [ ] T02: Escrever testes unitários para a função de soma.
*   **US02: Como usuário, eu quero poder subtrair dois números.**
    *   [ ] T03: Criar uma função para subtrair dois números.
    *   [ ] T04: Escrever testes unitários para a função de subtração.
*   **US03: Como usuário, eu quero poder multiplicar dois números.**
    *   [ ] T05: Criar uma função para multiplicar dois números.
    *   [ ] T06: Escrever testes unitários para a função de multiplicação.
*   **US04: Como usuário, eu quero poder dividir dois números.**
    *   [ ] T07: Criar uma função para dividir dois números.
    *   [ ] T08: Escrever testes unitários para a função de divisão, incluindo divisão por zero.

### Épico E02: Interface Web

Este épico cobre o desenvolvimento da interface web para o usuário.

*   **US05: Como usuário, eu quero ver uma interface de calculadora no meu navegador.**
    *   [ ] T09: Criar um arquivo HTML com o layout básico da calculadora.
    *   [ ] T10: Estilizar a calculadora com CSS para que ela tenha uma boa aparência.
*   **US06: Como usuário, eu quero poder clicar nos botões de número e vê-los no visor.**
    *   [ ] T11: Escrever JavaScript para lidar com cliques nos botões de número.
    *   [ ] T12: Atualizar o visor quando um botão de número for clicado.
*   **US07: Como usuário, eu quero poder clicar nos botões de operador.**
    *   [ ] T13: Escrever JavaScript para lidar com cliques nos botões de operador.
    *   [ ] T14: Armazenar o primeiro número e o operador quando um botão de operador for clicado.
*   **US08: Como usuário, eu quero ver o resultado do cálculo quando eu clicar no botão de igual.**
    *   [ ] T15: Criar um script de servidor para lidar com a solicitação de cálculo.
    *   [ ] T16: O script deve chamar as funções Python do backend.
    *   [ ] T17: Escrever JavaScript para enviar os números e o operador para o backend.
    *   [ ] T18: Exibir o resultado retornado pelo backend.

### Épico E03: Implantação

Este épico cobre a implantação da aplicação.

*   **US09: Como desenvolvedor, eu quero ter uma maneira simples de executar a aplicação localmente.**
    *   [ ] T19: Criar um script de shell para iniciar um servidor web local.
*   **US10: Como usuário, eu quero acessar a calculadora pela internet.**
    *   [ ] T20: Escolher um provedor de hospedagem para a aplicação web.
    *   [ ] T21: Configurar o servidor para servir o frontend.
    *   [ ] T22: Configurar o servidor para executar o backend.
    *   [ ] T23: Implantar a aplicação.
