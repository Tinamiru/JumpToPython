package application;

import javafx.application.Application;
import javafx.event.*;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;

public class Main4 extends Application {
	TextField tf;
	TextArea ta;

	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox) FXMLLoader.load(getClass().getResource("main4.fxml"));

			Scene scene = new Scene(root, 400, 400);

			Button btn = (Button) scene.lookup("#btn");
			tf = (TextField) scene.lookup("#tf");
			ta = (TextArea) scene.lookup("#ta");

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
		ta.clear();
		String a = tf.getText();
		int aa = Integer.parseInt(a);
		for (int i = 1; i <= 9; i++) {
			ta.appendText(aa + " * " + i + " = " + (aa * i));
			ta.appendText("\n");
		}
	}

	public static void main(String[] args) {
		launch(args);
	}
}
