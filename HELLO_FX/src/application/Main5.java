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
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;

public class Main5 extends Application {
	TextField tf1;
	TextField tf2;
	TextField tf3;

	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox) FXMLLoader.load(getClass().getResource("main5.fxml"));

			Scene scene = new Scene(root, 400, 400);

			Button btn = (Button) scene.lookup("#btn");
			tf1 = (TextField) scene.lookup("#tf_mine");
			tf2 = (TextField) scene.lookup("#tf_com");
			tf3 = (TextField) scene.lookup("#tf_result");

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
		String com = comChoise();
		String user = tf1.getText();
		tf2.setText(com);

		if (com.equals(user)) {
			tf3.setText("이김");
		} else {
			tf3.setText("짐");
		}

	}

	public String comChoise() {
		Random ran = new Random();
		int ranNum = ran.nextInt(2) + 1;
		String result = "";
		switch (ranNum) {
		case 1:
			result = "홀";
			break;
		case 2:
			result = "짝";
			break;
		}

		return result;
	}

	public static void main(String[] args) {
		launch(args);
	}
}
