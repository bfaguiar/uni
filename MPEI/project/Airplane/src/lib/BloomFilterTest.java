package lib;

public class BloomFilterTest {

		public static void main(String[] args) { 
			
			BloomFilter bloom = new BloomFilter(100, 5);
			
			bloom.inserirElemento("Airbus");
			bloom.inserirElemento("Antonov");
			bloom.inserirElemento("ANTR");
			
			System.out.println("Airbus: "  + bloom.elementoPertence("Airbus"));
			System.out.println("Antonov: " + bloom.elementoPertence("Antonov"));
			System.out.println("Antonio: " + bloom.elementoPertence("Antonio"));
			System.out.println("ANTR: "    + bloom.elementoPertence("ANTR"));
		}
}
