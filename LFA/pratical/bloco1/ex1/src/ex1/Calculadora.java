package ex1;

import java.util.Scanner;
import static java.lang.System.*;


public class Calculadora {

	static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
			
		try {
			String line = sc.nextLine();
			String[] lineSplitted = line.split(" ");
			double num1 = Double.parseDouble(lineSplitted[0]);
			double num2 = Double.parseDouble(lineSplitted[2]);
			String op   = lineSplitted[1];
			
			double result;
			
			
			switch (op) {
	
					case "+":
						result = num1 + num2;
						out.println("" + num1 + " " + op + " " + num2 + " = " + result);
					break;
					
					case "-":
						result = num1 - num2;
						out.println("" + num1 + " " + op + " " + num2 + " = " + result);
					break;
					
					case "/":
						result = num1 / num2;
						out.println("" + num1 + " " + op + " " + num2 + " = " + result);
					break;
					
					case "*":
						result = num1 * num2;
						out.println("" + num1 + " " + op + " " + num2 + " = " + result);
					break;
	
					default:
							out.println("ERRO: operador nao conhecido.");
						break;
					
					}
			
			} catch(ArrayIndexOutOfBoundsException e) {
				out.println("EXPERIMENTE:  <numero> <operador> <numero>");
			}
			
	}

}
