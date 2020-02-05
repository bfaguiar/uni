package exercicio3;

public class cliente {
	
	private data dataInscricao;
	private String nome;
	private int cc;
	private data dataNascimento;
	
	cliente(data dataInscricao, String nome, int cc, data dataNascimento) {
		this.dataInscricao = dataInscricao;
		this.nome = nome;
		this.cc = cc;
		this.dataNascimento = dataNascimento;
		
	}
	
	data dataInscricao() { return dataInscricao; }
	String nome() { return nome; }
	int cc() { return cc; }
	data dataNascimento() { return dataNascimento; }
	
	
	
	void listar(int ID) {
		System.out.printf("%d - %s\n", ID+1, this.nome);
	}
	
	void printCliente(cliente cAux) {
		System.out.println("");
		System.out.println("NOME: " + cAux.nome);
		System.out.println("CC: " + cc);
		System.out.println("DATA NASCIMENTO: " + cAux.dataNascimento.dia() + "/" + cAux.dataNascimento.mes() + "/" + cAux.dataNascimento.ano());
		System.out.println("DATA INSCRICAO: " + cAux.dataInscricao.dia() + "/" + cAux.dataInscricao.mes() + "/" + cAux.dataInscricao.ano());
	}
}
