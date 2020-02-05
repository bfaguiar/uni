package exercicio2;

public class Bicicleta extends Veiculo {

	public Bicicleta(String cor, int ano, int velocidadeMaxima, int matricula, int cilindrada) {
		super(cor, ano, velocidadeMaxima, matricula, cilindrada);
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
		return 0;
	}

	@Override
	public String toString() {
		return "Bicicleta [nRodas=" + nRodas + ", cor=" + cor + ", ano=" + ano + ", velocidadeMaxima="
				+ velocidadeMaxima + ", matricula=" + matricula + ", cilindrada=" + cilindrada + "]";
	}
	
	
	
	
	
}
