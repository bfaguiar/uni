package lib;

import java.util.concurrent.atomic.AtomicInteger;

class PassByRef {
	public int value;
}
public class Teste {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Integer x = 5;
		x.value = 5;
		change(x);
		System.out.println(x.value);
	}
	
	static void change(PassByRef x) {
		x.value = 10;
	}

}
