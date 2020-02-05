package exercicio4;

public class video {
	//partilhado por todos os objectos da classe -> static
	private String titulo;
	private int idade;
	private String categoria;
	
	
	video(String titulo, int idade, String categoria) {
		this.titulo = titulo;
		this.idade = idade;
		this.categoria = categoria;
	}
	
	
	int idade() { return idade; }
	String titulo() { return titulo; }
	String categoria() { return categoria; }
	
	void getVideo(video objVid) {
		System.out.println("");
		System.out.println("NOME DO VIDEO: " + objVid.titulo);
		System.out.println("IDADE: " + objVid.idade);
		System.out.println("CATEGORIA: " + objVid.categoria);
		
	}
}