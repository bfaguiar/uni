package exercicio2;

import java.util.ArrayList;

public class ColecaoFiguras {
	
	ArrayList<Figura> colecaoFig = new ArrayList<>();
	
	private double maxArea;
	
	public ColecaoFiguras(double maxArea) {
		this.maxArea = maxArea;
		
	}
	
	public double getMaxArea() {
		return maxArea;
	}

	public boolean addFigura(Figura f) { 
		if (colecaoFig.contains(f)) return false;
		 colecaoFig.add(f);
		 return true;
	}
	
	public boolean delFigura(Figura f) { 
		if (colecaoFig.contains(f)) {
			colecaoFig.remove(f);
		}
		return false;
	}
	
	public double areaTotal() { 
		double areaTot = 0;
		for (int i = 0; i < colecaoFig.size(); i++) {
			areaTot += colecaoFig.get(i).area();
		}
		return areaTot;
	}
	
	public boolean exists(Figura f) { 
		if(colecaoFig.contains(f)) return true;
		return false;
	}
	
	
	@Override
	public String toString() {
		
		String str = null;
		for (int i = 0; i < colecaoFig.size(); i++) {
			str = " " + colecaoFig.get(i);
		}
		return str;
	}
	
	//adaptamos o array Figura[] do enunciado ao ArrayList.
	public ArrayList<Figura> getFiguras() { return colecaoFig; }

	//adaptamos o array Figura[] do enunciado ao ArrayList.
	public ArrayList<Ponto> getCentros() { 
		ArrayList<Ponto> ponto = new ArrayList<>();
		for (int i = 0; i < colecaoFig.size(); i++) {
			ponto.add(colecaoFig.get(i).getPonto());
			}
		return ponto;
	}
}
