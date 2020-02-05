import static java.lang.System.*;
import java.util.*;

public class Post {
	private String titulo;
	private String texto;
	private Person author;
	private Date data;
	
	public Post(String texto, Person author, Date data){
		this.texto = texto;
		this.titulo = "Publicacao de " + author.name();
		this.data = data;
		this.author = author;
	}
	
	public Post(String titulo, String texto, Person author, Date data){
		this.texto = texto;
		this.titulo = titulo;
		this.data = data;
		this.author = author;
	}

	public String titulo() { return titulo; }

   
	public String texto() { return texto; }

	public Person author() { return author;} 
   
	public Date data() { return data; }
}
