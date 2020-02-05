package ex3;

public class circulo {
	
	private double raio;  
	private Ponto centro;   
	
	public circulo(double x, double y, double z){
		this.raio = z;
		Ponto centro = new Ponto (x,y);
		this.centro = centro;
	}
	public circulo(Ponto centro, double z){
		this.centro = centro;
		this.raio = z;
	}
	public double area (){
		double a = Math.PI*Math.pow(raio, 2);
		return a;
	}
	
	public double perimetro(){
		double p = 2*raio*Math.PI;
		return p;
	}
	public String toString(){
		String str = "raio: " + raio + ", diametro: " + 2*raio + ", centro: (" + centro.x + ", " + centro.y + "), Perimetro: " + perimetro() + ", Area: " + area() + ".";  
		return str;
	}
	
	public void comparacao(circulo circulo2){
		if(this.raio == circulo2.raio){
			System.out.println("Os dois circulos sao iguais");
		}else {
			System.out.println("Os dois circulos diferem");
		}
		
		double distancia= Math.pow(this.centro.x-circulo2.centro.x, 2) + Math.pow(this.centro.y-circulo2.centro.y, 2);
		if(this.raio+circulo2.raio>= distancia){
			System.out.println("Os dois circulos interceptam-se");
		}else{
			System.out.println("Os dois circulos nao se interceptam-se");
		}
		
			
		
	}
	
		
	
}
