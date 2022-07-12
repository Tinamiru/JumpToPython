<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="jquery-3.6.0.min.js"></script>
<script type="text/javascript">
function fn_list(){
	var param = "";
	param += "dummy=" + Math.random();
	param += "&a=777";
	$.ajax({
		url : "ajaxlist",
		data : param,
		dataType : "json",
		type : "post",
		async: false,
		success : function(res) {
			var list = res;
			
			var html = ``;
			
			for(var i=0;i<list.length;i++){
				var e_id = list[i].e_id;
				var e_name = list[i].e_name;
				var sex = list[i].sex;
				var addr = list[i].addr;
				html += `
				<tr>
					<td><a href="javascript:fn_one('`+e_id+`')">`+e_id+`</a></td>
					<td>`+e_name+`</td>
					<td>`+sex+`</td>
					<td>`+addr+`</td>
				</tr>
				`;
			}
			$("#mytbody").html(html);
		}
	});
}

function fn_one(e_id){
	var param = "";
	param += "dummy=" + Math.random();
	param += "&e_id="+e_id;
	$.ajax({
		url : "ajaxone",
		data : param,
		dataType : "json",
		type : "post",
		async: false,
		success : function(res) {
			var emp = res;
			$("#e_id").val(emp.e_id);
			$("#e_name").val(emp.e_name);
			$("#sex").val(emp.sex);
			$("#addr").val(emp.addr);
		}
	});
}

function fn_add(){
	var param = "";
	param += "dummy=" + Math.random();
	param += "&e_name="+$("#e_name").val();
	param += "&sex="+$("#sex").val();
	param += "&addr="+$("#addr").val();
	
	$.ajax({
		url : "ajaxadd",
		data : param,
		dataType : "json",
		type : "post",
		async: false,
		success : function(res) {
			var cnt = res.cnt;
			if(cnt ==1){
				alert("정상적으로 추가하였습니다.");
				fn_list();
				$("#e_id").val("");
				$("#e_name").val("");
				$("#sex").val("");
				$("#addr").val("");
			}
		}
	});
}

</script>
</head>
<body onload="fn_list()">
<table border="1px">
	<thead>
		<tr>
			<td>사번</td>
			<td>이름</td>
			<td>성별</td>
			<td>주소</td>
		</tr>
	</thead>
	<tbody id="mytbody">
		<tr>
			<td>1</td>
			<td>1</td>
			<td>1</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

<table border="1px">
	<tr>
		<td>사번</td>
		<td>
			<input type="text" id="e_id" />
		</td>
	</tr>
	<tr>
		<td>이름</td>
		<td>
			<input type="text" id="e_name" />
		</td>
	</tr>
	<tr>
		<td>성별</td>
		<td>
			<input type="text" id="sex" />
		</td>
	</tr>
	<tr>
		<td>주소</td>
		<td>
			<input type="text" id="addr" />
		</td>
	</tr>
	<tr>
		<td colspan="2">
			<input type="button" value="추가" onclick="fn_add()" />
			<input type="button" value="수정" />
			<input type="button" value="삭제" />
		</td>
	</tr>
	
</table>




</body>
</html>