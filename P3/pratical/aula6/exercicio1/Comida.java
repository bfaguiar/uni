package Aula06.Ex01;

public class Comida {
	private double proteinas, calorias, peso;
	
	public Comida(double proteinas, double calorias, double peso){
		this.proteinas=proteinas;
		this.calorias=calorias;
		this.peso=peso;
	}
	
	public double getProt(){
		double aux = (100*proteinas)/peso;
		return aux;
	}
	
	public double getCal(){
		double aux = (100*calorias)/peso;
		return aux;
	}
	
	public double getPeso(){
		return peso;
	}
	
	public double calorias(){
		return calorias;
	}
}
