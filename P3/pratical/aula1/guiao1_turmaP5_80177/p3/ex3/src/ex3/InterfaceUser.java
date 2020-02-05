package ex3;
import java.util.Scanner;

public class InterfaceUser {
	
	static Scanner in = new Scanner(System.in) ;
	
	public static void main(String[] args) {
		
	
		int opcao;
		
		do{		
			System.out.printf("\n\n1-Circulo\n2-Quadrado\n3-Rectangulo\n4-Comparar dois circulos\nOpçao: ");
			opcao = in.nextInt();
			
			switch(opcao){
			 	case 1:
			 		 System.out.print("coordenadas do centro x:");
					 double x = in.nextDouble();
					 
					 System.out.print("y:");
					 double y = in.nextDouble();
					
					 System.out.print("raio:");
					 double z = in.nextDouble();
					 circulo circ = new circulo(x,y,z);
					 
					 System.out.print(circ.toString());
					 break;
				 
			 	case 2:
					 System.out.print("Lado:");
					 double lado = in.nextDouble();
					 
					 quadrado quad = new quadrado(lado);
					
					 System.out.print(quad.toString());
					 break;
				 
			 	case 3:
					 System.out.print("Comprimento:");
					 double comprimento = in.nextDouble();
					 
					 System.out.print("Largura:");
					 double largura  = in.nextDouble();
					 
					 rectangulo rect = new rectangulo (comprimento, largura);
					 
					 System.out.print(rect.toString());
					 break;
				 
			 	case 4:
					 System.out.print("CIRCULO 1. Coordenadas do centro. x:");
					 double x1= in.nextDouble();
					 
					 System.out.print("y:");
					 double y1 = in.nextDouble();
					
					 System.out.print("Raio:");
					 double z1 = in.nextDouble();
					 
					 circulo circulo1 = new circulo(x1,y1,z1);
					 
					 System.out.print("CIRCULO 2.Coordenadas do centro. x:");
					 double x2= in.nextDouble();
					 
					 System.out.print("y:");
					 double y2 = in.nextDouble();
					 
					 System.out.print("Raio:");
					 double z2 = in.nextDouble();
					 
					 circulo circulo2 = new circulo(x2,y2,z2);
					 circulo1.comparacao(circulo2);
					 break;
			 }
		
		}while(!(opcao >= 5));

	}
}