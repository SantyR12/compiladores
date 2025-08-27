grammar Calculadora;

prog: expresion EOF ;
// Regla principal
expresion : '-' expresion                   # Negativo
          | funcion                         # Funciones
          | expresion '^' expresion         # Potencia
          | expresion ('*'|'/') expresion   # MultDi
          | expresion ('+'|'-') expresion   # AddSub  
          | '(' expresion ')'               # Parentesis
          | NUMBER                          # Numero
          ;

funcion
    : ID '(' expresion ')'
    ;

// Tokens
NUMBER : [0-9]+ ('.' [0-9]+)? ;
ID : [a-zA-Z_][a-zA-Z_0-9]* ;
WS : [ \t\r\n]+ -> skip ;