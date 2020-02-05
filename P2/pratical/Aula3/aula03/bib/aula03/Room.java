public class Room {
	
	private String RoomType;
	private Point bottomLeft;
	private Point bottomRight;
	
	public Room (String RoomType, Point bottomLeft, Point bottomRight) {
		
		assert (bottomLeft().x < bottomRight().x);
		assert (bottomLeft().y < bottomRight().y);
		assert (roomType != null);
		assert (roomType.length > 0);
		
		this.RoomType = RoomType;
		this.bottomLeft = bottomLeft;
		this.bottomRight = bottomRight;}
	
	public String roomType() { return roomType; }
	public Point bottomLeft() { return bottomLeft; }
	public Point bottomRight() { return bottomRight; }
	public Point geomCenter() { return bottomLeft.halfWay(bottomRight); }
	
	public int area() { 
		int dx = bottomLeft.x - bottomRight.x;
		int dy = bottomRight.y - bottomLeft.y;
		int dt = dx * dy; 
		assert (dt > 0); 
		return dt; } }


