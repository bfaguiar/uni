import java.util.*;
import java.io.*;

public class ex1guiao8 {
	
	public static void main (String args[]) {
			
		SortedListInt myList = new SortedListInt();
		
		File f; Scanner fin = null;
		
		for (int i = 0; i < args.length; i++) {
			try {
				f = new File (args[i]);
				fin = new Scanner (f);
				while (fin.hasNextLine()) {
					String[] s = fin.nextLine().split(" ");
					for (int j = 0; j < s.length; j++) {
						try {
							int x = Integer.parseInt(s[j]);
							myList.insert(x);
						} catch (Exception ee) {;}
						}
					} fin.close();
				} catch(IOException e) {;} finally { fin.close(); }
			}
			while (!myList.isEmpty()) {
				System.out.println(myList.first());
				myList.removeFirst();
			}
		}
	}

