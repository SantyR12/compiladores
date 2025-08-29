grammar SwitchLang;

// 📌 REGLA PRINCIPAL
query       : SELECT column_list FROM table (WHERE condition)? SEMI ;

// 📌 Definición de columnas y tabla
column_list : STAR | column (COMMA column)* ;
column      : IDENTIFIER ;
table       : IDENTIFIER ;

// 📌 Condición en WHERE
condition   : column operator value ;
operator    : GT | LT | EQ | GE | LE | NE ;
value       : NUMBER | STRING ;

// 📌 PALABRAS RESERVADAS
IF     : 'if' ;
ELSE   : 'else' ;
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
ASSIGN : '=' ;
PLUS   : '+' ;
MINUS  : '-' ;
MUL    : '*' ;
DIV    : '/' ;
GT     : '>' ;
LT     : '<' ;
EQ     : '==' ;
NEQ    : '!=' ;
SEMI   : ';' ;
SEMA   : ':' ;


// 📌 IDENTIFICADORES Y VALORES
IDENTIFIER  : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER      : [0-9]+ ('.' [0-9]+)? ;

// 📌 CORRECCIÓN DE `STRING` PARA EVITAR EL ERROR
STRING      : '\'' (~('\'' | '\r' | '\n'))* '\'' ;

// 📌 IGNORAR ESPACIOS Y SALTOS DE LÍNEA
WS          : [ \t\r\n]+ -> skip ;