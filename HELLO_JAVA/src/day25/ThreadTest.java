package day25;

public class ThreadTest {
	public static void showNumber() {
		for (int i = 1; i <= 100000; i++) {
			System.out.print(i+" ");
			if (i % 100 == 0) {
				System.out.println();
			}
		}
	}

	public static void showAscii() {
		for (int i = 1; i <= 100000; i++) {
			System.out.print((char) i);
			if (i % 100 == 0) {
				System.out.println();
			}
		}
	}

	public static void main(String[] args) {
		showNumber();
		showAscii();
	}
}
