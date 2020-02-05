package ex1;

public class funcionario {
	
		private int nFiscal;
		private cliente clienteFuncionario;
		
		funcionario(int nFiscal, cliente clienteFuncionario) { 
		this.nFiscal = nFiscal;
		this.clienteFuncionario = clienteFuncionario;
	}
	
	int nFiscal() { return nFiscal; }
	cliente clienteFuncionario() { return clienteFuncionario; }
}
