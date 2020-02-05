import pt.ua.prog2.Contacto;
import java.util.*;

public class p22
{
	static  Scanner in = new Scanner(System.in);


   public static void main(String[] args)
   {
	   Contacto[] cl = new Contacto [2]; 
	 // cl[0] = new Contacto(Contacto.nome", "978676760");
     //  cl[1] = new Contacto("Rita", "867367834", "rita@gmail.com");
     //  cl[2] = new Contacto("Paulo", "897476388", "paulo@hotmail.com");
     //  cl[3] = new Contacto("Carlos", "674767867");
      
	   for (int j = 0; j < cl.length; j++) {
	   System.out.print("Insira um nome para o contacto: ");
	   String nome  = in.nextLine();
	   
	   System.out.print("Insira um numero de telemovel para o contacto: ");
	   String telemovel  = in.nextLine();
	   
	   System.out.print("Insira um email para o contacto: ");
	   String eMail = in.nextLine();
	   

     cl[j] = new Contacto(nome, telemovel, eMail);
	}
     
      for (int i = 0; i < cl.length; i++)
      {
         System.out.println("Nome: " +  cl[i].nome() + " ; Telemovel: " + cl[i].telefone() + 
          " ; E-Mail: " + cl[i].eMail());
          
      }
      Contacto.print();
      
   }
}
