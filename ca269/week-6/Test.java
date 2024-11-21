public class Test
{
   public static double getPassingAverage(Student [] student)
   {
       double totalMarks = 0;
       int passingStudents = 0;
       double average;
      for(int i = 0; i < student.length; i++) {

        if (student[i].getMark() >= 40) {
           totalMarks += student[i].getMark();
           passingStudents += 1;
        }
         
    }
    average = totalMarks / passingStudents;
    return average;


    }
}