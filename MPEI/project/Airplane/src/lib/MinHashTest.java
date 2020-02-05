package lib;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.Arrays;

public class MinHashTest {
	
	public static void main(String[] args) throws ClassNotFoundException, IOException {
		
		Airplane[] planes = load();
		Airplane plane = new Airplane("Hello", "Night fighter", "Rhomboidal Wing", "Turboprop", 4, 1991, 108, 812 );
		MinHash min = new MinHash();
		Airplane[] top5 = min.verify(plane, planes);
		Arrays.asList(top5).forEach(System.out::println);
	}
	
public static Airplane[] load() throws IOException, ClassNotFoundException {
		
		ObjectInputStream ois = new ObjectInputStream(new FileInputStream(new File("AirplanesDataBase.txt")));
		Airplane[] planes = (Airplane[]) ois.readObject();
		ois.close();
		
		return planes;
	
	}

}
