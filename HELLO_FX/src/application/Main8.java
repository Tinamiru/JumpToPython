package application;

import java.util.Random;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;

public class Main8 extends Application {
	TextField tf1;
	TextField tf2;
	TextArea ta;

	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox) FXMLLoader.load(getClass().getResource("main8.fxml"));

			Scene scene = new Scene(root, 400, 400);

			Button btn = (Button) scene.lookup("#btn");
			tf1 = (TextField) scene.lookup("#tf1");
			tf2 = (TextField) scene.lookup("#tf2");
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
		int first = Integer.parseInt(tf1.getText());
		int second = Integer.parseInt(tf2.getText());
		ta.clear();
		ta.setText("");
		
		for (int i = first; i <= second; i++) {
			String star = "";
			for (int j = 0; j < i; j++) {
				star += "*";
			}
			ta.appendText(star+"\n");
		}
	}

	public String comChoise() {
		Random ran = new Random();
		int ranNum = ran.nextInt(3) + 1;
		String result = "";
		switch (ranNum) {
		case 1:
			result = "가위";
			break;
		case 2:
			result = "바위";
			break;
		case 3:
			result = "보";
			break;
		}

		return result;
	}

	public static void main(String[] args) {
		launch(args);
	}
}
