//abstract class representing a course
abstract class Course extends StudyActivity {
    public Course(String type, int ects, String department, String name) {
        super(ects, type, name, department);
    }
}

//specific course classes
class BasicCourse extends Course {
    public BasicCourse(String type, int ects, String department, String name) {
        super(type, ects, department, name);
    }
}

class SubjectModuleCourse extends Course {
    public SubjectModuleCourse(String type, int ects, String department, String name) {
        super(type, ects, department, name);
    }
}

class ElectiveCourse extends Course {
    public ElectiveCourse(String type, int ects, String department, String name) {
        super(type, ects, department, name);
    }
}