module com.example.portfoliotwo {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;


    opens com.example.portfoliotwo to javafx.fxml;
    exports com.example.portfoliotwo;
}