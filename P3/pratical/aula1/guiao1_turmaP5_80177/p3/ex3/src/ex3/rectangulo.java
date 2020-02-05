package ex3;

public class rectangulo {
	
	private double comprimento;
	private double largura;
	
	public rectangulo (double comprimento, double largura){
		this.comprimento = comprimento;
		this.largura = largura;
	}
	
	public double area (){
		double a = comprimento*largura;
		return a;
	}
	
	public double perimetro(){
		double p = 2*comprimento + 2*largura;
		return p;
	}
	
	public String toString(){
		String str = "comprimento: " + comprimento + ", largura: " + largura + ", perimetro: " + perimetro() + ", area: " + area() + ".";  
		return str;
	}
}
