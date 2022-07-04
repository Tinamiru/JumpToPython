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
	<h4>수정페이지입니다</h4>
	<%
	EmpVO list = (EmpVO) request.getAttribute("list");
	%>
	<form method="post" action=".\emp_mod_act">
		<table border="1px">
			<tr>
				<td>사번</td>
				<td>이름</td>
				<td>성별</td>
				<td>주소</td>
			</tr>
			<tr>
				<td><input type="text" name="id" value="<%=list.getE_id()%>"
					readonly></td>
				<td><input type="text" name="name"
					value="<%=list.getE_name()%>"></td>
				<td><input type="text" name="sex" value="<%=list.getSex()%>"></td>
				<td><input type="text" name="addr" value="<%=list.getAddr()%>"></td>
			</tr>
		</table>
		<input type="submit" value="수정">
		<button type="button" onclick="location.href='./emp_list'">뒤로</button>
	</form>


</body>
</html>