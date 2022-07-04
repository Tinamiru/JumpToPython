package kr.co.aiai.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

public class DaoEmp {

	public static void main(String[] args) throws ClassNotFoundException {

		DaoEmp de = new DaoEmp();

//		de.insert(new EmpVO("3", "3", "3", "3"));
//		de.update(new EmpVO("3", "2", "2", "2"));
//		de.delete(new EmpVO("2"));
		EmpVO vo = de.getOne(new EmpVO("2"));
		System.out.println("vo = " + vo);

//		ArrayList<EmpVO> list = de.getlist();
//
//		for (int i = 0; i < list.size(); i++) {
//			EmpVO imsi = list.get(i);
//			System.out.println("id = \t" + imsi.getE_id());
//			System.out.println("name = \t" + imsi.getE_name());
//			System.out.println("sex = \t" + imsi.getSex());
//			System.out.println("addr = \t" + imsi.getAddr());
//			System.out.println();
//		}

	}

	public EmpVO getOne(EmpVO vo) throws ClassNotFoundException {

		EmpVO rvo = new EmpVO();
		Class.forName("com.mysql.jdbc.Driver");
		Connection conn = null;
		Statement stmt = null;
		ResultSet rs = null;

		String url = "jdbc:mysql://127.0.0.1:3305/python";

		String sql = "select * from emp where e_id = " + vo.getE_id();
		EmpVO temp = new EmpVO();
		try {
			conn = DriverManager.getConnection(url, "root", "python");
			stmt = conn.createStatement();
			rs = stmt.executeQuery(sql);

			while (rs.next()) {

				String e_id = rs.getString(1);
				String e_name = rs.getString(2);
				String sex = rs.getString(3);
				String addr = rs.getString(4);

				rvo.setE_id(e_id);
				rvo.setE_name(e_name);
				rvo.setSex(sex);
				rvo.setAddr(addr);
			}

		} catch (SQLException e) {
			System.err.println("접속 실패");
		} finally {
			try {
				rs.close();
				stmt.close();
				conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}

		return rvo;
	}

	public ArrayList<EmpVO> getlist() throws ClassNotFoundException {

		ArrayList<EmpVO> list = new ArrayList<EmpVO>();

		Class.forName("com.mysql.jdbc.Driver");
		Connection conn = null;
		Statement stmt = null;
		ResultSet rs = null;

		String url = "jdbc:mysql://127.0.0.1:3305/python";

		String sql = "select * from emp";
		try {
			conn = DriverManager.getConnection(url, "root", "python");
			stmt = conn.createStatement();
			rs = stmt.executeQuery(sql);

			while (rs.next()) {

				String e_id = rs.getString(1);
				String e_name = rs.getString(2);
				String sex = rs.getString(3);
				String addr = rs.getString(4);

				EmpVO temp = new EmpVO();
				temp.setE_id(e_id);
				temp.setE_name(e_name);
				temp.setSex(sex);
				temp.setAddr(addr);
				list.add(temp);
			}

		} catch (SQLException e) {
			System.err.println("접속 실패");
		} finally {
			try {
				rs.close();
				stmt.close();
				conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		return list;
	}

	public int insert(EmpVO vo) throws ClassNotFoundException {
		Connection conn = null;
		Statement stmt = null;

		String url = "jdbc:mysql://127.0.0.1:3305/python";
		Class.forName("com.mysql.jdbc.Driver");
		int cnt = 0;
		try {
			String sql = "insert into emp" + "(e_id,e_name,sex,addr)" + "value" + "(" + vo.getE_name() + ","
					+ vo.getE_id() + "," + vo.getSex() + "," + vo.getAddr() + ")";
			conn = DriverManager.getConnection(url, "root", "python");
			stmt = conn.prepareStatement(sql);
			cnt = stmt.executeUpdate(sql);

			if (cnt > 0) {
				System.out.println("SQL 실행 성공.");
			} else {
				System.err.println("SQL 실행 실패.");
			}

		} catch (SQLException e) {
			System.err.println("insert 접속 실패");
			e.printStackTrace();
		} finally {
			try {
				stmt.close();
				conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		return cnt;
	}

	public int update(EmpVO vo) throws ClassNotFoundException {
		Connection conn = null;
		Statement stmt = null;
		Class.forName("com.mysql.jdbc.Driver");

		System.out.println("접속 성공");
		String url = "jdbc:mysql://127.0.0.1:3305/python";
		int cnt = 0;
		try {
			conn = DriverManager.getConnection(url, "root", "python");
			stmt = conn.createStatement();

			String sql = "UPDATE emp set e_name = " + vo.getE_name() + ", sex = " + vo.getSex() + ", addr = "
					+ vo.getAddr() + " where e_id = " + vo.getE_id();
			cnt = stmt.executeUpdate(sql);

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

		return cnt;
	}

	public int delete(EmpVO vo) throws ClassNotFoundException {

		Connection conn = null;
		Statement stmt = null;

		int cnt = 0;

		try {
			Class.forName("com.mysql.jdbc.Driver");
			String url = "jdbc:mysql://127.0.0.1:3305/python";
			conn = DriverManager.getConnection(url, "root", "python");
			stmt = conn.createStatement();

			System.out.println("접속 성공");

			String sql = "DELETE from emp where e_id = " + vo.getE_id();
			cnt = stmt.executeUpdate(sql);

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
		return cnt;
	}

}
