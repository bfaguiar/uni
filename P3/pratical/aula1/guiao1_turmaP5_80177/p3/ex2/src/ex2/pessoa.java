package ex2;

public class pessoa {
	private String nome;
	private int cc;
	private data dataNasc;
	
	public pessoa(String nome, int cc, data dataNasc) {
		this.nome = nome;
		this.cc = cc;
		this.dataNasc = dataNasc;	
	}
	
	public String nome(){
		return nome;
	}
	
	public int cc() {
		return cc;
	}
	
	public data dataNasc() {
		return dataNasc;
	}

}
