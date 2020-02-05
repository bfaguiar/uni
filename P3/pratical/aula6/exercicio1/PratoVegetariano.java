package Aula06.Ex01;

import java.util.ArrayList;

public class PratoVegetariano extends Prato implements Vegetariano {
	
	public PratoVegetariano(String nome) {
		super(nome);
		// TODO Auto-generated constructor stub
	}
	
	public boolean addIngrediente(Comida aux) {
		// TODO Auto-generated method stub
		if(aux instanceof Vegetariano){
			return super.addIngrediente(aux);
			}
		else{
			
			return false;
		}
	}
}