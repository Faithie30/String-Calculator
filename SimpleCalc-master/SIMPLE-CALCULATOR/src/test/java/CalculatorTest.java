
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class CalculatorTest {
    @Test
    void testAddition(){
        assertEquals(6, Calculator.add(1,2,3));
    }

    @Test
    void testAddition2(){
        assertEquals(6, Calculator.add(4,2));
    }
    @Test
    void testMulti(){
        assertEquals(6, Calculator.multiply(2,3));
    }

    @Test
    void testMulti2(){
        assertEquals(6, Calculator.multiply(1,2,3));
    }

}
