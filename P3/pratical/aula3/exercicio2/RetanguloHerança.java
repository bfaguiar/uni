package Aula03.Ex2;

public class RetanguloHeranša extends FiguraHeranša {
	private double comprimento;
	private double largura;

	public RetanguloHeranša(int x, int y, double comprimento, double largura) {
		super(x, y);
		this.comprimento=comprimento;
		this.largura=largura;
		// TODO Auto-generated constructor stub
	}
	
	public RetanguloHeranša(double comprimento, double largura){
		super(null);
		this.comprimento=comprimento;
		this.largura=largura;
	}
	
	public RetanguloHeranša(RetanguloHeranša coiso){
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
		RetanguloHeranša other = (RetanguloHeranša) obj;
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
