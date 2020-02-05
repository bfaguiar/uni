package exercicio1;

import java.io.Closeable;
import java.io.IOException;
import java.util.Iterator;
import java.util.Scanner;

public class ScannerAbeirense implements Iterator<String>, Closeable {

	private Scanner scanner;
	
	public ScannerAbeirense() {
		
		this.scanner = new Scanner(System.in);
	
	}
	
	
	@Override
	public void close() throws IOException {
		scanner.close();
	}

	@Override
	public boolean hasNext() {
		if (scanner.hasNext()) return true;
		return false;
	}

	@Override
	public String next() {
		if (scanner.next() != null) return scanner.next();
		return null;
	}
	
	public String stringReplace(String str) {
		str =str.replace('v', 'b');
		str = str.replace('V', 'B');
		return str;
	}
	
	public String nextLine(){
		return scanner.nextLine();
	}

}
