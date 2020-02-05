package Aula06.Ex01;

import java.util.ArrayList;

public class Prato {
	private String nome;
	private ArrayList<Comida> pratoArray = new ArrayList<>();
	
	public Prato(String nome){
		this.nome=nome;
	}
	
	public String getNome(){
		return nome;
	}
	
	public ArrayList<Comida> getAlimentos(){
		return pratoArray;
	}
	
	public double calorias(){
		double soma=0;
		for(int i=0; i<pratoArray.size(); i++){
			soma=soma+pratoArray.get(i).getCal();
		}
		return soma;
	}
	
	public int size(){
		return pratoArray.size();
	}

	public boolean addIngrediente(Comida aux) {
		// TODO Auto-generated method stub
		if(pratoArray.contains(aux) || aux==null){return false;}
		else{
			pratoArray.add(aux);
			return true;
		}
	}

	@Override
	public String toString() {
		return  nome + "' composto por " + pratoArray.size() + " Ingredientes";
	}
	
}
