package exercicio1;

public class Ponto {
	private double x;
	private double y;
	
	public Ponto(double x, double y){
		this.x=x;
		this.y=y;
	}

	@Override
	public String toString() {
		return "[x=" + x + ", y=" + y + "]";
	}
	
	

}