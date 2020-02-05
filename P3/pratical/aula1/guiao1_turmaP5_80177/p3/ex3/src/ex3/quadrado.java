package ex3;

public class quadrado {
	
	private double lado;
	
	public quadrado(double lado){
		this.lado = lado;
	}
	
	public double area (){
		double area = lado*lado;
		return area;
	}
	
	public double perimetro(){
		double per = 4*lado;
		return per;
	}
	
	public String toString(){
		String str = "lado: " + lado + ", perimetro: " + perimetro() + ", area: " + area() + ".";  
		return str;
	}
}
