package ex1;

public class emprestimo {
	
	private cliente cl;
	private video vi;
	
	emprestimo(cliente cl, video vi) {
		this.cl = cl;
		this.vi = vi;
	}
	
	cliente cl() { return cl; }
	video vi() { return vi; }
	
	void getEmprestimo(emprestimo objEmp) {
		System.out.println("");
		System.out.println("NOME DO VIDEO EMPRESTADO: " + objEmp.vi.titulo());
		System.out.println("NOME DO CLIENTE QUE O REQUESITOU: " + objEmp.cl.nome());
		
	}

}
