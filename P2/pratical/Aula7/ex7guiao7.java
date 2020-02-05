// 1- ler fx e mostrar no ecra
// 2- criar e preencher 3 listas
import aula07.p2utils.LinkedList;
import java.io.*;
import java.util.Scanner;

public class ex7guiao7 {
	
	static Scanner in = new Scanner(System.in);
	public static void main (String args[]) throws IOException {
		
			// meter as 3 linkedlists 
			
			LinkedList<String> lista1 = new LinkedList<String>();
			LinkedList<String> lista2 = new LinkedList<String>();
			LinkedList<String> lista3 = new LinkedList<String>();
			
			try {
			String nomeficheiro = in.nextLine(); 
			System.out.println("-------------------------");
			File ficheiroin = new File(nomeficheiro);
		
			Scanner scannerficheiro = new Scanner(ficheiroin);
			
			
			
			while(scannerficheiro.hasNextLine()) {
				String linha = scannerficheiro.nextLine();
				if ( linha.length() < 20) {
					lista1.addFirst(linha);
				} else if (linha.length() <= 40) {
					lista2.addFirst(linha);
				} else {
					lista3.addFirst(linha);
				}
				System.out.println(linha.length()); 
				System.out.println("-------------------------");
			}
			
			scannerficheiro.close();
		
		} catch (FileNotFoundException e) {
			System.out.println("ERRO: ficheiro não encontrado!");
		}
	    // mostraR LISTA 1
	    while (lista1.size() > 0) {
			System.out.println("linha1 : " + lista1.first());
			lista1.removeFirst();
		}	
		// mostrar LISTA 2
		while (lista2.size() > 0) {
			System.out.println("linha 2 : " + lista2.first());
			lista2.removeFirst();
		}
		// mostrar LISTA 3
		while (lista3.size() > 0) {
			System.out.println("linha 3 : " + lista3.first());
			lista3.removeFirst();
		}
	}
}

