package application;

import java.util.*;

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

public class Main6 extends Application {
	Label lbl1;
	Label lbl2;
	Label lbl3;
	Label lbl4;
	Label lbl5;
	Label lbl6;

	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox) FXMLLoader.load(getClass().getResource("main6.fxml"));

			Scene scene = new Scene(root, 400, 400);

			Button btn = (Button) scene.lookup("#btn");
			lbl1 = (Label) scene.lookup("#lbl1");
			lbl2 = (Label) scene.lookup("#lbl2");
			lbl3 = (Label) scene.lookup("#lbl3");
			lbl4 = (Label) scene.lookup("#lbl4");
			lbl5 = (Label) scene.lookup("#lbl5");
			lbl6 = (Label) scene.lookup("#lbl6");

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
		List<Label> lbl = new ArrayList<Label>();
		lbl.add(lbl1);
		lbl.add(lbl2);
		lbl.add(lbl3);
		lbl.add(lbl4);
		lbl.add(lbl5);
		lbl.add(lbl6);
		for (int i = 0; i < lbl.size(); i++) {
			lbl.get(i).setText("");
		}

		ArrayList<Integer> lotto = new ArrayList<Integer>();
		for (int i = 0; i < 6; i++) {
			lotto.add(ranNum());
			for (int j = 0; j < 6; j++) {
				lotto.add(ranNum());
				if (lotto.get(i).equals(lotto.get(j))) {
					lotto.set(j, ranNum());
				}
			}
		}
		for (int i = 0; i < lbl.size(); i++) {
			lbl.get(i).setText(lotto.get(i)+"");
		}
	}

	public int ranNum() {
		Random ran = new Random();
		int ranNum = ran.nextInt(45) + 1;
		return ranNum;
	}

	public static void main(String[] args) {
		launch(args);
	}
}
