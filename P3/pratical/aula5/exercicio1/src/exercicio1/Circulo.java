package exercicio1;

public class Circulo extends Figura {
	private double raio;

	public Circulo(int x, int y, double raio) {
		super(x, y);
		this.raio=raio;
		
		// TODO Auto-generated constructor stub
	}
	
	public Circulo(double raio){
		super(null);
		this.raio=raio;
	}
	
	public Circulo(Circulo coiso){
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
		Circulo other = (Circulo) obj;
		if (getPonto() == null) {
			if (other.getPonto() != null)
				return false;
			} else if (!getPonto().equals(other.getPonto()))
				return false;
			if (raio != other.raio)
				return false;
			return true;
	}

	@Override
	public String toString() {
		return "Circulo [raio=" + raio + ", Centro = " + getPonto() + "]";
	}

	
	
	
}
