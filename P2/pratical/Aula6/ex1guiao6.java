import java.util.*;
import java.io.*;

public class ex1guiao6 {
	
	public static void main (String args[]) {
	
	Fibonacci(10);
	for ( int i = 0; i <= 10; i++) {
	System.out.println(Fibonacci(i));
	}
	
	}
	
	static int Fibonacci(int n) {
		int f;
		
		if (n == 0) {
			f = 0;
			return f;
		}
		
		if (n == 1) {
			f = 1;
			return f;
		}
		
		if (n > 1) {
			f = Fibonacci(n - 2) + Fibonacci(n - 1);
			return f;
		}
		
		return 0;
	}
}

