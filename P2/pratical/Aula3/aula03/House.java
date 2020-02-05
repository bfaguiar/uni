public class House {
	
	public House(String type) {
	
	}
	
	public House(String type, int maxRooms, int numExpand) {
	this.type = type;
	this.maxRooms = maxRooms;
	this.numExpand = numExpand;
	rooms = new Room[maxRooms];
	
	
	}
	
	public void addRoom (Room r) {
		
		if (numRooms == maxRooms) {
			Room[] newrooms = new Room[maxRooms + numExpand];
			
			System.arraycopy(rooms, 0, newrooms, 0, numRooms); // (array a (origem), posição do array a, array b (que queremos copiar do a para este), posição do array b, numero de arrays)
			rooms = newrooms;
		}
	
		rooms[numRooms] = r;
		numRooms++;
	}
	
	public int size() {
		return size;
	}
	
	public int maxSize() {
		int a = rooms.length;
		assert a>=8;
		return a;
	}
	
	//fazer funcao
	public Room room(int lel) {
	
	return rooms[lel];
	}
	  
	public int area() {
		
		
		for (int i=0; i < maxRooms; i++) {
			areatotal += rooms[i].area(); 
		}
		return areatotal;
	}
	
		// fazer funcao
	public RoomTypeCount[] getRoomTypeCounts() {
		
		RoomTypeCount[] rtc = new RoomTypeCount[rooms.length];
		int nt = 0; //numero de tipos diferentes
		
		for(int r = 0; r < numRooms; r++) {
			boolean encontrei = false;
			for(int t = 0; t < nt && !encontrei; t++) {
				if (rtc[t].roomType.equals(rooms[r].roomType())) {
					rtc[t].count++;
					encontrei = true;
				}
			}
		if (!encontrei) {
			rtc[nt] = new RoomTypeCount();
			rtc[nt].roomType = rooms[r].roomType();
			rtc[nt].count = 1;
			nt++;
		}
		}
		RoomTypeCount[] newrtc = new RoomTypeCount[nt];
		System.arraycopy(rtc, 0, newrtc, 0, nt);
		return newrtc;
	}
	
	public double averageRoomDistance() {
		int n=0;
		double areamedia=0;
		for (int i = 0; i < size; i++){
			for(int j = i+1; j < size; j++){
				areamedia = areamedia + (rooms[i].geomCenter().distTo(rooms[j].geomCenter()));
				n++;
			}
		}
		return areamedia/n;
	}
	
	private String type;
	private int maxRooms = 8, numExpand = 4;
	private Room[] rooms = new Room[maxRooms];
	private int numRooms = 0;
	private int areatotal=0;
	private int size;
}
	
