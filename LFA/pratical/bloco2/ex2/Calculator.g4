grammar Calculator;

program : stat* EOF ;

stat    : expr NEWLINE {
  System.out.println("result = " + $expr.result);
}
        | NEWLINE
        ;

expr returns[int result]  : op1=expr opx=( '*' | '/' ) op2=expr {
            if ($opx.text.equals("*"))
              $result = $op1.result * $op2.result;
            else
              $result = $op1.result / $op2.result;
          }
        | op1=expr opx=( '+' | '-' ) op2=expr {
            if ($opx.text.equals("+"))
              $result = $op1.result + $op2.result;
            else
              $result = $op1.result / $op2.result;
        }
        | INT {
          $result = Integer.parseInt($INT.text);
        }
        | '(' expr ')' {
          $result = $expr.result;
        }
        ;

INT    : [0-9]+         ;
NEWLINE: '\r' ? '\n'    ;
WS     : [ \t]+ -> skip ;
