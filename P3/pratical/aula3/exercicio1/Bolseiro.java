package exercicio1;

public class Bolseiro extends Estudante {
	
	private int bolsa;
	
	public Bolseiro(Data dataInsc, String nome, int cc, Data dataNasc, int bolsa) {
		
		super(dataInsc, nome, cc, dataNasc);
		this.bolsa = bolsa;
		
	}
	
	public Bolseiro(String nome, int cc, Data dataNasc) {
		
		super(nome, cc, dataNasc);
		
	}
	
	public int getBolsa() { return bolsa; }

	public void setBolsa(int bolsa) { this.bolsa = bolsa; }

	@Override
	public String toString() {
		return "Bolseiro [bolsa=" + bolsa + ", nmec()=" + nmec() + ", dataNasc()=" + dataNasc() + ", nome()=" + nome()
				+ ", cc()=" + cc() + "]";
	}
	
	
	
	
	
}
