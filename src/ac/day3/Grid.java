package ac.day3;

import java.util.*;
import java.util.stream.*;
// import java.lang.Math;
import static ac.utility.artPrint.print;




public class Grid {
	

	
	enum direction {
		right,
		up,
		left,
		down
	}
	
	
	private ArrayList<Cell> cells = new ArrayList<>();
	
	private int max_x, min_x, max_y, min_y;
	private int curr_x, curr_y;
	private direction currDirection;
	
	public int getMaxValue() {
		if (!cells.isEmpty()) {
			Cell last = cells.get(cells.size() - 1);
			return last.getValue();
		} else {
			throw new IndexOutOfBoundsException();
		}
	}
	
	public Grid(int value) {
		initializeGrid();
		makeCells(value);
	}
	
	static Grid gridVersionTwo(int targetMaxValue) {
		Grid g = new Grid();
		g.makeCellsToTargetValue(targetMaxValue);
		return g;
	}

	public Grid() {
		initializeGrid();
	}
	
	private void makeCells(int value) { // phase 1
		for(int i = 1 ; i <= value ; i++) {
			cells.add(makeCell(i));
		}
	}

	private Cell makeCell(int value) {
		if (value == 1) {
			return new Cell(value,0,0);
		} else {
			return getNextCell(value);
		}
	}
	
	private void makeCellsToTargetValue(int target) {
		initializeGrid();
		cells.add(new Cell(1,0,0));
		int nextValue;
		do {
			setNextCoordinates();
			nextValue = getAdjacentValues();
			// if (nextValue <= target) {
				cells.add( new Cell(nextValue, curr_x, curr_y) );
			// }
		} while (nextValue <= target);			
	}
	
	private int getAdjacentValues() {
		// for now, just read through whole list although this is not efficient.
		
		// print ("Current: [" + Integer.toString(curr_x) + "," + Integer.toString(curr_y) + "]");
		int total = 0;
		for (Cell c : cells) {
			if (Math.abs(c.getX() - curr_x) <= 1 &&
				Math.abs(c.getY() - curr_y) <= 1) {
				total += c.getValue();
			}
		}
		// print ("Total: " + Integer.toString(total));
		return total;
	}
	
	private void initializeGrid() {
		max_x = 0;
		max_y = 0;
		min_x = 0;
		min_y = 0;
		curr_x = 0;
		curr_y = 0;
		currDirection = direction.right;
	}
	
	private Cell getNextCell(int value) {
		setNextCoordinates();
		return new Cell(value, curr_x, curr_y);
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

	public int distanceToPort() {
		return Math.abs(curr_x) + Math.abs(curr_y);
	}
	
	private Cell get(int x, int y) {
		//  List<User> olderUsers = users.stream().filter(u -> u.age > 30).collect(Collectors.toList());
		 List<Cell> filteredCells = cells.stream().filter(c -> c.getY() == y && c.getX()	 == x).collect(Collectors.toList());
		if (filteredCells.size() > 1) {
			throw new RuntimeException("Invalid grid: duplicate cell coordinates");
		} else if (filteredCells.size() < 1) {
			return null;
		} else {
			return filteredCells.get(0);
		}
	}
	
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
	
	public int count() {
		return cells.size();
	}
	public int numDigits() {
		return Integer.toString(this.getMaxValue()).length();
	}
		
}







