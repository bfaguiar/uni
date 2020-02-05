package Aula02.Ex2;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class SopaDeLetras {
	static Scanner sc = new Scanner(System.in);
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		String ficheiro = sc.nextLine();
		verificaçao(ficheiro);
		File fin = new File(ficheiro);
		Scanner reader = new Scanner(fin);
		String linha = reader.nextLine();
		int x=linha.length();
		int y=x;
		reader.close();
		creator(ficheiro, x, y);
		searchKeyWords(ficheiro);
		
	}	
		
	public static void creator(String ficheiro, int x, int y) throws IOException {
		Scanner readerNovo = new Scanner(ficheiro);//De forma a poder voltar a ler o ficheiro do inicio
		char[][]matriz = new char [x][y];
		String aux;
		for(int i=0; i<x; i++){
			aux=readerNovo.nextLine();
			for(int j=0; j<aux.length(); j++){
				matriz[i][j]=aux.charAt(j);
			}
		}
		readerNovo.close();
	}
	
	public static void searchKeyWords(String ficheiro) throws IOException {
		Scanner readerAgain = new Scanner(ficheiro);//De forma a poder voltar a ler o ficheiro do inicio, mais uma vez
		String words = readerAgain.nextLine();
		String[] divisao = words.split(", ");
		readerAgain.close();
	}
	
	public static void searchTheWords(String ficheiro, int x, int y){
		Scanner lastReader = new Scanner(ficheiro);
		
	}
	
	
	public static void verificaçao(String ficheiro){
		File fin = new File(ficheiro);
		if(!fin.exists()){ 
			System.out.println("ERROR: input file " + ficheiro+ " does not exist!"); 
			System.exit(2);             
		} 
		if(fin.isDirectory()){ 
			System.out.println("ERROR: input file " + ficheiro+ " is a directory!"); 
			System.exit(3);
		} 
		if(!fin.canRead()){ 
			System.out.println("ERROR: cannot read from input file " + ficheiro+ "!"); 
			System.exit(4);             
		}
	}

}
/*Não conseguimos resolver o segundo exercicio, pelo que foi simplesmente enviado assim
  Se entretanto conseguirmos chegar a sua resulução enviaremos novamente com um apontamento a explicar novamente a situação.*/
