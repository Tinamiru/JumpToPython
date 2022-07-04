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
	<h4>세부 페이지</h4>
	<%
	EmpVO list = (EmpVO) request.getAttribute("list");
	%>
	<table border="1px">
		<tr>
			<td>사번</td>
			<td>이름</td>
			<td>성별</td>
			<td>주소</td>
		</tr>
		<tr>
			<td><%=list.getE_id()%></td>
			<td><%=list.getE_name()%></td>
			<td><%=list.getSex()%></td>
			<td><%=list.getAddr()%></td>
		</tr>
	</table>
	<button type="button" onclick="location.href='./emp_list'">뒤로</button>
	<button type="button"
		onclick="location.href='./emp_mod?e_id=<%=list.getE_id()%>'">수정</button>
	<button type="button" onclick="location.href='./emp_del'">삭제</button>
</body>
</html>