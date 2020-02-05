package Aula03.Ex2;


public class TesteHerança {
     public static void main(String[] args) {
		 CirculoHerança c1 = new CirculoHerança (2);
		 CirculoHerança c2 = new CirculoHerança (1,3,2);
		 CirculoHerança c3 = new CirculoHerança (c1);
		 System.out.println(c1 + "tem area: " + c1.area()
		 + " e perimetro: " + c1. perimetro());
		 System.out.println(c3 + "tem area: " + c3.area()
		 + " e perimetro: " + c3. perimetro());
		 System.out.println("c1 equals to c3? -> " + c1.equals(c3)); // True
		 QuadradoHerança q1 = new QuadradoHerança(2);
		 QuadradoHerança q2 = new QuadradoHerança(3,4,2);
		 QuadradoHerança q3 = new QuadradoHerança(q2);
		 System.out.println(q1 + "tem area: " + q1.area()
		 + " e perimetro: " + q1.perimetro());
		 System.out.println(q3 + "tem area: " + q3.area()
		 + " e perimetro: " + q3.perimetro());
		 System.out.println("q1 equals to q3? -> " + q1.equals(q3)); // False
		 RetanguloHerança r1 = new RetanguloHerança(2,3);
		 RetanguloHerança r2 = new RetanguloHerança(3,4,2,3);
		 RetanguloHerança r3 = new RetanguloHerança(r2);
		 System.out.println(r1 + "tem area: " + r1.area()
		+ " e perimetro: " + r1. perimetro());
		 System.out.println(r3 + "tem area: " + r3.area() 
		+ " e perimetro: " + r3. perimetro());
		 System.out.println("r2 equals to r3? -> " + r2.equals(r3)); // True
	}
}