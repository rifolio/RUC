import java.util.ArrayList;
import java.util.List;

//class representing a bachelor programme
class BProgramme {
    private List<StudyActivity> activities; //list of activities
    private int bCourseCounter = 0; //counter for Basic Courses
    private int eCourseCounter = 0; //elective
    private int mCourseCounter = 0; //module
    private int bProjectCounter = 0;
    private int mProjectsCounter = 0;
    private int bcProjectCounter = 0;
    private int totalECTSCourses = 0;
    private int totalECTSProjects = 0;
    private int totalECTSbCourse = 0;
    private int totalECTSmCourse = 0;
    private int totalECTSeCourse = 0;

    public BProgramme() {
        activities = new ArrayList<>();
    }

    public void addActivity(int n, String type, String department) {
        for (int i = 0; i < n; i++) {
            StudyActivity activity = createActivity(type, department);
            if (activity != null) {
                activities.add(activity);
            }
        }
    }

    //switch statement to create 7 different types of study activities
    private StudyActivity createActivity(String type, String department) {
        switch (type) {
            case "Basic Course":
                bCourseCounter++; //increasing counter of activity type
                return new BasicCourse("Basic Course", 5, department, "Basic Course " + bCourseCounter);

            case "Module Course5": //Module course with 5 ECTS
                mCourseCounter++;
                return new SubjectModuleCourse("Module Course", 5, department, "Module Course " + mCourseCounter);

            case "Module Course10": //Module course with 10 ECTS
                mCourseCounter++;
                return new SubjectModuleCourse("Module Course", 10, department, "Module Course " + mCourseCounter);

            case "Elective Course":
                eCourseCounter++;
                return new ElectiveCourse("Elective Course", 5, department, "Elective Course " + eCourseCounter);

            case "Basic Project":
                bProjectCounter++;
                return new BasicProject("Basic Project", department, "Basic Project " + bProjectCounter);

            case "Module Project":
                mProjectsCounter++;
                return new SubjectModuleProject("Module Project", department, "Module Project " + mProjectsCounter);

            case "Bachelor Project":
                bcProjectCounter++;
                return new BachelorProject("Bachelor Project", department, "Bachelor Project");
            default:
                System.out.println("Invalid activity type: " + type);
                return null;
        }
    }

    //calculating total ECTS poinst over the whole StudyActivities list
    public int calculateTotalECTS() {
        int totalECTS = 0;
        for (StudyActivity activity : activities) {
            totalECTS += activity.getECTS();
        }
        return totalECTS;
    }

    public List<StudyActivity> getActivities() { //getter for StudyActivities
        return activities;
    }

    public void pointsCounter(){ //getting ECTS points for different activity types
        for (StudyActivity activity : activities) {
            if (activity instanceof Course) {
                totalECTSCourses += activity.getECTS();
            }
            if (activity instanceof BasicCourse) {
                totalECTSbCourse += activity.getECTS();
            }

            if (activity instanceof SubjectModuleCourse) {
                totalECTSmCourse += activity.getECTS();
            }

            if (activity instanceof ElectiveCourse) {
                totalECTSeCourse += activity.getECTS();
            }
            if (activity instanceof Project) {
                totalECTSProjects += activity.getECTS();
            }
        }
    }
    public boolean valid() {
        //call ECTS values
        pointsCounter();

        //check if all conditions are met
        if (totalECTSbCourse == 45 && totalECTSCourses == 90 && totalECTSProjects == 90 && totalECTSmCourse >= 40 && bCourseCounter == 9 && eCourseCounter == 1 && (mCourseCounter >= 6 && mCourseCounter <= 8) && bProjectCounter == 3 && mProjectsCounter == 2 && bcProjectCounter == 1) {
            return true;
        }

        //if any condition is not met, return false
        return false;
    }
}