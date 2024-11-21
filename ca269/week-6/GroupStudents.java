public class GroupStudents
{
   public static void main(String [] args)
   {
      Student [] group = {
         new Student("John", 50),
         new Student("Abby", 40),
         new Student("Dylan", 20),
         new Student("Carl", 70),
         new Student("Maeve", 73),
         new Student("Chris", 69),
         new Student("James", 55),
         new Student("Anne", 13)
               
            };

      double passingAverage = Test.getPassingAverage(group);
      System.out.println("The average mark of all students who passed is " + passingAverage);
   }
}