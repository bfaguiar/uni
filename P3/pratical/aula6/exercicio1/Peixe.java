package Aula06.Ex01;

public class Peixe extends Comida{
	private TipoPeixe peixe;
	public Peixe(TipoPeixe peixe, double proteinas, double calorias, double peso) {
		super(proteinas, calorias, peso);
		this.peixe=peixe;
		// TODO Auto-generated constructor stub
	}

	public String toString() {
		return "Peixe " + peixe + ", Proteinas " + getProt() + ", Calorias " + getCal() + ", Peso "
				+ getPeso();
	}
	
}
