package ac.day3;

public class Cell {
	private int value;
	private int x;
	private int y;
	
	public int getValue() {
		return value;
	}
	public String toString(int numDigits) {
		return String.format("%" + Integer.toString(numDigits) + "s",Integer.toString(this.value));
	}
	public int getX() {
		return x;
	}
	public int getY() {
		return y;
	}
	
	public Cell(int value, int x, int y) {
		this.value = value;
		this.x = x;
		this.y = y;
	}
}
