package Aula03.Ex2;

public class FiguraHerança {
	private PontoHerança ponto;
	
	public FiguraHerança(int x, int y){
		ponto = new PontoHerança (x,y);
	}

	public FiguraHerança(PontoHerança ponto){
		this.ponto=ponto;
		// TODO Auto-generated constructor stub
	}
	
	
	public PontoHerança getPonto(){
		return ponto; 
	}
}

