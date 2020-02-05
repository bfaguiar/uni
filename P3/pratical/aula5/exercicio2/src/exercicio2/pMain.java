package exercicio2;
import static java.lang.System.out;

public class pMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Automovel a1 = new Automovel("Branco", 2010, 250, 123, 100, 900, 2, 4);
		Bicicleta b1 = new Bicicleta("Azul", 2002, 20, 145, 0);
		CarroPolicia cp1 = new CarroPolicia("Azul e Branco", 2015, 300, 021, 120, 1000, 2, 4, tipo.GNR);
		Moto m1 = new Moto("Vermelha", 2001, 150, 234, 45, 56, 56, 100);
		MotoPolicia mp1 = new MotoPolicia("Azul e Branca", 2016, 400, 234, 2345, 2345, 2345, 234, tipo.PSP);
		
		out.println(a1);
		out.println(b1);
		out.println(cp1);
		out.println(m1);
		out.println(mp1);
		
		Automovel a2 = new CarroPolicia("Vermelho", 2016, 300, 021, 120, 1000, 2, 4, tipo.Bombeiros);
		Automovel[] arrAuto = new Automovel[3];
		arrAuto[0] = a1;
		arrAuto[1] = cp1;
		arrAuto[2] = a2;
		out.println(a2);
		
		out.println("\nCarro com mais anos: " + UtilCompare.findMax(arrAuto) );
		
	}

}
