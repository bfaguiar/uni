package ex1;

public class estudante {
	
	private int nmec;
	private String curso;
	private cliente clienteEstudante;
	
	estudante(int nmec, String curso, cliente clienteEstudante) { 
		this.nmec = nmec;
		this.curso = curso;
		this.clienteEstudante = clienteEstudante;
	}
	
	int nmec() { return nmec; }
	String curso() { return curso; }
	cliente clienteEstudante() { return clienteEstudante; }
	
}
