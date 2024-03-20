//abstract class representing a project
abstract class Project extends StudyActivity {

    public Project(String type, String department, String name) {
        super(15, type, name, department); // Fixed ECTS value to 15
    }
}

//specific project classes
class BachelorProject extends Project {
    public BachelorProject(String type, String department, String name) {
        super(type, department, name);
    }
}

class SubjectModuleProject extends Project {
    public SubjectModuleProject(String type, String department, String name) {
        super(type, department, name);
    }
}

class BasicProject extends Project {
    public BasicProject(String type, String department, String name) {
        super(type, department, name);
    }
}
