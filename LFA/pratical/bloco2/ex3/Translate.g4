grammar Translate ;

file   : (line)* EOF            ;
line   : NUM '-' CARACT NEWLINE ;

NUM    : [0-9]+      ;
CARACT : [a-z]+      ;
NEWLINE: '\r' ? '\n' ; // optativo.
WS   : [ \t] -> skip ;
