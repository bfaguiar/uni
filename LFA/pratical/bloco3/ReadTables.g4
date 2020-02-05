grammar ReadTables;

file   : header row+ EOF;
header : row;
row    : field (COMMA field)* NEWLINE;
field  : TEXT | STRING | ;

TEXT    : ~[,\n\r];
COMMA   : ',';
NEWLINE : '\r' ? '\n';
STRING  : [ \t]* '"' .* ? '"' [ \t]*;
