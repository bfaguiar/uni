package Aula03.Ex2;

public class CirculoHeran�a extends FiguraHeran�a {
	private double raio;

	public CirculoHeran�a(int x, int y, double raio) {
		super(x, y);
		this.raio=raio;
		
		// TODO Auto-generated constructor stub
	}
	
	public CirculoHeran�a(double raio){
		super(null);
		this.raio=raio;
	}
	
	public CirculoHeran�a(CirculoHeran�a coiso){
		super(coiso.getPonto());
		this.raio=coiso.raio();
	}
	
	public double raio(){
		return raio;
	}
	
	public double area(){
		return Math.PI*Math.pow(raio, 2);
	}
	
	public double perimetro(){
		return 2*Math.PI*raio;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		CirculoHeran�a other = (CirculoHeran�a) obj;
		if (getPonto() == null) {
			if (other.getPonto() != null)
				return false;
			} else if (!getPonto().equals(other.getPonto()))
				return false;
			if (raio != other.raio)
				return false;
			return true;
	}
}
