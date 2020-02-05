grammar teste;

file  : inst* EOF;

inst  : prnt        #print
      | declation    #declaration
      ;

prnt : 'print' operation;

declation : VAR ':' operation;

operation : operation '+' operation                        #concat
		  | 'input' '(' operation ')'					   #input
		  | '(' operation '/' operation '/' operation ')'  #subs
		  | STRING                                         #string
		  | VAR											   #var
		  ;

STRING: '"' .*? '"'; 
VAR: [A-Za-z0-9]+;

WS: [ \t\r\n] -> skip;

	