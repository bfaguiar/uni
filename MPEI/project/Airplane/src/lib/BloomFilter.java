package lib;

import java.util.Arrays;

import static java.lang.System.*;

public class BloomFilter {
	
	private int size;
	private int[] filtro;
	private int nHashes;
	
	
	public BloomFilter(int size, int nHashes) {
		this.size     = size;
		filtro        = new int[size];
		this.nHashes  = nHashes;
		
	}
	
	/*
	 *  insere com 1 na posicao do Bloom Filter e replica a string com strings derivadas dele, 
	 *  Ex.: string1, string2, ... , stringn para uma melhor eficiencia. 
	 *  
	 */
	public void inserirElemento(String elemento) {
		
		filtro[this.hash(elemento)] = 1;
		
		for(int i = 1; i < nHashes; i++) {			
			filtro[this.hash(elemento += i)] = 1;
		}
	
	}
	
	/*
	 * Verifica se o elemento nao pertence à Bloom Filter
	 */
	public boolean elementoPertence(String elemento) {
		
		if (filtro[this.hash(elemento)] != 1)
			return false;
		
		for(int i = 1; i < nHashes; i++)
			if (filtro [this.hash(elemento += i)] != 1)
				return false;
		
		return true;
	}
	
	/*
	 * faz a função de hash.
	 */
	public int hash(String elemento) { 
		return Math.abs(elemento.hashCode() % size);
	}
	

	public void print_teste(){
		
		Arrays.asList(filtro).forEach(out::println);
		System.out.println();
	}
}
