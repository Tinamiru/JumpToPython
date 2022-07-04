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

@WebServlet("/emp_mod")
public class EmpMod extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		DaoEmp de = new DaoEmp();
		String eId = (String) request.getParameter("e_id");
		EmpVO vo = new EmpVO(eId);

		try {
			EmpVO list = de.getOne(vo);

			request.setAttribute("list", list);
			
			RequestDispatcher rd = request.getRequestDispatcher("/empMod.jsp");
			rd.forward(request, response);
			
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
