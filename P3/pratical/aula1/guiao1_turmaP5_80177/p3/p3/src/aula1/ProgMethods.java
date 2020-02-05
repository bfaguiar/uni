package aula1;

import java.util.Arrays;

public class ProgMethods {
	
	private String aux;
	
	public ProgMethods(String aux){ this.aux = aux; }
	
	public String aux(){ return aux; }
	
	public void countChar(String aux) {
		
		int i = 0;
				
		for (int j = 0; j < aux.length(); j++){
			
			char b = aux.charAt(j);
			
			if (Character.isDigit(b)) {
				i++;
			}
		}
		System.out.println("total de numeros: " +i);
	}
	
	public boolean isLowerString(String aux) {
		
		for (int j = 0; j < aux.length(); j++){
			
			char b = aux.charAt(j);
			
			if (Character.isUpperCase(b)) {
				
				return false;
				
			}
			
		} return true;
	}
	
	public boolean isUpperString(String aux) {
		
		for (int j = 0; j < aux.length(); j++){
			
			char b = aux.charAt(j);
			
			if (Character.isLowerCase(b)) {
				
				return false;
				
			}
			
		} return true;
	}
	
	public void printTotalPalavras(String aux) {

		
		
		String[] palavra = aux.split(" ");
		int count = palavra.length;
		
		for (int j = 0; j < palavra.length; j++){
			
			for (int i = 0; i < palavra[j].length(); i++) {

				char b = palavra[j].charAt(i);
				
				if (Character.isDigit(b)) {
					break;
				} else {
					
				}
			}
		}
		System.out.println("Palavras: " + Arrays.toString(palavra));
		System.out.println("Numero de palavras:  " + count);
	}
	
	public void invertPalavras(String aux) {
		
		String[] palavra = aux.split(" ");
		int count = palavra.length;
		
		for (int i = 0; i < count; i++) {
			for (int j = 0; j < palavra[i].length(); j=j+2) {
				System.out.printf("%d%d\n", palavra[i].charAt(j), palavra[i].charAt(i+1));
			}
		}
	}
}
