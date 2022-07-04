package kr.co.aiai.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.dao.DaoEmp;
import kr.co.aiai.dao.EmpVO;

@WebServlet("/emp_mod_act")
public class EmpModAct extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		request.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charset=UTF-8");

		DaoEmp de = new DaoEmp();
		String id = (String) request.getParameter("id");
		String name = (String) request.getParameter("name");
		String sex = (String) request.getParameter("sex");
		String addr = (String) request.getParameter("addr");

		EmpVO vo = new EmpVO(id, name, sex, addr);
		try {
			int cnt = de.update(vo);
			if (cnt > 0) {
				RequestDispatcher rd = request.getRequestDispatcher("/empModAct.jsp");
				rd.forward(request, response);
			} else {
				RequestDispatcher rd = request.getRequestDispatcher("/empErr.jsp");
				rd.forward(request, response);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
