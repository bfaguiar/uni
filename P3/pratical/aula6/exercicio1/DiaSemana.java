package Aula06.Ex01;

public enum DiaSemana {
	Domingo, Segunda, Ter�a, Quarta, Quinta, Sexta, S�bado;
	
	public static DiaSemana rand(){
		 switch ((int) (Math.random() * 7)) {
		   default:
			   case 0:
				   return DiaSemana.Domingo;
			   case 1:     
				   return DiaSemana.Segunda;   
			   case 2:     
				   return DiaSemana.Ter�a;
			   case 3:     
				   return DiaSemana.Quarta;
			   case 4:
				   return DiaSemana.Quinta;
			   case 5:
				   return DiaSemana.Sexta;
			   case 6:
				   return DiaSemana.S�bado;
		 }  
	}
}


