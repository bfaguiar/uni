package ex2;
import java.util.*;

public class Interface {
	
	static Scanner sc = new Scanner(System.in);
	static boolean found = false;
	static int count = 0;
	
	public static void main(String args[]){
		
		int opcao;
		pessoa[] lista = new pessoa[100];
		
		do{
			System.out.println("1 - Introduzir nova pessoa na lista.\n 2 - Apagar pessoa da lista.\n 3 - Apresentar lista completa.\n 4 - Sair do programa.\n opcao -> ");
			opcao = sc.nextInt();

		
		switch(opcao){
		
			case 1: AddPerson(lista);
				count++;
			break;
		
			case 2: DeletePerson(lista);
			break;	
			
			case 3: FullList(lista);
				System.out.println("\n");
			break;
			}
		
		}while(!(opcao >= 4));
	}
	
	public static void AddPerson(pessoa[] lista){
		
		boolean validacao, mesvalido, anovalido;
		
		System.out.println("Nome da pessoa: ");
		sc.nextLine();
		String nome = sc.nextLine();
		
		System.out.println("Cartão de Cidadão: ");
		int cc = sc.nextInt();
		
		System.out.println("Ano em que nasceu: ");
		int ano = sc.nextInt();
		do{
			anovalido = true;
			if(ano > 2016){
				anovalido = false;
				System.out.println("ERRO: Introduza um ano ate' 2016!\n Ano: ");
				ano = sc.nextInt();
			}
		} while(anovalido = false);
		
		System.out.println("Mes de nascimento: ");
		int mes = sc.nextInt();
		do{
			mesvalido=true;
			if(mes<1 || mes>12){
				System.out.println("ERRO: Introduza um mes valido!\n Mes: ");
				mes = sc.nextInt();
			}
		}while(mesvalido = false);
		
		System.out.println("Dia em que nasceu: " );
		int dia = sc.nextInt();
		
		do{
			validacao = true;
			if(!(mes == 1 || mes == 3 || mes == 5 || mes == 7 || mes == 8 || mes == 10 || mes == 12) && (dia<1 || dia>31)){
				validacao = false;			
			}
			if(!(mes == 2) && (dia<0 || dia>30)){
				validacao = false;
			}
			if(!(mes == 4 || mes == 6 || mes == 9 || mes == 11) && (dia<0 || dia>31)){
				validacao = false;
			}
			if(validacao==false){
				System.out.println("ERRO: Introduza uma data valida:\n data: ");
				dia = sc.nextInt();
			}
		} while(validacao==false);
		
		data dataNasc = new data(dia, mes, ano);
		lista[count] = new pessoa(nome, cc, dataNasc);	
	}
	
	public static void DeletePerson(pessoa[] lista){
		if(count!=0){
			System.out.print("Numero do Cartão de Cidadão da pessoa que deseja ser eliminada: ");
			int delete = sc.nextInt();
			for(int i=0; i<count; i++){
				System.out.println(delete);
				System.out.println(lista[i].cc());
				if(delete==lista[i].cc()){
					found=true;
					for(int j=i; j<count-1; j++){
						lista[j] = lista[j+1];
					}		
					lista[count-1] = null;
					count--;
					break;
				}
			}
			if(found == false){
				System.out.println("Numero inexistente.");
			}
		}else{
			System.out.print("A lista esta vazia.\n");
		}
	}
	
	public static void FullList(pessoa[] lista){
		String nome;
		int cc, dia, mes, ano;
		if(count!=0){
			for(int i=0; i<count; i++){

				nome = lista[i].nome();
				cc = lista[i].cc();
				dia = lista[i].dataNasc().dia();
				mes = lista[i].dataNasc().mes();
				ano = lista[i].dataNasc().ano();
				System.out.print("\nNome: " + nome + "   CC: " + cc + "   Data de Nascimento: " + dia + "/" + mes + "/" + ano);
			}
		}else{
			System.out.println("\n A lista esta vazia.");
		}
		
	}

}
