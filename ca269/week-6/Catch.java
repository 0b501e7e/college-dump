public class Catch
{
    public static void main(String [] args)
    {
        try{
           Broken broke = new Broken();

        System.out.println("Testing");
        broke.cracked(); 
        }
        catch(ArrayIndexOutOfBoundsException a) {
            System.out.println("ArrayIndexOutOfBoundsException");
        }
        catch(NullPointerException n) {
            System.out.println("NullPointerException");
        }
        catch(ArithmeticException c) {
            System.out.println("ArithmeticException");
        }
        finally {
            System.out.println("Finally!");
        }
        
        
    }
}