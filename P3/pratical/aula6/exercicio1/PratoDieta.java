package Aula06.Ex01;

import java.util.ArrayList;

public class PratoDieta extends Prato {
	
	private double limite;

	public PratoDieta(String nome, double limite) {
		super(nome);
		this.limite=limite;
		// TODO Auto-generated constructor stub
	}

	
	public double getLimite(){
		return limite;
	}
	
	public boolean addIngrediente(Comida aux) {
		if(super.calorias()+aux.getCal()<=limite){
			return super.addIngrediente(aux);
		}
		else{	
			return false;
		}
	}


	@Override
	public String toString() {
		return "Dieta (" + super.calorias() + "), "+ super.getNome() + " composto por " + super.size() + " ingredientes ";
	}

}