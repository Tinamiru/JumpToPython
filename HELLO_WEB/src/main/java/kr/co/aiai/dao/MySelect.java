package kr.co.aiai.dao;

import java.sql.*;

public class MySelect {
	
	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		Connection conn = null;
		Statement stmt = null;
		ResultSet rs = null;


		String url = "jdbc:mysql://127.0.0.1:3305/python";

		String sql = "select * from emp";
		try {
			System.out.println("접속 성공");
			
			conn = DriverManager.getConnection(url, "root", "python");
			stmt = conn.createStatement();
			rs = stmt.executeQuery(sql);
			
			while (rs.next()) {
                // 주의 - DB 레코드들의 칼럼은 0이 아닌 1부터 시작한다.
                // resultSet.next()는 boolean을 리턴함 - 다음 레코드가 존재하면 true 리턴

                int e_id = rs.getInt(1);
                String e_name = rs.getString(2);
                String sex = rs.getString(3);
                String addr = rs.getString(4);

                System.out.println(String.format("id = %d, name = %s, sex = %s, addr = %s",e_id,e_name,sex,addr));
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
