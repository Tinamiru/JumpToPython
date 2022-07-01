package kr.co.aiai.dao;

import java.sql.*;

public class MyInsert {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		Connection conn = null;
		Statement stmt = null;

		String url = "jdbc:mysql://127.0.0.1:3305/python";

		String sql = "insert into emp" + "(e_id,e_name,sex,addr)" + "value" + "(3,3,3,3)";

		try {
			System.out.println("접속 성공");

			conn = DriverManager.getConnection(url, "root", "python");
			stmt = conn.createStatement();
			int cnt = stmt.executeUpdate(sql);

			if (cnt > 0) {
				System.out.println("SQL 실행 성공.");
			} else {
				System.err.println("SQL 실행 실패.");
			}

		} catch (SQLException e) {
			System.err.println("접속 실패");
		} finally {
			try {
				stmt.close();
				conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}
}
