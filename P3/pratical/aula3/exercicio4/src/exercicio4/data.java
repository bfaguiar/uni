package exercicio4;

import java.util.*;
import java.text.DateFormat;
import java.text.SimpleDateFormat;

public class data {
		
		private int dia, mes, ano;
		
		data(int dia, int mes, int ano) {
			this.dia = dia;
			this.mes = mes;
			this.ano = ano;
		}
		
		int dia() { return dia; }
		int mes() { return mes; }
		int ano() { return ano; }
		
		public int idade(){
		DateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
		Date date = new Date();
		String data = dateFormat.format(date);
		String [] aux = data.split("/");
		int d = Integer.parseInt(aux[0]);
		int m = Integer.parseInt(aux[1]);
		int a = Integer.parseInt(aux[2]);
		
		
		if(m>mes){
			return a-ano;
		}else if(m<mes){
			return a-ano-1;
		}else{
			if(d>=dia){
				return a-ano;
			}else{
				return a-ano-1;
			}
		}
	}
		
	@Override
	public String toString() {
		return  dia + "/" + mes + "/" + ano;
	}

}
