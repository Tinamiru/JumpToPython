<%@page import="kr.co.aiai.dao.EmpVO"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link rel="stylesheet" href="index.css">
</head>
<body>
	<h4>사원목록</h4>
	<%
	ArrayList<EmpVO> list = (ArrayList<EmpVO>) request.getAttribute("list");
	%>
	<table border="1px">
		<tr>
			<td>사번</td>
			<td>이름</td>
			<td>성별</td>
			<td>주소</td>
		</tr>
		<%
		for (int i = 0; i < list.size(); i++) {
		%>
		<%
		EmpVO temp = (EmpVO) list.get(i);
		%>
		<tr>
			<td><a href="emp_detail?e_id=<%=temp.getE_id()%>"><%=temp.getE_id()%></a></td>
			<td><%=temp.getE_name()%></td>
			<td><%=temp.getSex()%></td>
			<td><%=temp.getAddr()%></td>
		</tr>
		<%
		}
		%>
	</table>
	<button type="button" onclick="location.href='./emp_add'">추가</button>
</body>
</html>