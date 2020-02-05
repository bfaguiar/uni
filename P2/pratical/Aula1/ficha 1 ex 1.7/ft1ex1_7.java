import java.util.*;
import java.io.*;

public class ft1ex1_7 {
	
	static String nome1 = new String();
	static String nome2 = new String();
	static Scanner in = new Scanner(System.in);
	
	public static void main (String args[]) throws IOException {
		if(args.length!=2) {
			System.out.println("n de argumentos deve ser igual a 2");
			System.exit(-1);
		}
		String nome1 = args[0];
		String nome2 = args[1];
		
		
		
		// FICHEIRO 1
		
		File fich1; // DECLARAR ANTES PARA AO METER BEM, NÃO REPETIR
		
	//	do {
			
		//	System.out.print("Insira o nome do primeiro ficheiro: ");
		//	nome1 = in.nextLine();
		fich1 = new File(nome1);
		
			if (!fich1.exists()) {
				System.out.println("ERRO: o ficheiro " + nome1 + " nao existe!"); }
		
	//} // while (!fich1.exists());
		
		
		// FICHEIRO 2
		
		File fich2;  // DECLARAR ANTES PARA AO METER BEM, NÃO REPETIR
		
		// do {
			
		// System.out.print("Insira o nome do segundo ficheiro: ");
		// nome2 = in.nextLine();
		fich2 = new File(nome2);
		
		if (!fich2.exists()) {
			System.out.println("ERRO: o ficheiro " + nome2 + " nao existe!"); }
			
		// } while (!fich2.exists());
		
		
		
		// SCANNERES PARA FICHEIROS
		
		Scanner scanfich1 = new Scanner (fich1);
		
		PrintWriter cp = new PrintWriter(fich2);
		
		// LER FICHEIRO 1
		
		while (scanfich1.hasNextLine()) {
			String line1 = scanfich1.nextLine();
			cp.println(line1);
			System.out.println(line1);
		}
		
		
		System.out.print("Ficheiro Copiado Com Sucesso!");
			
		scanfich1.close();
		cp.close();
	
}
}

