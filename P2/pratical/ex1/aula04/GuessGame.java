import static java.lang.System.*;

public class GuessGame
{
	private int min;
	private int max;
	int secretNumber;
	int last;
	int count = 0;
	
	public GuessGame (int min, int max) {
		this.min = min;
		this.max = max;
		secretNumber = (int) (Math.random() * (max - min + 	1) + min);  
		last = min - 1;
	}
	
	public int min() { return this.min; }
	public int max() { return this.max; }
	
	public boolean validAttempt(int num) {
		if (num == max || num == min) {
		return true;
		} else return false;
	}
	
	public boolean finished() {
		return last  == secretNumber;
	}
	
	public void play(int n) {
		assert validAttempt(n);
		assert finished() == false;
		count ++;
	}
	
	public boolean attemptIsHigher() {
		if (last > secretNumber) {
			return true;
		} else return false;
	}
	
	public boolean attemptIsLower() {
		if ( last < secretNumber) {
			return true;
		} else return false;
	} 
    
    public int numAttempts() {
	return count;
	}
   
   
   public static void main(String[] args)
   {
      out.println("Starting test.");
      GuessGame game = new GuessGame(1,10);
      assert !game.finished();
      assert game.min() == 1;
      assert game.max() == 10;
      assert game.numAttempts() == 0;
      assert !game.validAttempt(0) && !game.validAttempt(11);
      int n = 5;
      if(n == game.secretNumber)
         n++;
      game.play(n);
      assert game.numAttempts() == 1;
      assert n < game.secretNumber == game.attemptIsLower() || n > game.secretNumber && game.attemptIsHigher();
      game.play(game.secretNumber);
      assert game.numAttempts() == 2;
      assert game.finished();
      out.println("No error detected!");
   }
}

