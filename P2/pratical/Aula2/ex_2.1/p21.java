/*************************************************************************
 * Compilation: javac j21.java 
 * Execution: java j21
 *************************************************************************/
import java.util.*;

public class p21 {
	// Exemplo simples de utilização da class Complex
	
	static Scanner in = new Scanner(System.in);
	
	public static void main(String[] args) {
	
		
		double re, im;

		
		// Consola
		if (args.length <2) {
			System.out.print("Re: ");
			re = in.nextDouble();
		
			System.out.print("Im: ");
			im = in.nextDouble();
		
		} else {
			re = Double.parseDouble(args[0]);
			im = Double.parseDouble(args[1]);
		}
		
		Complexo a = new Complexo(re, im);


		// Vamos usar métodos de 'a'
		System.out.println("(" + a.real() + " + " + a.imag() + "i)");
		System.out.println("  parte real = " + a.real());
		System.out.println("  parte imaginaria = " + a.imag());
		System.out.println("  modulo = " + a.abs());
		System.out.printf("  fase   =  %2.2f\n", a.phase());
	}

}
