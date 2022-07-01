package kr.co.aiai.dao;

import java.sql.*;

public class MyDelete {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		Connection conn = null;
		Statement stmt = null;

		try {
			String url = "jdbc:mysql://127.0.0.1:3305/python";
			conn = DriverManager.getConnection(url, "root", "python");
			stmt = conn.createStatement();

			System.out.println("접속 성공");

			String sql = "DELETE from emp where e_id = 1";
			int cnt = stmt.executeUpdate(sql);

			if (cnt > 0) {
				System.out.println("SQL 실행 성공.");
			} else {
				System.err.println("SQL 실행 실패.");
			}

		} catch (SQLException e) {
			System.err.println("접속 실패");
			e.printStackTrace();
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
