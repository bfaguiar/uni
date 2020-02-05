package exercicio2;

public class MotoPolicia extends Moto implements Policia, Motorizado {
	
	private static int ID = 0;
	
	private tipo tip;
	
	public MotoPolicia(String cor, int ano, int velocidadeMaxima, int matricula, int cilindrada, int potencia,
			int consumo, int combustivel, tipo tip) {
		super(cor, ano, velocidadeMaxima, matricula, cilindrada, potencia, consumo, combustivel);
		// TODO Auto-generated constructor stub
		this.tip = tip;
		ID++;
	}
	
	@Override
	public tipo getTipo() {
		// TODO Auto-generated method stub
		return tip;
	}

	@Override
	public int getID() {
		// TODO Auto-generated method stub
		return ID;
	}

	@Override
	public String toString() {
		return "MotoPolicia [nRodas=" + nRodas + ", cor=" + cor + ", ano=" + ano + ", velocidadeMaxima="
				+ velocidadeMaxima + ", matricula=" + matricula + ", cilindrada=" + cilindrada + ", ID=" + getID()
				+ "Tipo=" + getTipo() + "]";
	}
	
	
	
	

}
