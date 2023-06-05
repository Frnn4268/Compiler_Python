grammar MiLenguaje;

start: statement+;

statement: IF condition THEN action
        | ELSE THEN action
        | FOR variable EQUALS expression TO expression action
        | WHILE condition action
        | ELIF condition action
        | variableDeclaration
        | assignment;

condition: expression OPERATOR expression;

action: PRINT OPEN_PAREN (expression | expression_print) CLOSE_PAREN;

expression: arithmeticExpression | assignmentExpression;

expression_print: '"' (LETTER+ | NUMBER+)+  '"';

arithmeticExpression: additiveExpression;

additiveExpression: multiplicativeExpression (PLUS multiplicativeExpression | MINUS multiplicativeExpression)* | ;

multiplicativeExpression: primaryExpression (MULTIPLY primaryExpression | DIVIDE primaryExpression)*;

assignmentExpression: '"' (LETTER+ | NUMBER+)+  '"';

primaryExpression: variable
                | OPEN_PAREN arithmeticExpression CLOSE_PAREN
                | NUMBER;

variableDeclaration: LETTER+ EQUALS expression | LETTER+ EQUALS assignmentExpression;

assignment: variable EQUALS expression;

variable: LETTER+;

IF: 'SI';
THEN: 'ENTONCES';
ELSE: 'SINO';
ELIF: 'SWITCH';
PRINT: 'IMPRIMIR';
FOR: 'PARA';
WHILE: 'MIENTRAS';
TO: 'HASTA';
EQUALS: '=';
OPERATOR: ('>' | '<' | '==' | '!=');
OPEN_PAREN: '(';
CLOSE_PAREN: ')';
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
NUMBER: DIGIT+ ('.' DIGIT+)?;
LETTER: [a-zA-Z];
DIGIT: [0-9];

WHITESPACE: [ \t\r\n]+ -> skip;