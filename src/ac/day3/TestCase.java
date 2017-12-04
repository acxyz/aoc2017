package ac.day3;


class TestCase {

	private int input;
	private int phase_1_result;
	private int phase_2_result;

	public int getInputValue() {
		return this.input;
	}
	
	public int getP1() {
		return this.phase_1_result;
	}
	
	public int getP2() {
		return this.phase_2_result;
	}
	
	public TestCase(int input, int p1, int p2) {
		this.input = input;
		this.phase_1_result = p1;
		this.phase_2_result = p2;
	}
}





