% -------------------------
% Author: Luis Ruanova Lea
% -------------------------

% Problem context ( + domain.lp file)
row(0..n-1).
col(0..n-1).
color(0). color(1). % 0,1 = white, black

% -----------
% Generator
% -----------

{cell(X,Y,C) : color(C) } = 1 :- row(X), col(Y).

    % Alternative implementation much more longer
    % {board(I,J) : row(I), col(J)}.
    % :- {board(I,J)} != n*n.

    % {cell(X,Y,C) : color(C) } = 1 :- board(X,Y). 



% -----------
% Tester
% -----------

% There cannot be more than 2 consecutive circles of the same color in any direction (vertical or horizontal).

:- cell(X-1,Y,C), cell(X,Y,C2), cell(X+1,Y,C3), C==C2,C2==C3.
:- cell(X,Y+1,C), cell(X,Y,C2), cell(X,Y-1,C3), C==C2,C2==C3.

    % Alternative try MUCH more longer:
    % :- cell(X,Y,C), cell(X+1,Y,C), cell(X+2,Y,C). %rows with 3 positive consecutives 
    % :- cell(X,Y,C), cell(X-1,Y,C), cell(X-2,Y,C). %rows with 3 negative consecutives
    % :- cell(X,Y,C), cell(X+1,Y,C), cell(X-1,Y,C). %rows with intercalate consecutives
    % :- cell(X,Y,C), cell(X,Y+1,C), cell(X,Y+2,C). %cols with 3 positive consecutives 
    % :- cell(X,Y,C), cell(X,Y-1,C), cell(X,Y-2,C). %cols with 3 negative consecutives
    % :- cell(X,Y,C), cell(X,Y+1,C), cell(X,Y-1,C). %cols with intercalate consecutives


% Each row and each column must contain the same number of circles of each color, 
% that is, n/2 instances of each case.
:- row(X), #count{Y: cell(X,Y,0)} != n/2.
:- col(Y), #count{X: cell(X,Y,0)} != n/2.

%There cannot be two rows or two columns with the same configuration.
:- row(X), row(X'), X>X', #count{Y: cell(X,Y,C), cell(X',Y,C)} = S, S=n.
:- col(Y), col(Y'), Y>Y', #count{X: cell(X,Y,C), cell(X,Y',C)} = S, S=n.
