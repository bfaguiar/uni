package Aula03.Ex2;

public class FiguraHeranša {
	private PontoHeranša ponto;
	
	public FiguraHeranša(int x, int y){
		ponto = new PontoHeranša (x,y);
	}

	public FiguraHeranša(PontoHeranša ponto){
		this.ponto=ponto;
		// TODO Auto-generated constructor stub
	}
	
	
	public PontoHeranša getPonto(){
		return ponto; 
	}
}

