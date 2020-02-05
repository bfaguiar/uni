package lib;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

public class MinHash {
	
	private int hash;
    private char value[];
	
    public MinHash() { }
	
	public Airplane[] verify(Airplane plane, Airplane[] AirplanesOnDataBase){
		
		List<Airplane> AirplanesOnDataBaseList = new ArrayList<>();
		AirplanesOnDataBaseList.addAll(Arrays.asList(AirplanesOnDataBase));
		
		List<Airplane> planeSim1 = new ArrayList<Airplane>(); List<Airplane> planeSim2 = new ArrayList<Airplane>();
		List<Airplane> planeSim3 = new ArrayList<Airplane>(); List<Airplane> planeSim4 = new ArrayList<Airplane>();
	    List<Airplane> planeSim5 = new ArrayList<Airplane>(); List<Airplane> planeSim6 = new ArrayList<Airplane>();
		
		IntStream.range(0, AirplanesOnDataBaseList.size()).forEach(i -> { if (getSimilarity(plane, AirplanesOnDataBaseList.get(i)) == 1)
																			 planeSim1.add(AirplanesOnDataBaseList.get(i));
		
																		  if (getSimilarity(plane, AirplanesOnDataBaseList.get(i)) == 2)
																			  planeSim2.add(AirplanesOnDataBaseList.get(i));
																			  planeSim3.add(AirplanesOnDataBaseList.get(i));
																				 
																		  if (getSimilarity(plane, AirplanesOnDataBaseList.get(i)) == 4)
																			  planeSim4.add(AirplanesOnDataBaseList.get(i));
																		  
																		  if (getSimilarity(plane, AirplanesOnDataBaseList.get(i)) == 5)
																			  planeSim2.add(AirplanesOnDataBaseList.get(i));
																		  
																		  if (getSimilarity(plane, AirplanesOnDataBaseList.get(i)) == 6)
																			  planeSim6.add(AirplanesOnDataBaseList.get(i));
																		  });
		
		List<Airplane> similarAirplanes = new ArrayList<>();
		
		similarAirplanes.addAll(planeSim6); similarAirplanes.addAll(planeSim5); similarAirplanes.addAll(planeSim4);
		similarAirplanes.addAll(planeSim3); similarAirplanes.addAll(planeSim2); similarAirplanes.addAll(planeSim1);
		
		Airplane[] top5 = new Airplane[5];
		IntStream.range(0, top5.length).forEach(i -> { if (similarAirplanes.get(i) != null) top5[i] = similarAirplanes.get(i); });
		
		return top5;
	}
	
	
	int getSimilarity(Airplane plane1, Airplane plane2) {
		
		String[] Airplane1Chars = { plane1.getAirplaneType(), plane1.getWingsType(), plane1.getJetEngine(), Integer.toString(plane1.getNumberOfJets()), 
									Integer.toString(plane1.getNumberOfSeats()),  Integer.toString(plane1.getSpeed()) };
		
		String[] Airplane2Chars = { plane2.getAirplaneType(), plane2.getWingsType(), plane2.getJetEngine(), Integer.toString(plane2.getNumberOfJets()), 
				                    Integer.toString(plane2.getNumberOfSeats()),  Integer.toString(plane2.getSpeed()) };

		int[] getSign1 = getSignature(Airplane1Chars);
		int[] getSign2 = getSignature(Airplane2Chars);
		
		return  IntStream.range(0, getSign1.length).map(i -> count(getSign1[i], getSign2[i])).sum();
	}
	
	int count(int getSign1Int, int getSign2Int) {
		if (getSign1Int == getSign2Int) return 1;
		return 0;
   }
	
	int[] getSignature(String[] plane) {
		return IntStream.range(0,plane.length).map(i -> plane[i].hashCode()).toArray();
	}
	
	void getHashed(String caract) {
		int[] hashes = new int[7];
		int[] primes = { 619, 677, 751, 829, 929, 941, 947 };
		IntStream.range(0, 7).map(i -> hashes[i] = hash((int) Math.random()*500 + 100,(int) Math.random()*500 + 100, caract, primes[(int) (Math.random()*7)])).;
	}
	
	int hash (int a, int b, String x, int p) {
		int x2 = x.hashCode();
		return ( (a*x2 + b) % p) % N;
	}
	
	private final int N = 400;
}
