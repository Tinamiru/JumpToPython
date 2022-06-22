package application;

import javafx.application.Application;
import javafx.event.*;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;

public class Main2 extends Application {
	TextField tf;

	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox) FXMLLoader.load(getClass().getResource("main2.fxml"));
			
			Scene scene = new Scene(root, 400, 400);

			Button btn = (Button) scene.lookup("#btn");
			tf = (TextField) scene.lookup("#tf");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myclick();
				}
			});

			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void myclick() {
		String a = tf.getText();
		int aa = Integer.parseInt(a);
		aa++;
		tf.setText(aa + "");
	}

	public static void main(String[] args) {
		launch(args);
	}
}
