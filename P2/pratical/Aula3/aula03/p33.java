import static java.lang.System.*;
import lib.*;

public class p33
{
   public static void main(String[] args)
   {
      Nota[] notas = new Nota[args.length / 7]; // argumentos em grupos de sete (data-inicio data-fim texto)
      for(int i = 0; i < notas.length; i++)
      {
         int dia, mes, ano;
		 dia = Integer.parseInt(args[i*7]);	
         assert (dia > 0);
         mes = Integer.parseInt(args[i*7+1]);
         assert (mes > 0 && mes <=12);
         ano = Integer.parseInt(args[i*7+2]);
         assert (Data.diasDoMesAno(mes,ano)>= dia);
         Data inicio = new Data(dia, mes, ano);
         assert (Data.dataValida(inicio));
         dia = Integer.parseInt(args[i*7+3]);
         assert (dia > 0);
         mes = Integer.parseInt(args[i*7+4]);
         assert (mes > 0 && mes <=12);
         ano = Integer.parseInt(args[i*7+5]);
         assert (Data.diasDoMesAno(mes,ano)>= dia);
         Data fim = new Data(dia, mes, ano);
         assert (Data.dataValida(fim));
         assert (inicio.menorDoQue(fim));
         String texto = args[i*7+6]; // nota por exemplo, escrever "estudar CII" 
         assert (!(texto.compareTo("")==0));
         notas[i] = new Nota(inicio, fim, texto);
      }
      for(int i = 0; i < notas.length; i++)
         notas[i].escreve();
   }
}

