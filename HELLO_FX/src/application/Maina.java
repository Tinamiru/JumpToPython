package application;

import java.util.Random;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;

public class Maina extends Application {
	TextField from;
	TextField to;
	TextField powNum;
	TextField result;

	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox) FXMLLoader.load(getClass().getResource("maina.fxml"));
			Scene scene = new Scene(root, 400, 400);

			from = (TextField) scene.lookup("#tf1");
			to = (TextField) scene.lookup("#tf2");
			powNum = (TextField) scene.lookup("#tf3");
			result = (TextField) scene.lookup("#tf4");

			Button btn = (Button) scene.lookup("#btn");

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
		result.clear();

		int fromNum = Integer.parseInt(from.getText());
		int toNum = Integer.parseInt(to.getText());
		int pn = Integer.parseInt(powNum.getText());
		int result = 0;

		for (int i = fromNum; i <= toNum; i++) {
			if (i % pn == 0) {
				result += i;
			}
		}
		this.result.setText(result + "");

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
