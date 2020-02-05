package lib;

import static java.lang.System.out;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.Arrays;
import  java.util.Scanner;

public class AirplaneGenerator implements Serializable {

	
	/**
	 * 
	 */
	private static final long serialVersionUID = -1929771208597876251L;
	
	static int NPLANES = 400;
	
	static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) throws FileNotFoundException, IOException, ClassNotFoundException {
		// TODO Auto-generated method stub
		int command = 0;
		
		do {
			
			System.out.print("AIRPLANE DATABASE GENERATOR:\n1 - generate, print and save\n2 - load and print\nOther - Quit\n-> ");
			try {
				command = sc.nextInt();
			} catch(Exception e) {
				System.out.println("ERROR. PROGRAM IS QUITING...");
				System.exit(1);
			}
			if (command == 1)
				generate();
			else if (command == 2)
				load();
			else
				System.exit(0);
					
		} while (command == 1 || command == 2);

	
	}
	
	public static void save(Object[] planes) throws IOException {

		ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(new File("AirplanesDataBase.txt")));
		oos.writeObject(planes);
		oos.close();
		System.out.println("LOG: Objecto gravado");
	}
	
	public static void generate() throws IOException {
		
		String[] planeName     = {"Airbus", "Antonov", "ATR", "Boeing", "Bombardier", "Douglas", "Ilyushin", "Lockheed", "McDonnell Douglas", "Vickers", "Atlas", "BlackBurn", "Bristol", "Dassault", " Eurofighter", "Fiat", "Grumman", "Hawker",  "Junkers" , "Concorde"};
		String[] planeType     = {"Stealth aircraft", "Dive bomber", "Attack aircraft", "Night fighter", "Aerial warfare", "Dogfight", "Airliner", "Seaplane"} ;
		String[] wingsType     = {"Rigid delta wing", "Flexible Rogallo wing", "Constant chord", "Tapered", "Elliptical", "Semi-elliptical", "Bird wing", "Bat wing", "Flying saucer", "Ogival Delta", "Swept", "Straight", "Crescent", "Cranked Arrow", "Rhomboidal Wing" };
	    String[] jetEngine     = {"Turbojet", "Turbofan", "Turboprop", "Propfan", "Ramjet", "Scramjet", "Waterjet", "Rocket", "Hybrid" };  
	    Integer[] numberOfJets = {2, 3, 4};
	    
	    
	    Airplane[] planes = new Airplane[NPLANES];
	    
	    for(int i = 0; i < NPLANES; i++) {
	    	planes[i] = new Airplane(planeName[(int) (Math.random()*(planeName.length))], 
	    							 planeType[(int) (Math.random()*(planeType.length))],
	    							 wingsType[(int) (Math.random()*(wingsType.length))], 
	    						     jetEngine[(int) (Math.random()*(jetEngine.length))],
	    						     numberOfJets[(int) (Math.random()*(numberOfJets.length))],
	    						     (int) (Math.random()*36 + 1980),
	    						     (int) (Math.random()*400 + 2),
	    						     (int) (Math.random()*1000 + 600)
	    						     );
	    }
	    

		Arrays.asList(planes).forEach(out::println);
		
	    save(planes);
	}
	
	public static void load() throws IOException, ClassNotFoundException {
		
		ObjectInputStream ois = new ObjectInputStream(new FileInputStream(new File("AirplanesDataBase.txt")));
		Airplane[] planes = (Airplane[]) ois.readObject();
		ois.close();
		

		Arrays.asList(planes).forEach(out::println);
		
		System.out.println("Number Of Airplanes On Data Base: " + planes.length);
		System.out.println(" \n ");
	}
}
