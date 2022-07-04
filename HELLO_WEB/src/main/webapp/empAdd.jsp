


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
	<h4>사원 추가페이지</h4>
	<form method="post" action=".\emp_add_act">
		<table border="1px">
			<tr>
				<td>사번</td>
				<td>이름</td>
				<td>성별</td>
				<td>주소</td>
			</tr>
			<tr>
				<td><input type="text" name="id"></td>
				<td><input type="text" name="name"></td>
				<td><input type="text" name="sex"></td>
				<td><input type="text" name="addr"></td>
			</tr>
		</table>
		<input type="submit" value="생성">
	</form>


</body>
</html>