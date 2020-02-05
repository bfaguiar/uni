package exercicio2;

public abstract class Figura {
	
	private Ponto ponto;
	
	public Figura(int x, int y){
		ponto = new Ponto (x,y);
	}

	public Figura(Ponto ponto){
		this.ponto=ponto;
		// TODO Auto-generated constructor stub
	}
	
	public abstract double area();
	
	public abstract double perimetro();
	
	
	public Ponto getPonto(){
		return ponto; 
	}
}
