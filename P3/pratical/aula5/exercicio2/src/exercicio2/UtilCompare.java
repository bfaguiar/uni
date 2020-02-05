package exercicio2;

public class UtilCompare {
	public static <T> Comparable<T> findMax(Comparable<T>[] a) {
		int maxIndex = 0;
		
		for (int i = 1; i < a.length; i++) {
			if (a[i] != null && a[i].compareTo((T) a[maxIndex]) > 0)
				maxIndex = i;
		}
		return a[maxIndex];
	}
	public static <T> Comparable<T>[] sortArray(Comparable<T>[] a) {
		Comparable <T> aux;
		for (int i = 0; i < a.length; i++) {
			for (int j = 1; j < a.length; j++) {
				if (a[i] != null && a[j] != null && a[i].compareTo((T) a[j]) > 0) {
					aux = a[i];
					a[i] = a[j];
					a[j] = aux;
				}
			}
		}
		return a;
	}
	
}
