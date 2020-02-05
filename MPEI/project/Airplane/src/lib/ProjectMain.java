package lib;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Stream;

import com.sun.xml.internal.messaging.saaj.packaging.mime.util.LineInputStream;

import static java.lang.System.*;

import static java.lang.System.*;

public class ProjectMain {
	
	static final int N_CAR = 8; // numero de caracteristicas de cada objecto.
	
	static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) throws ClassNotFoundException, IOException {
	
		/*
		 *  1 - Load da dataBase das aeronaves
		 *  2 - Criacao de Bloom Filters para as caracteristicas de cada Aviao.
		 *  3 - Adicao das caracteristicas em cada bloom filter.
		 *  4 - Menu.
		 */
		 
		 Airplane[] planes = load();
		 BloomFilter[] bloom = bloomArrayInit();
		 bloomArrayAdd(bloom, planes);
		 menu(planes, bloom);
		 
	}
	
	
	
	public static Airplane[] load() throws IOException, ClassNotFoundException {
		
		ObjectInputStream ois = new ObjectInputStream(new FileInputStream(new File("AirplanesDataBase.txt")));
		Airplane[] planes = (Airplane[]) ois.readObject();
		ois.close();
		
		return planes;
	
	}
	
	public static BloomFilter[] bloomArrayInit() {
		
	     BloomFilter[] bloom = new BloomFilter[N_CAR];
		
	     for (int i = 0; i < N_CAR; i++)
			 bloom[i] = new BloomFilter(1500, 14);

		 return bloom;
	
	}
	
	public static void bloomArrayAdd(BloomFilter[] bloom, Airplane[] planes) {
		
			Arrays.stream(planes).parallel().forEach(pln -> bloom[0].inserirElemento((pln.getName())));
			Arrays.stream(planes).parallel().forEach(pln -> bloom[1].inserirElemento((pln.getAirplaneType())));
			Arrays.stream(planes).parallel().forEach(pln -> bloom[2].inserirElemento((pln.getWingsType())));
			Arrays.stream(planes).parallel().forEach(pln -> bloom[3].inserirElemento((pln.getJetEngine())));
			Arrays.stream(planes).parallel().forEach(pln -> bloom[4].inserirElemento((Integer.toString(pln.getNumberOfJets()))));
			Arrays.stream(planes).parallel().forEach(pln -> bloom[5].inserirElemento((Integer.toString(pln.getReleaseYear()))));
			Arrays.stream(planes).parallel().forEach(pln -> bloom[6].inserirElemento((Integer.toString(pln.getNumberOfSeats()))));
			Arrays.stream(planes).parallel().forEach(pln -> bloom[7].inserirElemento((Integer.toString(pln.getSpeed()))));
	}
	
	public static void menu(Airplane[] planes, BloomFilter[] bloom) throws IOException {
		
		String input = null;
		do {
			
			out.print("\n-------------------------------------------------------------------------------------------------------\n"
					+ "                                           SEARCH AIRPLANES                                            \n" 
					+ "-------------------------------------------------------------------------------------------------------\n"
					+ "type 'help' to see how it works\n\n"                                                                     );
			out.print("» ");
			input = sc.nextLine();
			
			String[] str = input.split(" ");
			
			switch (str[0]) {
			
				case "plane":
					final String in = str[1];
					 if(bloom[0].elementoPertence(str[1])) {
						 out.println("Airplane " + in + " exists, type 'print' to print all or press enter to skip...\n");
						 input = sc.nextLine();
						 if(input.equals("print"))
							 Arrays.stream(planes).parallel().filter(pln -> pln.getName().equals(in)).forEach(out::println);

					 }
					 else out.println("Airplane " + in + " does not exist in our data base, please try again...\n");
				break;
				
				case "type":
					final String in2 = str[1];
					 if(bloom[1].elementoPertence(str[1])) {
						 out.println("Airplane type" + in2 + " exists, type 'print' to print all or press enter to skip...\n");
						 input = sc.nextLine();
						 if(input.equals("print"))
							 Arrays.stream(planes).parallel().filter(pln -> pln.getAirplaneType().equals(in2)).forEach(out::println);
					 }
					 else out.println("Airplane type" + in2 + " does not exist in our data base, please try again...\n");
				break;
				
				case "wings":
					final String in3 = str[1];
					 if(bloom[2].elementoPertence(str[1])) {
						 out.println("Wings type " + in3 + " exists, type 'print' to print all or press enter to skip...\n");
						 input = sc.nextLine();
						 if(input.equals("print"))
							 Arrays.stream(planes).parallel().filter(pln -> pln.getWingsType().equals(in3)).forEach(out::println);
					 }
					 else out.println("WingsType " + in3 + " does not exist in our data base, please try again...\n");
				break;
				
				case "engine":
					final String in4 = str[1];
					 if(bloom[3].elementoPertence(str[1])) {
						 out.println("Engine type " + in4 + " exists, type 'print' to print all or press enter to skip...\n");
						 input = sc.nextLine();
						 if(input.equals("print"))
							 Arrays.stream(planes).parallel().filter(pln -> pln.getJetEngine().equals(in4)).forEach(out::println);
					 }
					 else out.println("Engine type " + in4 + " does not exist in our data base, please try again...\n");
				break;
				
				case "njets":
					final String in5 = str[1];
					 if(bloom[4].elementoPertence(str[1])) {
						 out.println("Number of jets =  " + in5 + " exists, type 'print' to print all or press enter to skip...\n");
						 input = sc.nextLine();
						 if(input.equals("print"))
							 Arrays.stream(planes).parallel().filter(pln -> Integer.toString(pln.getNumberOfJets()).equals(in5)).forEach(out::println);
					 }
					 else out.println("Number of jets = " + in5 + " does not exist in our data base, please try again...\n");
			    break;
			    
				case "release":
					final String in6 = str[1];
					 if(bloom[5].elementoPertence(str[1])) {
						 out.println("Airplanes with release year of  " + in6 + " exists, type 'print' to print all or press enter to skip...\n");
						 input = sc.nextLine();
						 if(input.equals("print"))
							 Arrays.stream(planes).parallel().filter(pln -> Integer.toString(pln.getReleaseYear()).equals(in6)).forEach(out::println);
					 }
					 else out.println("Airplanes with release year of " + in6 + " does not exist in our data base, please try again...\n");
				break;
				
				case "nseats":
					final String in7 = str[1];
					 if(bloom[6].elementoPertence(str[1])) {
						 out.println("Number of seats =  " + in7 + " exists, type 'print' to print all or press enter to skip...\n");
						 input = sc.nextLine();
						 if(input.equals("print"))
							 Arrays.stream(planes).parallel().filter(pln -> Integer.toString(pln.getNumberOfSeats()).equals(in7)).forEach(out::println);
					 }
					 else out.println("Number of seats =  " + in7 + " does not exist in our data base, please try again...\n");
				break;
				
				case "speed":
					final String in8 = str[1];
					 if(bloom[7].elementoPertence(str[1])) {
						 out.println("Maximum speed of =  " + in8 + " exists, type 'print' to print all or press enter to skip...\n");
						 input = sc.nextLine();
						 if(input.equals("print"))
							 Arrays.stream(planes).parallel().filter(pln -> Integer.toString(pln.getSpeed()).equals(in8)).forEach(out::println);
					 }
					 else out.println("Maximum speed  = " + in8 + " does not exist in our data base, please try again...\n");
				break;
				
				case "help":
					out.println("\n\n"
						  	    + "                                             INSTRUCTION SET                                               ");
					out.println("\n\nThis application works with commands... if you want to search for an airplane by its characteristics, type them...\nExample:\n» plane Concorde\nSearch for planes with name 'Concorde'.");
					out.println("\nCOMMANDS LIST:\n'plane'   - Search by Airplane's name\n'type'    - Search by Airplane's type... Eg.: Airliner, Dive Bomber, Night Fighter, etc...\n'wings'   - Search for wings type"
							+ "\n'engine'  - Search for engine type\n'njets'   - Search for number of engine jets on a plane\n'release' - Search for planes that was released in that year\n"
							+ "'nseats'  - Search for Airplanes with that have a specific number of seats\n'speed'   - Search for Airplanes with a specific maximum speed\n'specific' - Search for an airplane by all of its characteristics. Eg.: » specific \\n » Concorde,Airliner,Crescent,Turboprop,3,1993,308,1068\n'printall' - Print all Airplanes available on Data Base.\n\n  To quit program: 'q', 'quit', 'exit'\n\n"
						  	  + "\n");
				break;
				
				case "specific": 
					int cntPrtnc = 0;
					out.print("» ");
					String scan = sc.nextLine();
					String inputs[] = scan.split(",");
					Airplane plnUser = new Airplane(inputs[0], inputs[1], inputs[2], inputs[3], Integer.parseInt(inputs[4]), Integer.parseInt(inputs[5]), Integer.parseInt(inputs[6]), Integer.parseInt(inputs[7]));
					if (inputs.length == 8)
						for (int i = 0; i < inputs.length; i++)
							if (bloom[i].elementoPertence(inputs[i]))
								cntPrtnc++;
					
					if (cntPrtnc == 8) {
						out.println("That Airplane  exists:\n");
						Arrays.stream(planes).parallel()
											 .filter(pln -> pln.getName().equals(inputs[0]))
											 .filter(pln -> pln.getAirplaneType().equals(inputs[1]))
											 .filter(pln -> pln.getWingsType().equals(inputs[2]))
										     .filter(pln -> pln.getJetEngine().equals(inputs[3]))
										     .filter(pln -> Integer.toString(pln.getNumberOfJets()).equals(inputs[4]))
										     .filter(pln -> Integer.toString(pln.getReleaseYear()).equals(inputs[5]))
										     .filter(pln -> Integer.toString(pln.getNumberOfSeats()).equals(inputs[6]))
										     .filter(pln -> Integer.toString(pln.getSpeed()).equals(inputs[7]))
											 .forEach(out::println);
					}
					else {
						MinHash min = new MinHash();
						Airplane[] top5 = min.verify(plnUser, planes);
						out.println("\nThat Airplane does not exist in our data base, but we found this similar Airplanes (the 5 most similar airplanes):");
						Arrays.asList(top5).forEach(out::println);
					}
				   
				break;
				
				case "printall": 
					Arrays.asList(planes).forEach(out::println);
				break;
				
				case "q":
					exit(0);
				break;
				
				case "quit":
					exit(0);
				break;
				
				case "exit":
					exit(0);
				break;
				
				default:
					out.println("Please, insert appropriate command, type 'help' to see options.");
				break;
			}
		
		} while(!(input.equals("q") || input.equals("quit") || input.equals("exit")));
	
	}
}
