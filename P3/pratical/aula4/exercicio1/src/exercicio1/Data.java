package exercicio1;

public class Data {
	
	private int dia;
	private int mes;
	private int ano;


	public Data(int dia, int mes, int ano){
		this.dia=dia;
		this.mes=mes;
		this.ano=ano;
	}
	
	public int dia(){
		return dia;
	}
	
	public int mes(){
		return mes;
	}
	
	public int ano(){
		return ano;
	}

	@Override
	public String toString() {
		return "Data [dia=" + dia + ", mes=" + mes + ", ano=" + ano + "]";
	}
}
