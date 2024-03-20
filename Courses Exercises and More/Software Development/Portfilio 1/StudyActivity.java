//abstract class representing a study activity
abstract class StudyActivity {
    // constants
    protected int ects;
    protected String type;
    protected String name;
    public String department;

    public StudyActivity(int ects, String type, String name, String department) { //creating a constructor
        this.ects = ects;
        this.type = type;
        this.name = name;
        this.department = department;
    }

    public int getECTS() { // getter for ECTS
        return ects;
    }

    public String getType() { // getter for Type
        return type;
    }

    public String getName() { // getter for Name
        return name;
    }

    public String getDepartment() { // getter for Department
        return department;
    }
}