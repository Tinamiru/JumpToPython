package application;

import java.util.ArrayList;
import java.util.Random;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;

public class Main9 extends Application {
	ArrayList<Button> btn;
	TextField tf;

	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox) FXMLLoader.load(getClass().getResource("main9.fxml"));

			Scene scene = new Scene(root, 400, 400);

			// 10개의 버튼 lookup
			btn = new ArrayList();
			Button btn_call = (Button) scene.lookup("#btn_call");
			tf = (TextField) scene.lookup("#tf");

			for (int i = 0; i < 10; i++) {
				String btnNum = "#btn" + i;
				btn.add((Button) scene.lookup(btnNum));
			}

				btn.get(0).setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {myclick(event);}});
				btn.get(1).setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {myclick(event);}});
				btn.get(2).setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {myclick(event);}});
				btn.get(3).setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {myclick(event);}});
				btn.get(4).setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {myclick(event);}});
				btn.get(5).setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {myclick(event);}});
				btn.get(6).setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {myclick(event);}});
				btn.get(7).setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {myclick(event);}});
				btn.get(8).setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {myclick(event);}});
				btn.get(9).setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {myclick(event);}});
				
				btn_call.setOnMouseClicked(new EventHandler<Event>() { public void handle(Event event) { mycall(); }	 });

			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public void mycall() {
		String str_tel = tf.getText();
		Alert alert = new Alert(AlertType.INFORMATION);
		alert.setTitle("phone");
		alert.setHeaderText("calling");
		alert.setContentText(str_tel);
		alert.showAndWait();

	}

	public void myclick(Event event) {
		String str_old = tf.getText();
		Button b = (Button) event.getSource();
		String str_new = b.getText();
		tf.setText(str_old + str_new);
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
