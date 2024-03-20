    import java.util.Iterator;
    import java.util.List;

    public class Main {
        public static void main(String[] args) {
            // Create a new BProgramme
            BProgramme programme = new BProgramme();

            // Add chosen activities to the programme
            programme.addActivity(9, "Basic Course", "Natural Science");
            programme.addActivity(4, "Module Course5", "Mathematics");
            programme.addActivity(2, "Module Course10", "Mathematics");
            programme.addActivity(1, "Elective Course", "Gender Studies");
            programme.addActivity(3, "Basic Project", "Natural Science");
            programme.addActivity(2, "Module Project", "Physics");
            programme.addActivity(1, "Bachelor Project", "Computer Science");


            if (programme.valid()) {

                // Retrieve the list of activities
                List<StudyActivity> activities = programme.getActivities();

                // Print information for each activity
                for (StudyActivity activity : activities) {
                    System.out.println("Name: " + activity.getName());
                    System.out.println("Type: " + activity.getType());
                    System.out.println("ECTS: " + activity.getECTS());
                    System.out.println("Department: " + activity.getDepartment());
                    System.out.println("___________________________________\n\n");
                }

                // Calculate total ECTS
                int totalECTS = programme.calculateTotalECTS();
                System.out.println("Total ECTS: " + totalECTS);
            }else {
                System.out.println("Something went wrong, Valid() = " + programme.valid());
            }
        }
    }
