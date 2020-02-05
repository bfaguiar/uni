package exercicio1;

public class Professor extends Pessoa {
	
	private int nfunc;
	private int dataAdmissao;
	
	public Professor(String nome, int cc, Data dataNasc, int nfunc, int dataAdmissao) {
		
		super(nome, cc, dataNasc);
		this.nfunc = nfunc;
		this.dataAdmissao = dataAdmissao;
	}

	public int getNfunc() {
		return nfunc;
	}

	public int getDataAdmissao() {
		return dataAdmissao;
	}
	
	
	
}
