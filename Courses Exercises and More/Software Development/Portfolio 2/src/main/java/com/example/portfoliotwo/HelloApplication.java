package com.example.portfoliotwo;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.TextArea;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.text.Text;
import javafx.stage.Stage;

import java.sql.*;
public class HelloApplication extends Application {
    private Connection connection;
    private Text totalECTSText; //Decvlaring the totalECTSText variable

    @Override
    public void start(Stage stage) {
        //Establish connection to SQLite database
        connectToDatabase();

        totalECTSText = new Text("Total ECTS: 0");

        //Create ComboBoxes
        ComboBox<String> selectBox1 = new ComboBox<>();
        ComboBox<String> selectBox2 = new ComboBox<>();
        ComboBox<String> selectBox3 = new ComboBox<>();
        ComboBox<String> selectBox4 = new ComboBox<>();
        ComboBox<String> typeBox1 = new ComboBox<>();
        ComboBox<String> typeBox2 = new ComboBox<>();
        ComboBox<String> typeBox3 = new ComboBox<>();


        try {
            //Populate ComboBoxes with data from the database
            populateProgramComboBox(selectBox1);
            populateElectiveCoursesComboBox(selectBox4);
        } catch (SQLException e) {
            e.printStackTrace();
        }

        //Set initial box text
        selectBox1.setPromptText("Select program");
        selectBox2.setPromptText("Select subject");
        selectBox3.setPromptText("Select subject");
        selectBox4.setPromptText("Select subject");
        typeBox1.setPromptText("Select type");

        //Create TextArea
        TextArea textArea1 = new TextArea();
        TextArea textArea2 = new TextArea();
        TextArea textArea3 = new TextArea();
        TextArea textArea4 = new TextArea();

        //Set prompt texts and disable editing
        textArea1.setPromptText("Selected courses will be displayed here");
        textArea2.setPromptText("Selected courses will be displayed here");
        textArea3.setPromptText("Selected courses will be displayed here");
        textArea4.setPromptText("Selected courses will be displayed here");

        //making textArea non editable
        textArea1.setEditable(false);
        textArea2.setEditable(false);
        textArea3.setEditable(false);
        textArea4.setEditable(false);
        textArea1.setPrefHeight(200);
        textArea2.setPrefHeight(200);
        textArea3.setPrefHeight(200);
        textArea4.setPrefHeight(200);

        //Create Buttons for select
        Button selectButton1 = new Button("Select");
        Button selectButtontype = new Button("Select");
        Button selectButton2 = new Button("Select");
        Button selectButton3 = new Button("Select");
        Button selectButton4 = new Button("Select");

        //Create Buttons for add
        Button addButton1 = new Button("Add");
        Button addButton2 = new Button("Add");
        Button addButton3 = new Button("Add");
        Button addButton4 = new Button("Add");

        //Event listeners for buttons and ComboBoxes

        //If Program Select button pressed
        selectButton1.setOnAction(e -> {
            String selectedProgram = selectBox1.getValue(); //getting value from ComboBox
            if (selectedProgram != null) {
                try {
                    populateBasicCourseComboBox(typeBox1); //updates
                    populateITCategoryComboBox(selectBox2); //updating second and third ComboBoxes with Modules
                    populateCPCategoryComboBox(selectBox3); //2nd module
                } catch (SQLException ex) {
                    throw new RuntimeException(ex);
                }
            }
        });

        //if Add button is pressed in first column
        addButton1.setOnAction(e -> {
            String selectedCourse = typeBox1.getValue(); //getting value from above ComboBox
            if (selectedCourse != null) {
                String currentText = textArea1.getText();
                if (!currentText.isEmpty()) { //if not empty
                    textArea1.setText(currentText + "\n" + selectedCourse); //taking text that is already in textArea and adding new selected course
                } else {
                    textArea1.setText(selectedCourse);
                }
                typeBox1.getSelectionModel().clearSelection();

                try { //try to save the students selection and update the ects
                    storeStudentSelection(1, selectedCourse); //store selected course into databse
                    updateTotalECTS();
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
        });

        //rest of the button do pretty much the same thing
        selectButton2.setOnAction(e -> {
            String selectedProgram = selectBox2.getValue();
            if (selectedProgram != null) {
                try {
                    populateITCoursesComboBox(typeBox2);
                } catch (SQLException ex) {
                    throw new RuntimeException(ex);
                }
            }
        });

        addButton2.setOnAction(e -> {
            String selectedCourse = typeBox2.getValue();
            if (selectedCourse != null) {
                String currentText = textArea2.getText();
                if (!currentText.isEmpty()) {
                    textArea2.setText(currentText + "\n" + selectedCourse);
                } else {
                    textArea2.setText(selectedCourse);
                }
                typeBox2.getSelectionModel().clearSelection();

                try {
                    storeStudentSelection(1, selectedCourse);
                    updateTotalECTS();
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
        });

        selectButton3.setOnAction(e -> {
            String selectedProgram = selectBox3.getValue();
            if (selectedProgram != null) {
                try {
                    populateCPCoursesComboBox(typeBox3);
                } catch (SQLException ex) {
                    throw new RuntimeException(ex);
                }
            }
        });

        addButton3.setOnAction(e -> {
            String selectedCourse = typeBox3.getValue();
            if (selectedCourse != null) {
                String currentText = textArea3.getText();
                if (!currentText.isEmpty()) {
                    textArea3.setText(currentText + "\n" + selectedCourse);
                } else {
                    textArea3.setText(selectedCourse);
                }
                typeBox3.getSelectionModel().clearSelection();

                try {
                    storeStudentSelection(1, selectedCourse);
                    updateTotalECTS();
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
        });

        addButton4.setOnAction(e -> {
            String selectedCourse = selectBox4.getValue();
            if (selectedCourse != null) {
                String currentText = textArea4.getText();
                if (!currentText.isEmpty()) {
                    textArea4.setText(currentText + "\n" + selectedCourse);
                } else {
                    textArea4.setText(selectedCourse);
                }
                typeBox2.getSelectionModel().clearSelection();

                try {
                    storeStudentSelection(1, selectedCourse);
                    updateTotalECTS();
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
        });

        //The Layout out of our GUI. Each column of the GUI has its own column here so that it is easier to indentify and interact with.
        HBox root = new HBox();
        VBox column1 = new VBox();
        column1.getChildren().addAll(new Text("Program"), selectBox1, selectButton1, typeBox1, addButton1, textArea1, new Text("ECTS: "), totalECTSText); //only under row one we showcase the total ECTS.
        VBox column2 = new VBox();
        column2.getChildren().addAll(new Text("Subject 1"), selectBox2, selectButton2, typeBox2, addButton2, textArea2);
        VBox column3 = new VBox();
        column3.getChildren().addAll(new Text("Subject 2"), selectBox3, selectButton3, typeBox3, addButton3, textArea3);
        VBox column4 = new VBox();
        column4.getChildren().addAll(new Text("Elective"), selectBox4, addButton4, textArea4);
        root.getChildren().addAll(column1, column2, column3, column4);
        root.setSpacing(20);
        column1.setSpacing(10);
        column2.setSpacing(10);
        column3.setSpacing(10);
        column4.setSpacing(10);
        root.setPadding(new Insets(20));

        //creating a scene object
        Scene scene = new Scene(root, 1000, 500);

        //Create the Stage
        stage.setScene(scene);
        stage.setTitle("RUC University Registration Program");
        stage.show();

        //catch and show total ECTS initially
        updateTotalECTS();

        //Attempt to clear selections for student ID 1 alsotrying to catch and printing any SQL exception that may occur
        try {
            clearStudentSelections(1); // Clear selections for student ID 1
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }
    //Connection to the backend Database
    private void connectToDatabase() {
        String url = "jdbc:sqlite:identifier.sqlite"; // Replace with your actual database file path

        try {
            connection = DriverManager.getConnection(url);
            System.out.println("Connected to the database.");
        } catch (SQLException e) {
            System.out.println("Error connecting to the database: " + e.getMessage());
        }
    }
    //Populate Program title
    private void populateProgramComboBox(ComboBox<String> comboBox) throws SQLException {
        String query = "SELECT DISTINCT bprogramme_name FROM BACHELOR_PROGRAMME";

        try (PreparedStatement pstmt = connection.prepareStatement(query)) {
            ResultSet rs = pstmt.executeQuery();
            comboBox.getItems().clear();
            while (rs.next()) {
                comboBox.getItems().add(rs.getString("bprogramme_name"));
            }
        }
    }
    //Populate Basic courses
    private void populateBasicCourseComboBox(ComboBox<String> comboBox) throws SQLException {
        String query = "SELECT DISTINCT activity_name FROM STUDY_ACTIVITY WHERE category = 'Basic'";

        try (PreparedStatement pstmt = connection.prepareStatement(query)) {
            ResultSet rs = pstmt.executeQuery();
            comboBox.getItems().clear();
            while (rs.next()) {
                comboBox.getItems().add(rs.getString("activity_name"));
            }
        }
    }
    //Populate Informatics Title
    private void populateITCategoryComboBox(ComboBox<String> comboBox) throws SQLException {
        String query = "SELECT DISTINCT category FROM STUDY_ACTIVITY WHERE category = 'Informatics'";

        try (PreparedStatement pstmt = connection.prepareStatement(query)) {
            ResultSet rs = pstmt.executeQuery();
            comboBox.getItems().clear();
            while (rs.next()) {
                comboBox.getItems().add(rs.getString("Category"));
            }
        }
    }
    //Populate Informatics courses
    private void populateITCoursesComboBox(ComboBox<String> comboBox) throws SQLException {
        String query = "SELECT DISTINCT activity_name FROM STUDY_ACTIVITY WHERE category = 'Informatics'";

        try (PreparedStatement pstmt = connection.prepareStatement(query)) {
            ResultSet rs = pstmt.executeQuery();
            comboBox.getItems().clear();
            while (rs.next()) {
                comboBox.getItems().add(rs.getString("activity_name"));
            }
        }
    }
    //Populate Computer Science Title
    private void populateCPCategoryComboBox(ComboBox<String> comboBox) throws SQLException {
        String query = "SELECT DISTINCT category FROM STUDY_ACTIVITY WHERE category = 'Computer Science'";

        try (PreparedStatement pstmt = connection.prepareStatement(query)) {
            ResultSet rs = pstmt.executeQuery();
            comboBox.getItems().clear();
            while (rs.next()) {
                comboBox.getItems().add(rs.getString("Category"));
            }
        }
    }
    //Populate Computer Science courses
    private void populateCPCoursesComboBox(ComboBox<String> comboBox) throws SQLException {
        String query = "SELECT DISTINCT activity_name FROM STUDY_ACTIVITY WHERE category = 'Computer Science'";

        try (PreparedStatement pstmt = connection.prepareStatement(query)) {
            ResultSet rs = pstmt.executeQuery();
            comboBox.getItems().clear();
            while (rs.next()) {
                comboBox.getItems().add(rs.getString("activity_name"));
            }
        }
    }
    //Populate Elective courses
    private void populateElectiveCoursesComboBox(ComboBox<String> comboBox) throws SQLException {
        String query = "SELECT DISTINCT activity_name FROM STUDY_ACTIVITY WHERE category = 'Elective'";

        try (PreparedStatement pstmt = connection.prepareStatement(query)) {
            ResultSet rs = pstmt.executeQuery();
            comboBox.getItems().clear();
            while (rs.next()) {
                comboBox.getItems().add(rs.getString("activity_name"));
            }
        }
    }
    //Method to store the selection of the activities
    private void storeStudentSelection(int studentId, String activityName) throws SQLException {
        String insertQuery = "INSERT INTO StudentSelections (student_id, activity_name) VALUES (?, ?)";

        try (PreparedStatement pstmt = connection.prepareStatement(insertQuery)) {
            pstmt.setInt(1, studentId); // Set studentId at index 1
            pstmt.setString(2, activityName); // Set activityName at index 2
            pstmt.executeUpdate();
        }
    }
    //method to clear
    private void clearStudentSelections(int studentId) throws SQLException {
        String deleteQuery = "DELETE FROM StudentSelections WHERE student_id = ?";

        try (PreparedStatement pstmt = connection.prepareStatement(deleteQuery)) {
            pstmt.setInt(1, studentId);
            pstmt.executeUpdate();
        }
    }

    //in this method retrieves the total ECTS credits chosen by a student from the database and updates the display accordingly
    private void updateTotalECTS() {
        String query = "SELECT SUM(s.ects_weight) AS total_chosen_ects " +
                "FROM StudentSelections ss " +
                "JOIN STUDY_ACTIVITY s ON ss.activity_name = s.activity_name " +
                "WHERE ss.student_id = 1";

        try (PreparedStatement pstmt = connection.prepareStatement(query)) {
            ResultSet rs = pstmt.executeQuery();
            if (rs.next()) {
                int totalECTS = rs.getInt("total_chosen_ects");
                totalECTSText.setText("Total ECTS: " + totalECTS);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        launch();
    }
}