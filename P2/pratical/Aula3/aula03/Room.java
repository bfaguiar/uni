///////////////////////////////////////////////////////////////////////////////////////
//EXERCÍCIO 3.7																	   	//
//////////////////////////////////////////////////////////////////////////////////////

public class Room {

	
	public  Room(String roomType, Point bl, Point tr) {
		
		assert topRight.x() > bottomLeft.x() : "invalid room";
		assert topRight.y() > bottomLeft.y() : "invalid room";
		assert roomType != null : "invalid room";
		assert roomType.length() > 0 : "invalid room";
		
		this.roomType = roomType;
		bottomLeft = bl;
		topRight = tr;
	
	}
	
	public String roomType() { return roomType; }

	public Point bottomLeft() { return bottomLeft;}
	
	public Point topRight() { return topRight; } 
	
	public Point geomCenter() { return bottomLeft.halfWayTo(topRight); }
	
	
	public double area() {
		double dx = topRight.x() - bottomLeft.x();
		double dy = topRight.y() - bottomLeft.x();
		double area = dx*dy;
		assert area > 0;
		return area;
	}
	
	private String roomType;
	private Point bottomLeft, topRight;
	
}

// ESQUEMA DO QUE SE QUER.
//
//         ######################################## P(ponto )
//         ##								     ##
//		   ##							         ##
//		   ##				 **    			     ##  ( this.y + p.y ) / 2
//		   ##								     ##	  
//		   ##									 ##
//		   ########################################
// P0 (ponto 0) --->>> "this."  ( this.x + p.x) / 2
//                      bottomLeft	
