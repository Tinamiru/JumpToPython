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
	<h4>삭제페이지입니다</h4>
	<form method="post" action=".\emp_del_act">
		<table border="1px">
			<tr>
				<td>사번</td>
			</tr>
			<tr>
				<td><input type="text" name="id"></td>
			</tr>
		</table>
		<input type="submit" value="삭제">
		<button type="button" onclick="location.href='./emp_list'">뒤로</button>
	</form>


</body>
</html>