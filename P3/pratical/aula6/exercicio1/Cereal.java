package Aula06.Ex01;

public class Cereal extends Comida implements Vegetariano{
	private String nome;
	public Cereal(String nome, double proteinas, double calorias, double peso) {
		super(proteinas, calorias, peso);
		this.nome=nome;
		// TODO Auto-generated constructor stub
	}
	
	public String toString() {
		return "Cereal " + nome + ", Proteinas " + getProt() + ", Calorias " + getCal() + ", Peso "
				+ getPeso();
	}
	
}
