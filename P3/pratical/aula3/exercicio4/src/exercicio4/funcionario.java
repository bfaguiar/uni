package exercicio4;

public class funcionario extends cliente{
	
	private int nFiscal;
	
	funcionario(data dataInscricao, String nome, int cc, data dataNascimento, int nFiscal) { 
	super(dataInscricao, nome, cc, dataNascimento);
	this.nFiscal = nFiscal;
}

int nFiscal() { return nFiscal; }
}
