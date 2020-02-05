grammar CSV;

file    :   row+ EOF;
row     :   field (',' field)* NEWLINE;

field   :   TEXT
        |   STRING
        |
        ;

TEXT    :   ~[,\n\r"]+;
NEWLINE :   '\r' ? '\n';
STRING  :   [ \t]* '"' .*? '"' [ \t]*;
