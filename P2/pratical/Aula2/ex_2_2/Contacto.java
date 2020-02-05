
public class Contacto {
	private String nom;
	private String tel;
	private String mail;
	
	public Contacto (String nome, String telefone, String eMail) {
		this.nom = nome;
		this.tel = telefone;
		this.mail = eMail;
	}
	
	public Contacto (String nome, String telefone) {

		this.nom = nome;
		this.tel = telefone;
		this.mail = null;
	}
	
	public String nome() {
		return nom;
	}
	
	public String telefone() {
		return tel;
	}
	
	public String eMail() {
		return mail;
	}
}

