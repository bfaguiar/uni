import java.io.*;
import java.util.*;

public class ex2guiao5 {
	
	public static void main (String args[])// throws IOException >>> antes
    {
		String nomeficheiro1 = args[0];
		String nomeficheiro2 = args[1];
		
	try {
			File ficheiro1 = new File(nomeficheiro1);
			File ficheiro2 = new File(nomeficheiro2);
			
			Scanner fin = new Scanner(ficheiro1);
			PrintWriter pwf = new PrintWriter(ficheiro2);
			
			while(fin.hasNextLine()) {
				String s = fin.nextLine();
				System.out.print(s);
				 pwf.println(s);
				
			}
			fin.close();
			pwf.close();
		
		} catch (IOException e) {
			System.out.println ("Erro na leitura do Ficheiro.\n" + e.getMessage()); // "getMessage" lê erro e imprime erro.
		}
	}
}

// fazer em casa
//  
//          Exception
//			|   |	| 
//			|   |	|
//  IOException
//  |	|	|
//	|   |	|
