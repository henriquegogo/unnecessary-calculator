# Project: Unnecessary Calculator

This document outlines the development tasks for the Unnecessary Calculator project, structured in a way that resembles a task management system like Jira or Trello.

## Epics

Epics are large bodies of work that can be broken down into a number of smaller tasks.

*   **E01: Basic Calculator Functionality**
*   **E02: Web Interface**
*   **E03: Deployment**

## User Stories and Tasks

### Epic E01: Basic Calculator Functionality

This epic covers the implementation of the core calculator logic.

*   **US01: As a user, I want to be able to sum two numbers.**
    *   [ ] T01: Create a function to sum two numbers.
    *   [ ] T02: Write unit tests for the sum function.
*   **US02: As a user, I want to be able to subtract two numbers.**
    *   [ ] T03: Create a function to subtract two numbers.
    *   [ ] T04: Write unit tests for the subtract function.
*   **US03: As a user, I want to be able to multiply two numbers.**
    *   [ ] T05: Create a function to multiply two numbers.
    *   [ ] T06: Write unit tests for the multiply function.
*   **US04: As a user, I want to be able to divide two numbers.**
    *   [ ] T07: Create a function to divide two numbers.
    *   [ ] T08: Write unit tests for the divide function, including division by zero.

### Epic E02: Web Interface

This epic covers the development of the user-facing web interface.

*   **US05: As a user, I want to see a calculator interface in my browser.**
    *   [ ] T09: Create an HTML file with the basic calculator layout.
    *   [ ] T10: Style the calculator with CSS to make it look good.
*   **US06: As a user, I want to be able to click on the number buttons and see them on the display.**
    *   [ ] T11: Write JavaScript to handle number button clicks.
    *   [ ] T12: Update the display when a number button is clicked.
*   **US07: As a user, I want to be able to click on the operator buttons.**
    *   [ ] T13: Write JavaScript to handle operator button clicks.
    *   [ ] T14: Store the first number and the operator when an operator button is clicked.
*   **US08: As a user, I want to see the result of the calculation when I click the equals button.**
    *   [ ] T15: Create a server script to handle the calculation request.
    *   [ ] T16: The script should call the backend Python functions.
    *   [ ] T17: Write JavaScript to send the numbers and operator to the backend.
    *   [ ] T18: Display the result returned by the backend.

### Epic E03: Deployment

This epic covers the deployment of the application.

*   **US09: As a developer, I want to have a simple way to run the application locally.**
    *   [ ] T19: Create a shell script to start a local web server.
*   **US10: As a user, I want to access the calculator from the internet.**
    *   [ ] T20: Choose a hosting provider for the web application.
    *   [ ] T21: Configure the server to serve the frontend.
    *   [ ] T22: Configure the server to run the backend.
    *   [ ] T23: Deploy the application.
