package application;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.*;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;

public class Main extends Application {
	Label lbl;
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox) FXMLLoader.load(getClass().getResource("hello.fxml"));

			Scene scene = new Scene(root, 400, 400);

			Label lbl = (Label) scene.lookup("#lbl");
			Button button = (Button) scene.lookup("#btn");
        	
			button.setOnMouseClicked(new EventHandler<Event>() {
	            @Override
	            public void handle(Event e) {
	            	lbl.setText("Good Evening");
	            }
	        });
			
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) {
		launch(args);
	}
}
