<%@page import="kr.co.aiai.dao.EmpVO"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h4>삭제되었습니다.</h4>
	.
	<%
String pId = request.getParameter("id");

request.setAttribute("id", pId);
%>

	<br>
	<button type="button" onclick="location.href='./emp_list'">돌아가기</button>
</body>
</html>