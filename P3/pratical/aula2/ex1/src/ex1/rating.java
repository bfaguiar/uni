package ex1;

public class rating {
	
	private cliente AuxCL;
	private double rate;
	private int count = 0;
	private video AuxVV;
	
	rating(cliente AuxCL, video AuxVV, double rate) {
		
		this.AuxCL = AuxCL;
		this.rate = rate;
		this.AuxVV = AuxVV;
		count++;
	
	}
	
	cliente AuxCL() { return AuxCL; }
	double rate() { return rate; }
	video AuxVV() { return AuxVV; }
	int count() { return count; }
	
	double getMedia(rating rtAux, int size) {
		
		for (int i = 0; i < size; i++) {
			
			double som = rtAux.rate();	
		}
		
		return 0;
	}
	
}
