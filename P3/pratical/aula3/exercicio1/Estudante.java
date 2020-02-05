package exercicio1;

public class Estudante extends Pessoa{
	
	private static int count = 100; //variavel static para começar todos em 100
	private final int nmec; // para nao alterar o valor do nmec
	private Data dataInsc;
	
	public Estudante(Data dataInsc, String nome, int cc, Data dataNasc)  {

		super(nome, cc, dataNasc);
		this.dataInsc = dataInsc;
		nmec = count++; // gera o nmec sempre que construir um estudante
		
	}
	
	public Estudante(String nome, int cc, Data dataNasc)  {

		super(nome, cc, dataNasc);
		dataInsc = new Data(30, 9, 2016);
		nmec = count++;
	}


	public int nmec() { return nmec; }
	public Data dataNasc() { return dataInsc; }

	@Override
	public String toString() {
		return "Estudante [nmec=" + nmec + ", dataInsc=" + dataInsc + ", nome()=" + nome() + ", cc()=" + cc() + "]";
	}
	
	
	
}
