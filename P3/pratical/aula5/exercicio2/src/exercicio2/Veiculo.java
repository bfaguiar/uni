package exercicio2;

public abstract class Veiculo implements Comparable<Veiculo> {
		
		protected int nRodas;
		protected String cor;
		protected int ano;
		protected int velocidadeMaxima;
		protected int matricula;
		protected int cilindrada;
		protected static int id=0;
		
		// construtor para herdar nos construtores seguintes!
		public Veiculo(String cor, int ano, int velocidadeMaxima, int matricula, int cilindrada) {
			this.cor = cor;
			this.ano = ano;
			this.velocidadeMaxima = velocidadeMaxima;
			this.matricula = matricula;
			this.cilindrada = cilindrada;
			id++;
		}
		
		public abstract int getNRodas();
		public abstract String getCor();
		public abstract int getAno();
		public abstract int getVelocidadeMaxima();
		public abstract int matricula();
		public abstract int cilindrada();
		
		public int compareTo(Veiculo v) {
			return getAno() - v.getAno();
		}
}
