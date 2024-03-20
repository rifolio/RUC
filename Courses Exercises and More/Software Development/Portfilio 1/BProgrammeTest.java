import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class BProgrammeTest {

    @Test
    public void testAllConditionsMet() {
        // setting up new programme
        BProgramme programme = new BProgramme();

        // correct amount of courses and projects in the programme
        programme.addActivity(9, "Basic Course", "Natural Science");
        programme.addActivity(4, "Module Course5", "Mathematics");
        programme.addActivity(2, "Module Course10", "Mathematics");
        programme.addActivity(1, "Elective Course", "Bread Studies");
        programme.addActivity(3, "Basic Project", "Natural Science");
        programme.addActivity(2, "Module Project", "Physics");
        programme.addActivity(1, "Bachelor Project", "Computer Science");

        // check if the valid() can detect correct input with all conditions met
        assertTrue(programme.valid());
    }

    @Test
    public void test180TotalECTSButNotMeetingOtherConditions() {
        BProgramme programme = new BProgramme();

        //adding differrent amount of courses and project that sumup to 180, but do not satisfies conditoins
        programme.addActivity(1, "Basic Course", "Natural Science");
        programme.addActivity(1, "Module Course5", "Mathematics");
        programme.addActivity(7, "Module Course10", "Mathematics");
        programme.addActivity(2, "Elective Course", "Bread Studies");
        programme.addActivity(1, "Basic Project", "Natural Science");
        programme.addActivity(3, "Module Project", "Physics");
        programme.addActivity(2, "Bachelor Project", "Computer Science");

        assertEquals(180, programme.calculateTotalECTS());
        assertFalse(programme.valid());
    }

    @Test
    public void testLessThan90ECTSCreditsForCourses() {
        BProgramme programme = new BProgramme();

        //less courses ECTS than expected. Also do not satisfy number of types
        programme.addActivity(1, "Basic Course", "Natural Science");
        programme.addActivity(2, "Module Course10", "Business Studies");

        assertNotEquals(90, programme.calculateTotalECTS());
        assertFalse(programme.valid());
    }

    @Test
    public void testLessThan90ECTSCreditsForProjects() {
        BProgramme programme = new BProgramme();

        //less projects ECTS than expected. Also do not satisfy number of types
        programme.addActivity(3, "Basic Project", "Computer Science");

        assertNotEquals(90, programme.calculateTotalECTS());
        assertFalse(programme.valid());
    }

    @Test
    public void testMoreThan90ECTSCreditsForCourses() {
        BProgramme programme = new BProgramme();

        //more courses ECTS than expected. Also do not satisfy number of types
        programme.addActivity(33, "Module Course5", "Computer Science");

        assertNotEquals(90, programme.calculateTotalECTS());
        assertFalse(programme.valid());
    }

    @Test
    public void testMoreThan90ECTSCreditsForProjects() {
        BProgramme programme = new BProgramme();

        //more projects ECTS than expected. Also do not satisfy number of types
        programme.addActivity(12, "Module Project", "Computer Science");

        assertNotEquals(90, programme.calculateTotalECTS());
        assertFalse(programme.valid());
    }


    @Test
    public void testWrongNumberOfModuleCourses() {
        BProgramme programme = new BProgramme();

        // incorrect amount of courses and projects in the programme
        programme.addActivity(9, "Basic Course", "Natural Science");
        programme.addActivity(2, "Module Course5", "Mathematics"); //adding less module courses than allowed
        programme.addActivity(3, "Module Course10", "Mathematics"); //same totalECTS value
        programme.addActivity(1, "Elective Course", "Bread Studies");
        programme.addActivity(3, "Basic Project", "Natural Science");
        programme.addActivity(2, "Module Project", "Physics");
        programme.addActivity(1, "Bachelor Project", "Computer Science");

        // check if the valid() can detect incorrect input
        assertEquals(180, programme.calculateTotalECTS());
        assertFalse(programme.valid());
    }

    @Test
    public void testWrongNumberOfElectiveCourses() {
        BProgramme programme = new BProgramme();

        // incorrect amount of elective coursesin the programme
        programme.addActivity(9, "Basic Course", "Natural Science");
        programme.addActivity(4, "Module Course5", "Mathematics"); //changing number of Module to keep the same totalECTS value
        programme.addActivity(2, "Module Course10", "Mathematics");
        programme.addActivity(2, "Elective Course", "Bread Studies"); //one more elective. Higher same totalECTS value
        programme.addActivity(3, "Basic Project", "Natural Science");
        programme.addActivity(2, "Module Project", "Physics");
        programme.addActivity(1, "Bachelor Project", "Computer Science");

        // Check if the valid() can detect incorrect input
        assertNotEquals(180, programme.calculateTotalECTS());
        assertFalse(programme.valid());
    }
    
    @Test
    public void testBasicCoursesCountLessThan9() {
        BProgramme programme = new BProgramme();
        
        programme.addActivity(8, "Basic Course", "Natural Science"); //one less here
        programme.addActivity(4, "Module Course5", "Mathematics");
        programme.addActivity(2, "Module Course10", "Mathematics");
        programme.addActivity(1, "Elective Course", "Bread Studies");
        programme.addActivity(3, "Basic Project", "Natural Science");
        programme.addActivity(2, "Module Project", "Physics");
        programme.addActivity(1, "Bachelor Project", "Computer Science");
        assertFalse(programme.valid());
    }

    @Test
    public void testBasicProjectsCountLessThan3() {
        BProgramme programme = new BProgramme();
        
        programme.addActivity(9, "Basic Course", "Natural Science");
        programme.addActivity(4, "Module Course5", "Mathematics");
        programme.addActivity(2, "Module Course10", "Mathematics");
        programme.addActivity(1, "Elective Course", "Bread Studies");
        programme.addActivity(2, "Basic Project", "Natural Science");
        programme.addActivity(2, "Module Project", "Physics");
        programme.addActivity(1, "Bachelor Project", "Computer Science"); //less here
        assertFalse(programme.valid());
    }

    @Test
    public void testModuleProjectsCountNot2() {
        BProgramme programme = new BProgramme();
        
        programme.addActivity(9, "Basic Course", "Natural Science");
        programme.addActivity(4, "Module Course5", "Mathematics");
        programme.addActivity(2, "Module Course10", "Mathematics");
        programme.addActivity(1, "Elective Course", "Bread Studies");
        programme.addActivity(3, "Basic Project", "Natural Science");
        programme.addActivity(1, "Module Project", "Physics"); //less here
        programme.addActivity(1, "Bachelor Project", "Computer Science");
        assertFalse(programme.valid());
    }

    @Test
    public void testBachelorProjectsCountNot1() {
        BProgramme programme = new BProgramme();
        
        programme.addActivity(9, "Basic Course", "Natural Science");
        programme.addActivity(4, "Module Course5", "Mathematics");
        programme.addActivity(2, "Module Course10", "Mathematics");
        programme.addActivity(1, "Elective Course", "Bread Studies");
        programme.addActivity(3, "Basic Project", "Natural Science");
        programme.addActivity(2, "Module Project", "Physics");
        programme.addActivity(0, "Bachelor Project", "Computer Science"); //no bc project

        assertFalse(programme.valid());
    }

//    @Test
//    public void testCorrectCountsButECTSDistributionIncorrect() {
//        BProgramme programme = new BProgramme();
//        // Add activities with correct counts but incorrect ECTS distribution
//        // ...
//        assertFalse(programme.valid());
//    }
}