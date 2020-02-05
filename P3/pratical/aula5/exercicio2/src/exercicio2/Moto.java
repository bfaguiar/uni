package exercicio2;

public class Moto extends Veiculo implements Motorizado {
	
	private int potencia, consumo, combustivel;
	
	public Moto(String cor, int ano, int velocidadeMaxima, int matricula, int cilindrada, int potencia, int consumo, int combustivel) {
		super(cor, ano, velocidadeMaxima, matricula, cilindrada);
		this.potencia = potencia;
		this.consumo = consumo;
		this.combustivel = combustivel;
		// TODO Auto-generated constructor stub
	}

	@Override
	public int getNRodas() {
		// TODO Auto-generated method stub
		return 2;
	}

	@Override
	public String getCor() {
		// TODO Auto-generated method stub
		return cor;
	}

	@Override
	public int getAno() {
		// TODO Auto-generated method stub
		return ano;
	}

	@Override
	public int getVelocidadeMaxima() {
		// TODO Auto-generated method stub
		return velocidadeMaxima;
	}

	@Override
	public int matricula() {
		// TODO Auto-generated method stub
		return matricula;
	}

	@Override
	public int cilindrada() {
		// TODO Auto-generated method stub
		return cilindrada;
	}

	@Override
	public int getPotencia() {
		// TODO Auto-generated method stub
		return potencia;
	}

	@Override
	public int getConsumo() {
		// TODO Auto-generated method stub
		return consumo;
	}

	@Override
	public int getCombustivel() {
		// TODO Auto-generated method stub
		return combustivel;
	}

	@Override
	public String toString() {
		return "Moto [potencia=" + potencia + ", consumo=" + consumo + ", combustivel=" + combustivel + ", nRodas="
				+ nRodas + ", cor=" + cor + ", ano=" + ano + ", velocidadeMaxima=" + velocidadeMaxima + ", matricula="
				+ matricula + ", cilindrada=" + cilindrada + "]";
	}
	
	

}
