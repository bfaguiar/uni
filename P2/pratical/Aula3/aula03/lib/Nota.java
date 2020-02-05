package lib;

public class Nota {
	
	private Data inicio, fim;
	private String texto;
		
	
	
	public Nota (Data inicio, Data fim, String texto) {
	
	this.texto = texto;
	this.inicio = inicio;
	this.fim = fim;
	
	}
	
	public Data inicio() {
	
	return inicio;
	}
	
	public Data fim() {
		
	return fim;
	}
	
	public String texto() {
	
	return texto;
	}
	
	public void escreve() {
		inicio.print();
		fim.print();
		System.out.println(texto);
	}
}

