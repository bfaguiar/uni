package exercicio3;


import java.util.ArrayList;
import java.util.Scanner;

public class app {
	
	static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		ArrayList<estudante> estud = new ArrayList<>();
		ArrayList<cliente> client = new ArrayList<>();
		ArrayList<funcionario> func = new ArrayList<>();
		ArrayList<video> vid = new ArrayList<>();
		ArrayList<emprestimo> emp = new ArrayList<>();
		
		
		int opcao;
		cliente c = null;
		video objVid = null;
		emprestimo objEmp = null;
		
		do {
		System.out.printf("\nVIDEOCLUBE\n");
		System.out.println("");
		System.out.printf("1- Introduzir utilizador\n2- Remover utilizador\n3- Pesquisar e listar videos disponiveis\n4- Introduzir video\n5- Remover video\n6- pesquisar ou listar videos emprestados\n7- efetuar empréstimo\n8- devolução\n9- Ver todos os utilizadores \n10- Sair\n opcao -> ");
		opcao = sc.nextInt();
		sc.nextLine();
		switch(opcao) {
			case 1:
				String utilizador;
				do {
				System.out.printf("Introduzir um utilizador\n\n Es aluno ou funcionario? "); 
				utilizador = sc.nextLine();
				
				int nmec;
				int nFiscal;
				
				switch(utilizador) {
				
					case "aluno":
							
							System.out.print("\nData de inscricao: ");
							String dataInscricao = sc.nextLine();
							
							System.out.print("\nNome: ");
							String nome = sc.nextLine();
							
							System.out.print("\nCartao de cidadao: ");
							int cc  = sc.nextInt();
							sc.nextLine();
							
							System.out.print("\n N. Mecanografico: ");
							nmec = sc.nextInt();
							
							sc.nextLine();
							System.out.print("\n Data de nascimento: ");
							String dataNascimento = sc.nextLine();
						
							System.out.print("\nCurso: ");
							String curso = sc.nextLine();
							
							String[] splitDNascimento = dataNascimento.split("/");
							String[] splitDInscricao = dataInscricao.split("/");
							
							int dia1 = Integer.parseInt(splitDNascimento[0]);
							int mes1 = Integer.parseInt(splitDNascimento[1]);
							int ano1 = Integer.parseInt(splitDNascimento[2]);
							
							int dia2 = Integer.parseInt(splitDInscricao[0]);
							int mes2 = Integer.parseInt(splitDInscricao[1]);
							int ano2 = Integer.parseInt(splitDInscricao[2]);
							
							data dataNasc = new data(dia1, mes1, ano1);
							data dataInsc = new data(dia2, mes2, ano2);
							
							c = new cliente(dataInsc, nome, cc, dataNasc);
							estudante objEstudante = new estudante(dataInsc, nome, cc, dataNasc, nmec, curso);
							estud.add(objEstudante);
							client.add(c);
							
							
							break;
							
						case "funcionario":
							
							System.out.print("\nData de inscricao: ");
							String dataInscricaoF = sc.nextLine();
							
							System.out.print("\nNome: ");
							String nomeF = sc.nextLine();
							
							System.out.print("\nCartao de cidadao: ");
							int ccF  = sc.nextInt();
							
							sc.nextLine();
							System.out.print("\n Data de nascimento: ");
							String dataNascimentoF = sc.nextLine();
							
							System.out.print("\nNumero fiscal: ");
							nFiscal = sc.nextInt();
							

							String[] splitDNascimentoF = dataNascimentoF.split("/");
							String[] splitDInscricaoF = dataInscricaoF.split("/");
							
							int dia1F = Integer.parseInt(splitDNascimentoF[0]);
							int mes1F = Integer.parseInt(splitDNascimentoF[1]);
							int ano1F = Integer.parseInt(splitDNascimentoF[2]);
							
							int dia2F = Integer.parseInt(splitDInscricaoF[0]);
							int mes2F = Integer.parseInt(splitDInscricaoF[1]);
							int ano2F = Integer.parseInt(splitDInscricaoF[2]);
							
							data dataNascF = new data(dia1F, mes1F, ano1F);
							data dataInscF = new data(dia2F, mes2F, ano2F);
							
							c = new cliente(dataInscF, nomeF, ccF, dataNascF);
							funcionario objFuncionario = new funcionario(dataInscF, nomeF, ccF, dataNascF, nFiscal);
							func.add(objFuncionario);
							client.add(c);
							
							break;
							
						default : 
							System.out.println(" Erro!");
							break;
				} } while (utilizador == "aluno" || utilizador == "funcionario");
				break;
			
			case 2:
			
				sc.nextLine();
				System.out.print("ID do utilizador: ");
				int ID = sc.nextInt();
				client.remove(ID-1);
				break;
				
			case 3:
				
				String opcao2;
				do {
				System.out.println("Pesquisar video ou listar todos os videos?");
				System.out.printf("opcao -> ");
				opcao2 = sc.nextLine();
				
				switch(opcao2) {
					case "pesquisar":
						
						System.out.printf("Indique o ID do filme que quer pesquisar: ");
						int pesq = sc.nextInt();
						objVid.getVideo(vid.get(pesq-1));
						
						break;
					
					case "listar":
						
						for (int i = 0; i < vid.size(); i++) {
							objVid.getVideo(vid.get(i));
						}
						
						break;
					
					default:
						System.out.println(" Erro!");
						break;
				} } while (opcao2 == "pesquisar" || opcao2 == "listar");
				
				break;
			case 4:
				
				System.out.print("\nIntroduzir video\n ");
				System.out.print("\nNome: ");
				String nomeVid = sc.nextLine();
				
				System.out.print("\nIdade aconselhada: ");
				int iddVid = sc.nextInt();
				
				sc.nextLine();
				System.out.print("\nCategoria: ");
				String categoria = sc.nextLine();
				
				switch(iddVid) {
				case 10: 
					objVid = new video(nomeVid, video.categoria.M10, categoria);
					vid.add(objVid);
					break;
				case 12:
					objVid = new video(nomeVid, video.categoria.M12, categoria);
					vid.add(objVid);
					break;
				case 14: 
					objVid = new video(nomeVid, video.categoria.M14, categoria);
					vid.add(objVid);
					break;
				case 16: 
					objVid = new video(nomeVid, video.categoria.M16, categoria);
					vid.add(objVid);
					break;
				case 18:
					objVid = new video(nomeVid, video.categoria.M18, categoria);
					vid.add(objVid);
					break;
				default: objVid = new video(nomeVid, video.categoria.M10, categoria);
					vid.add(objVid);
					break;
					
				}
				
				
				break;
			case 5:
				sc.nextLine();
				System.out.print("ID do video: ");
				int IDvid = sc.nextInt();
				vid.remove(IDvid-1);
				break;
			case 6:
				String opcao3;
				do {
				System.out.println("Pesquisar video ou listar todos os videos emprestados?");
				System.out.printf("opcao -> ");
				opcao3 = sc.nextLine();
				
				switch(opcao3) {
					case "pesquisar":
						
						System.out.printf("Indique o ID do filme que quer pesquisar: ");
						int pesq2 = sc.nextInt();
						objEmp.getEmprestimo(emp.get(pesq2-1));
						
						break;
					
					case "listar":
						
						for (int i = 0; i < emp.size(); i++) {
							objEmp.getEmprestimo(emp.get(i));
						}
						
						break;
					
					default:
						System.out.println(" Erro!");
						break;
				} } while (opcao3 == "pesquisar" || opcao3 == "listar");
				
				
				
				break;
			case 7:
				// efetuar emprestimo
				System.out.print("Indique o seu ID de utilizador: ");
				int IDu = sc.nextInt();
				System.out.print("Indique o ID do video que quer requesitar: ");
				int empVideo = sc.nextInt();
				
				cliente aux = client.get(IDu-1);
				video auxV = vid.get(empVideo-1);
				objEmp = new emprestimo (aux, auxV);
				
				emp.add(objEmp);
				vid.remove(empVideo-1);
				
				break;
			case 8:
				// devolucao
				System.out.print("Insira o ID do video que deseja devolver: ");
				int IDdev = sc.nextInt();
				emprestimo auxE = emp.get(IDdev-1);
				emp.remove(IDdev-1);
				video auxViddd = auxE.vi();
				vid.add(auxViddd);
				
				break;
			case 9:
				
				for (int i = 0; i < client.size(); i++) {
					c.printCliente(client.get(i));
					System.out.println("");
				}
				break;
				
			case 10:
				System.exit(10);
			
		
		} } while (opcao <=10);
	}

}
