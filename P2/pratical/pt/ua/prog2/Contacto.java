package pt.ua.prog2;

public class Contacto {
	private static int count = 0;
	private String nom;
	private String tel;
	private String mail;
	
	public Contacto (String nome, String telefone, String eMail) {
		this.nom = nome;
		this.tel = telefone;
		this.mail = eMail;
		count++;
	}
	
	public Contacto (String nome, String telefone) {

		this.nom = nome;
		this.tel = telefone;
		this.mail = null;
		count++;
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
	
	public static void print() {
		System.out.println("Numero de Contactos: " +  count);
	}
}

