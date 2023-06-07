# ASP_Exercises
Using ASP to solve two example exercises with clingo and telingo systems respectively.

Answer Set Programming (ASP) is a declarative programming paradigm used for solving complex problems. It allows you to express a problem in terms of rules and constraints and then find solutions that satisfy those constraints. Clingo is an ASP solver developed by the Potassco project. Telingo is an extension of clingo that incorporates temporal reasoning capabilities.

- Clingo can be installed from: https://potassco.org/clingo/
- Telingo can be installed from: https://github.com/potassco/telingo

Instructions of how to run each example are provided on a file inside each project. The two problems are described below:

## Binario puzzle

The Binairo puzzle is played on a square grid of cells, each of which can be filled with a white circle, a black circle, or left empty. The objective is to fill the grid according to specific rules:

- Each row and each column must have an equal number of white and black circles, which is half the size of the grid (n/2).
- There cannot be more than two consecutive circles of the same color in any direction (vertical or horizontal).
- No two rows or two columns can have the same configuration.

## Wire routing problem

Given a rectangular grid, the goal is to connect pairs of points (represented by letters) using non-intersecting lines, while avoiding obstacles. An initial configuration is provided, and the output is a text file representing the solution with wires labeled by their corresponding letters.

