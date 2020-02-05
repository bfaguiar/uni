package lib;

import java.io.Serializable;

public class Airplane implements Serializable {

	/**
	 * 
	 */
	private static final long serialVersionUID = 3249229861750617515L;
	
	private String  name          ;
	private String  airplaneType  ;
	private String  wingsType     ;
	private String  jetEngine     ;
	private int     numberOfJets  ;
	private int     releaseYear   ;
	private int     numberOfSeats ;
	private int     speed         ;
	
	public Airplane(String name, String airplaneType, String wingsType, String jetEngine, int numberOfJets, int releaseYear, int numberOfSeats, int speed) { 
		
		this.name           =  name          ;
		this.airplaneType   =  airplaneType  ;
		this.wingsType      =  wingsType     ;
		this.jetEngine      =  jetEngine     ;
		this.numberOfJets   =  numberOfJets  ;
		this.releaseYear    =  releaseYear   ;
		this.numberOfSeats  =  numberOfSeats ;
		this.speed          =  speed         ;
	
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getAirplaneType() {
		return airplaneType;
	}

	public void setAirplaneType(String airplaneType) {
		this.airplaneType = airplaneType;
	}

	public String getWingsType() {
		return wingsType;
	}

	public void setWingsType(String wingsType) {
		this.wingsType = wingsType;
	}

	public String getJetEngine() {
		return jetEngine;
	}

	public void setJetEngine(String jetEngine) {
		this.jetEngine = jetEngine;
	}

	public int getNumberOfJets() {
		return numberOfJets;
	}

	public void setNumberOfJets(int numberOfJets) {
		this.numberOfJets = numberOfJets;
	}

	public int getReleaseYear() {
		return releaseYear;
	}

	public void setReleaseYear(int releaseYear) {
		this.releaseYear = releaseYear;
	}

	public int getNumberOfSeats() {
		return numberOfSeats;
	}

	public void setNumberOfSeats(int numberOfSeats) {
		this.numberOfSeats = numberOfSeats;
	}
	
	public int getSpeed() {
		return speed;
	}

	@Override
	public String toString() {
		return  "\n######## AIRPLANE SPECS ###############"
				+ "\nNAME:"                       + name 
				+ "\nPLANE TYPE: "             + airplaneType 
				+ "\nWINGS TYPE: "             + wingsType 
				+ "\nJET ENGINE: "             + jetEngine 
				+ "\nNUMBER OF JETS: "         + numberOfJets 
				+"\nRELEASE YEAR: "            + releaseYear 
				+"\nNUMBER OF SEATS: "         + numberOfSeats 
				+ "\nMAXIMUM SPEED (KM/H): "   + speed 
				+ "";
	}
	
}
