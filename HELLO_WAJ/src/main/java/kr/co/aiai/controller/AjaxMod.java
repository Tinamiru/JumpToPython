package kr.co.aiai.controller;

import java.io.IOException;
import java.util.HashMap;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.dao.DaoEmp;
import kr.co.aiai.dao.EmpVO;
import kr.co.aiai.util.AjaxUtil;

@WebServlet("/ajaxmod")
public class AjaxMod extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		String e_id = request.getParameter("e_id");
		String e_name = request.getParameter("e_name");
		String sex = request.getParameter("sex");
		String addr = request.getParameter("addr");
		EmpVO pvo = new EmpVO(e_id, e_name, sex, addr);

		DaoEmp de = new DaoEmp();
		try {
			int cnt = de.update(pvo);
			HashMap<String, String> hm = new HashMap<String, String>();
			hm.put("cnt", cnt + "");
			AjaxUtil.responseJson(response, hm);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doGet(request, response);
	}

}