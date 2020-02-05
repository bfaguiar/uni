
import static java.lang.System.*;
import java.io.*;


public class TestSocialNetwork
{

   public static void main(String[] args)
   {
      String[] names = { "Joao","Anna","Nuno","Luis","Carlos",
                         "Antonio","Jose","Susana","Rosa","Odete",
                         "Amelia","Mario","Afonso","Leonor",
                         "Irene" };
      String[] professions = 
                       { "medico","engenheiro","professor",
                         "decorador","enfermeiro","juiz", "actor",
                         "carpinteiro","politico","padeiro",
                         "cabeleireiro","pastor","agricultor" };
      SocialNetwork sn = new SocialNetwork(10,4);

      out.println("sn.numMembers()=" + sn.numMembers());
      for(int i=0; i<names.length; i++) {
         int y = 1995-myRandom(35);
         String prof = professions[myRandom(professions.length)];
         sn.addMember(new Person(names[i],y,prof));
      }
      out.println("sn.numMembers()=" + sn.numMembers());
	out.println(sn.getPerson(13).name());
	try {
		Integer.parseInt("a");
		out.println(sn.getPerson(15).name());
	} catch (NullPointerException e) {
			out.println("ERRO: posicai invalida");
	}  
   
   }

   /**
    * Retorna um número aleatório entre 0 e n-1.
    */
   static int myRandom(int n) {
      return (int)(Math.random()*n);
   }
}


