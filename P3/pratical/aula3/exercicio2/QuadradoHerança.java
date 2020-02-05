package Aula03.Ex2;

public class QuadradoHerança extends FiguraHerança {
	private double lado;
	
	public QuadradoHerança(int x, int y, double lado){
		super(x, y);
		this.lado=lado;
		// TODO Auto-generated constructor stub
	}
	
	public QuadradoHerança(double lado){
		super(null);
		this.lado=lado;
	}
	
	public QuadradoHerança(QuadradoHerança coiso){
		super(coiso.getPonto());
		this.lado=coiso.lado();
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		QuadradoHerança other = (QuadradoHerança) obj;
		if (getPonto() == null) {
			if (other.getPonto() != null)
				return false;
			} else if (!getPonto().equals(other.getPonto()))
				return false;
		if (lado != other.lado)
			return false;
		return true;
	}

	public double lado(){
		return lado;
	}
	
	public double area(){
		return lado*lado;
	}
	
	public double perimetro(){
		return 4*lado;
	}
}
