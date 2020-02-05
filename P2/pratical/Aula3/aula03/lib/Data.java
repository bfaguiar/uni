package lib;

public class Data {
	
	private int  dia, mes, ano;
	
	public Data (int dia, int mes, int ano) {
		this.dia = dia;
		this.mes = mes;
		this.ano = ano;
		
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
	
	public static boolean dataValida(Data data){
		if(data.ano > 2015 && data.mes > 0 && data.mes < 13){
			if(Data.diasDoMesAno(data.mes,data.ano) >= data.dia && data.dia > 0){
				return true;
			} else return false;
		} else return false;
	}
	
	public static boolean anoBissexto(int ano){
		if(ano % 4 == 0){
			if(ano % 100 == 0 && ano % 400 != 0)
				return false;
			else return true;
		}
		else return false;
	}
	
	public static int diasDoMesAno(int mes, int ano){
		switch (mes){
		case 1:
			return 31;
		case 2:
			if(Data.anoBissexto(ano)){
				return 29;
			} else return 28;
		case 3:
			return 31;
		default:return 0;
		}
	}
	
	
	public boolean  igualA(Data d) {
		if (this.ano == d.ano() && this.dia == d.dia && this.mes == d.mes) 
			return true;
				else return false;
	}
	
	public boolean  menorDoQue(Data d) {
		if ((this.ano <  d.ano() &&  this.dia ==  d.dia() &&  this.mes ==  d.mes()) || (this.ano ==  d.ano() &&  this.dia() ==  d.dia &&  this.mes <  d.mes()) || (this.ano ==  d.ano() &&  this.dia() <  d.dia() &&  this.mes ==  d.mes()))
			return true;
				else return false;
	}
	
	public boolean  maiorDoQue(Data d) {
		if ((this.ano >  d.ano() &&  this.dia ==  d.dia() &&  this.mes ==  d.mes()) || (this.ano ==  d.ano() &&  this.dia() ==  d.dia &&  this.mes >  d.mes()) || (this.ano ==  d.ano() &&  this.dia() >  d.dia() &&  this.mes ==  d.mes()))
			return true;
				else return false;
	}
	
	public void print() {
        System.out.printf("%02d - %02d-%04d\n", this.dia, this.mes, this.ano);
	}
	
}

