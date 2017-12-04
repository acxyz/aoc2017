package ac.day3;

import java.util.*;
import java.util.stream.*;
import static ac.utility.artPrint.print;




public class Grid {
	

	
	enum direction {
		right,
		up,
		left,
		down
	}
	
	
	private ArrayList<Cell> cells; 
	
	private int max_x, min_x, max_y, min_y;
	private int curr_x, curr_y;
	private direction currDirection;
	
	private int testValue;
	
	public Grid(int value) {
		initializeGrid();
		testValue = value;
	}
		
	private void initializeGrid() {
		max_x = 0;
		max_y = 0;
		min_x = 0;
		min_y = 0;
		curr_x = 0;
		curr_y = 0;
		currDirection = direction.right;
		cells = new ArrayList<>();
	}
	
	/* METHODS TO POPULATE GRID */
	
	public void makeCellsConsecutively() { // phase 1
		makeCellsConsecutively(this.testValue);
	}
	
	public void makeCellsToTargetValue() { // phase 2
		makeCellsToTargetValue(this.testValue);
	}
	
	/* PHASE 1 */
	
	private void makeCellsConsecutively(int value) { // phase 1
		initializeGrid();
		addInitialCell(1);
		for(int i = 2 ; i <= value ; i++) {
			addCellAtNextLocation(i);
		}
	}



	/* PHASE 2 */
	
	private void makeCellsToTargetValue(int target) {
		initializeGrid();
		addInitialCell(1);
		int nextValue = 1;
		while (nextValue <= target) {
			setNextCoordinates();
			nextValue = getAdjacentValues();
			addCellAtCurrentLocation(nextValue);
		} 			
	}
	
	private void addCellAtNextLocation(int v) {
		setNextCoordinates();
		addCellAtCurrentLocation(v);
	}
	
	private void addCellAtCurrentLocation(int v) {
		cells.add(new Cell(v, curr_x, curr_y));
	}
	
	private void addInitialCell(int v) {
		cells.add(new Cell(v,0,0));
	}
	
	private int getAdjacentValues() {
		// for now, just read through whole list although this is not efficient.
		int total = 0;
		for (Cell c : cells) {
			if (Math.abs(c.getX() - curr_x) <= 1 &&
				Math.abs(c.getY() - curr_y) <= 1) {
				total += c.getValue();
			}
		}
		return total;
	}
	
	private void setNextCoordinates() {
		if (currDirection == direction.right) {
			curr_x++;
			if (curr_x > max_x) {
				max_x = curr_x;
				currDirection = direction.up;
			}
		} else if (currDirection == direction.up) {
			curr_y++;
			if (curr_y > max_y) {
				max_y = curr_y;
				currDirection = direction.left;
			}
		} else if (currDirection == direction.left) {
			curr_x--;
			if (curr_x < min_x) {
				min_x = curr_x;
				currDirection = direction.down;
			}
		} else {
			curr_y--;
			if (curr_y < min_y) {
				min_y = curr_y;
				currDirection = direction.right;
			}
		}
	}
	
	/* END OF METHODS TO POPULATE GRID */
	
	
	



	/* 
		RETURN VALUE FUNCTIONS
	*/
	
	public int distanceToPort() { // PHASE 1
		return Math.abs(curr_x) + Math.abs(curr_y);
	}
	
	public int getMaxValue() { // PHASE 2 and other uses
		// assumes that each cell is >= the previous
		if (!cells.isEmpty()) {
			Cell last = cells.get(cells.size() - 1);
			return last.getValue();
		} else {
			throw new IndexOutOfBoundsException();
		}
	}
	

	
	/*
		DRAW FUNCTIONS
	*/
	public void draw() { 
		print(this.toString());
	}
	public String toString() {
		StringBuilder sb = new StringBuilder();
		for (int j = max_y ; j >= min_y ; j--) {
			for (int i = min_x ; i <= max_x ; i ++) {
				Cell c = get(i,j);
				if (c == null) { 
					for (int k = 0 ; k <= this.numDigits() ; k++) {
						sb.append(" ");
					}
				} else {
					sb.append(c.toString(this.numDigits()) + " ");
				}
			}
			sb.append("\n");
		}
		
		// sb.append("\n");
		// sb.append(" * * * ");			
		// sb.append("\n");
		
		// for(Cell c : cells) {
			// sb.append(Integer.toString(c.getValue()) + " [" + Integer.toString(c.getX()) + "," + Integer.toString(c.getY()) + "]\n");
		// }
		return sb.toString();
	}
	
	/*
		MISC FUNCTIONS
	*/
	public int count() {
		return cells.size();
	}
	public int numDigits() { // size of largest (last) member
		return Integer.toString(this.getMaxValue()).length();
	}
	
	private Cell get(int x, int y) {

		List<Cell> filteredCells = cells.stream().filter(c -> c.getY() == y && c.getX()	 == x).collect(Collectors.toList());
		
		if (filteredCells.size() > 1) {
			throw new RuntimeException("Invalid grid: duplicate cell coordinates");
		} else if (filteredCells.size() < 1) {
			return null;
		} else {
			return filteredCells.get(0);
		}
	}
		
}







