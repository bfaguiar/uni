package exercicio1;

public class Test {
	

	public static void main(String[] args) {
		
		Estudante est = new Estudante ("Andreia", 9855678, new Data(18, 7, 1974));
		Bolseiro bls = new Bolseiro ("Maria", 8976543, new Data(11, 5, 1976));
		bls.setBolsa(745);
			
		System.out.printf("Estudante: " + est.nome());
		System.out.println(est);
		System.out.println("Bolseiro:" + bls.nome() + ", NMec: " + bls.nmec() + ", Bolsa:" + bls.getBolsa());
		System.out.println(bls);
		
	}

}
