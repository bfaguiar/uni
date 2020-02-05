package exercicio1;

public class Retangulo extends Figura {
	private double comprimento;
	private double largura;

	public Retangulo(int x, int y, double comprimento, double largura) {
		super(x, y);
		this.comprimento=comprimento;
		this.largura=largura;
		// TODO Auto-generated constructor stub
	}
	
	public Retangulo(double comprimento, double largura){
		super(null);
		this.comprimento=comprimento;
		this.largura=largura;
	}
	
	public Retangulo(Retangulo coiso){
		super(coiso.getPonto());
		this.comprimento=coiso.comprimento();
		this.largura=coiso.largura();
	}
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Retangulo other = (Retangulo) obj;
		if (Double.doubleToLongBits(comprimento) != Double.doubleToLongBits(other.comprimento))
			return false;
		if (Double.doubleToLongBits(largura) != Double.doubleToLongBits(other.largura))
			return false;
		return true;
	}

	public double comprimento(){
		return comprimento;
	}
	
	public double largura(){
		return largura;
	}
	
	public double area(){
		return comprimento*largura;
	}
	
	public double perimetro(){
		return 2*comprimento+2*largura;
	}

	@Override
	public String toString() {
		return "Retangulo [comprimento=" + comprimento + ", largura=" + largura + ", Ponto=" + getPonto() + "]";
	}
	
	

}
