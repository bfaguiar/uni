grammar Hello ;

top       : (greetings | bye)+ EOF ;

// no bye usei um método de impressao de ID a ID.
bye       : 'bye' { System.out.print("Goodbye:"); }   (ID {System.out.print(" " + $ID.text);})+ {
  System.out.println("");
};

// no greetings usei o método do returns.
// para isso criei uma regra chamada de "fullName".
greetings : 'hello' fullName {
  System.out.println("Ola " + $fullName.list);
};

fullName returns[String list = ""]: (ID {
  $list = $list + ($list.isEmpty() ? "" : ", ") + $ID.text; }
)+ ;

ID : [A-Za-z]+ ;
WS: [ \t\r\n]+ -> skip ;
