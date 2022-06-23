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

public class Main7 extends Application {
	TextField tf1;
	TextField tf2;
	TextField tf3;

	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox) FXMLLoader.load(getClass().getResource("main7.fxml"));

			Scene scene = new Scene(root, 400, 400);

			Button btn = (Button) scene.lookup("#btn");
			tf1 = (TextField) scene.lookup("#tfMine");
			tf2 = (TextField) scene.lookup("#tfCom");
			tf3 = (TextField) scene.lookup("#tfResult");

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
			tf3.setText("비김");
		} else if ((com.equals("가위") && user.equals("바위")) || (com.equals("바위") && user.equals("보"))
				|| (com.equals("보") && user.equals("가위"))) {
			tf3.setText("이김");
		} else {
			tf3.setText("짐");
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
