package Aula03.Ex2;

public class FiguraHeran�a {
	private PontoHeran�a ponto;
	
	public FiguraHeran�a(int x, int y){
		ponto = new PontoHeran�a (x,y);
	}

	public FiguraHeran�a(PontoHeran�a ponto){
		this.ponto=ponto;
		// TODO Auto-generated constructor stub
	}
	
	
	public PontoHeran�a getPonto(){
		return ponto; 
	}
}

