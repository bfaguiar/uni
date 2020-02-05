package Aula06.Ex01;

import java.util.ArrayList;

public class Ementa {
	private String nome;
	private String local;
	private ArrayList<Prato>[] em = new ArrayList[7];
	
	
	public Ementa(String nome, String local){
		this.nome=nome;
		this.local=local;
		for(int i=0; i<7; i++){
			em[i] = new ArrayList<Prato>();
		}
	}
	
	public String getNome(){
		return nome;
	}
	
	public String getLocal(){
		return local;
	}

	public boolean addPrato(Prato prato, DiaSemana rand) {
		if(!em[rand.ordinal()].contains(prato) && prato!=null){
			em[rand.ordinal()].add(prato);
			return true;
		}
		else{
			return false;
		}
		
	}
	public String toString() {
		String s = "";
		for(int i=0; i<7 ; i++){
			if(em[i]!=null){
				for(int j=0; j<em[i].size(); j++){
					s = s + em[i].get(j).toString() + " dia " ;
					if(i==0) s = s + DiaSemana.Domingo;
					if(i==1) s = s + DiaSemana.Segunda;
					if(i==2) s = s + DiaSemana.Terça;
					if(i==3) s = s + DiaSemana.Quarta;
					if(i==4) s = s + DiaSemana.Quinta;
					if(i==5) s = s + DiaSemana.Sexta;
					if(i==6) s = s + DiaSemana.Sábado;
					
					s = s + "\n";
				}
			}
		}
		return s;
	}
	
}