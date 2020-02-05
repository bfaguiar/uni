package Aula06.Ex01;

public class Carne extends Comida {
	private VariedadeCarne carne;
	public Carne(VariedadeCarne carne, double proteinas, double calorias, double peso) {
		super(proteinas, calorias, peso);
		this.carne=carne;
		// TODO Auto-generated constructor stub
	}
	
	public String toString() {
		return "Carne " + carne + ", Proteinas " + getProt() + ", Calorias " + getCal() + ", Peso "
				+ getPeso();
	}
	
}

	