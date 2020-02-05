package exercicio4;

public class estudante extends cliente{
	
	private int nmec;
	private String curso;
	
	estudante(data dataInscricao, String nome, int cc, data dataNascimento, int nmec, String curso) { 
		super(dataInscricao, nome, cc, dataNascimento);
		this.nmec = nmec;
		this.curso = curso;
	}
	
	int nmec() { return nmec; }
	String curso() { return curso; }
}
