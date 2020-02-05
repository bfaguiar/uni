package aula1;
import java.util.*;

public class ProgPrincipal {

	static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
	
	String frase;
	
	System.out.print("Escreva uma frase: ");
	frase = sc.nextLine();
	
	ProgMethods obj = new ProgMethods(frase);
	

	obj.countChar(frase);
	
	if(obj.isLowerString(frase)) {
		System.out.printf("Só ha letras minusculas.\n");
	} else if (obj.isUpperString(frase)) {
		System.out.printf("Existem apenas letras maiusculas\n");
	}
	obj.isUpperString(frase);
	obj.printTotalPalavras(frase);
	obj.invertPalavras(frase);
	}

}
