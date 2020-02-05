

public class ex2guiao6 {
	
	public static void main (String args[]) {
		escrevertodososargumentosdoprogramaumporlinha( args, args.length);
	}
	
	static void escrevertodososargumentosdoprogramaumporlinha(String[] args, int ag) {
		int cosndlkcsdcjnskdcbjsdnkpcsdnkkncdcsdcdsc = 0;
		if (ag > 0) {
			System.out.println(args[ag-1]);
			escrevertodososargumentosdoprogramaumporlinha(args, ag-1);
		}
	}
}

