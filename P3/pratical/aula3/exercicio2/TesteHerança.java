package Aula03.Ex2;


public class TesteHeran�a {
     public static void main(String[] args) {
		 CirculoHeran�a c1 = new CirculoHeran�a (2);
		 CirculoHeran�a c2 = new CirculoHeran�a (1,3,2);
		 CirculoHeran�a c3 = new CirculoHeran�a (c1);
		 System.out.println(c1 + "tem area: " + c1.area()
		 + " e perimetro: " + c1. perimetro());
		 System.out.println(c3 + "tem area: " + c3.area()
		 + " e perimetro: " + c3. perimetro());
		 System.out.println("c1 equals to c3? -> " + c1.equals(c3)); // True
		 QuadradoHeran�a q1 = new QuadradoHeran�a(2);
		 QuadradoHeran�a q2 = new QuadradoHeran�a(3,4,2);
		 QuadradoHeran�a q3 = new QuadradoHeran�a(q2);
		 System.out.println(q1 + "tem area: " + q1.area()
		 + " e perimetro: " + q1.perimetro());
		 System.out.println(q3 + "tem area: " + q3.area()
		 + " e perimetro: " + q3.perimetro());
		 System.out.println("q1 equals to q3? -> " + q1.equals(q3)); // False
		 RetanguloHeran�a r1 = new RetanguloHeran�a(2,3);
		 RetanguloHeran�a r2 = new RetanguloHeran�a(3,4,2,3);
		 RetanguloHeran�a r3 = new RetanguloHeran�a(r2);
		 System.out.println(r1 + "tem area: " + r1.area()
		+ " e perimetro: " + r1. perimetro());
		 System.out.println(r3 + "tem area: " + r3.area() 
		+ " e perimetro: " + r3. perimetro());
		 System.out.println("r2 equals to r3? -> " + r2.equals(r3)); // True
	}
}