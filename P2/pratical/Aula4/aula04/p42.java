import java.util.*;

public class p42 {
	
	static Scanner in = new Scanner(System.in);
	public static void main (String args[]) {
	 
	 int min;
	 int max;
	 String comando;
	 
	 if (args.length == 2) {
	 min = Integer.parseInt(args[0]);
	 assert (min > 0 );
	 max = Integer.parseInt(args[1]);
	 assert (max > 0 );
	 assert (min < max );
	
	} else { 
		min = 0;
		max = 20;
		
		
	GuessGame game = new GuessGame(min, max);
	assert !game.finished();
	assert game.min() == min;
    assert game.max() == max;
    assert game.numAttempts() == 0;
    assert !game.validAttempt(min-1) && !game.validAttempt(max + 1);
    System.out.printf("\n%d\n", game.secretNumber);
	do {
	 System.out.println("#######################################");
     System.out.println("###                                 ###");
	 System.out.println("###   JOGO ADIVINHA - GUESS GAME    ###");
	 System.out.println("###                                 ###");
	 System.out.println("#######################################");
     System.out.println("");
     System.out.println("");
	 System.out.println("Comandos Validos:  ");
	 System.out.printf("<numero> (intervalo configurado para [%d, %d]\n", min, max);
	 System.out.println("Contar tentativas inseridas");
     System.out.println("Ajuda");   
     System.out.println("Sair");
     System.out.print("Comando:  ");
     comando = in.nextLine();
     System.out.println("");
     System.out.println("");
     System.out.println("");
     System.out.println("");
     switch (comando) {
		case "<numero>" :
			if(!game.finished()){
				int num;
				do{
					try{
						System.out.println("Insira um numero dentro do intervalo indicado: ");
							String aux = in.nextLine();
							num = Integer.parseInt(aux);
							game.play(num);
							if(game.finished()){
								System.out.printf("\nParabens: acertou! O número era %d\n", game.secretNumber);
							}
						} catch (NumberFormatException f) {
								System.out.println("ERRO: digite um numero valido");
								num = min-1;
							}
				} while (!game.validAttempt(num));
						
			}
			break;
			
			case "Contar tentativas inseridas" : 
				System.out.printf("%d tentativas inseridas\n\n\n", game.numAttempts());
				break;
			default: break;
		}
		
		} while(!(comando.compareTo("SAIR")==0));
		
	}
}
}


