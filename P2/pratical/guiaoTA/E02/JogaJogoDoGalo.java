import static java.lang.System.*;
import java.util.Scanner;
import jogos.*;
    
public class JogaJogoDoGalo {
  public static void main(String[] args) {
    Scanner sin = new Scanner(in);
    char jogador1 = 'X';
    char jogador2 = 'O';
    JogoDoGalo jogo = new JogoDoGalo(jogador1, jogador2);
    int lin, col;
    jogo.mostraTabuleiro();
    while (!jogo.terminado()) {
      try {
      out.print("(lin col): ");
      lin = sin.nextInt();
      col = sin.nextInt();
      jogo.jogada(lin, col);
      jogo.mostraTabuleiro();
		} catch (AssertionError e) {
			out.println("ERRO: insira uma lin col diferente.");
		}
    }
    out.println();
    if (jogo.ultimoJogadorGanhou())
      out.println("Jogador "+jogo.ultimoJogador()+" ganhou!");
    else
      out.println("Jogo empatado!");
  }
}
