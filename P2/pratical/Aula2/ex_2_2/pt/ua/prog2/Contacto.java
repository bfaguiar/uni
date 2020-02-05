package pt.ua.prog2;

// #########################################################################
// CONSTRUTORES 

public class Contacto {
	private String nom;
	private String tel;
	private String mail;
	
	private static int count = 0;
	
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
	
//############################################################################

	
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

