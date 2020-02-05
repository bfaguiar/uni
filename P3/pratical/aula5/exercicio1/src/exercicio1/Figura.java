package exercicio1;

public abstract class Figura implements Comparable <Figura> {
	
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
	
	public int compareTo(Figura f) {
		if (f == null) 
			throw new NullPointerException("...");
		return (int) (area()-f.area());
	}
}
