package Aula03.Ex2;

public class RetanguloHerança extends FiguraHerança {
	private double comprimento;
	private double largura;

	public RetanguloHerança(int x, int y, double comprimento, double largura) {
		super(x, y);
		this.comprimento=comprimento;
		this.largura=largura;
		// TODO Auto-generated constructor stub
	}
	
	public RetanguloHerança(double comprimento, double largura){
		super(null);
		this.comprimento=comprimento;
		this.largura=largura;
	}
	
	public RetanguloHerança(RetanguloHerança coiso){
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
		RetanguloHerança other = (RetanguloHerança) obj;
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

}
