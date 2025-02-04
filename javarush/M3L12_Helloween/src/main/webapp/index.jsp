<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <title>JSP - Hello World</title>
</head>
<body>
<h1><%= "Hello World!" %>
</h1>
<br/>
<a href="hello-servlet">Hello Servlet</a> <!-- адресТекущегоСервера/тоЧтоВhref  -->
<!-- request -> GET localhost:8080/hello-servlet  -->
<br>
<a href="https://www.javarush.com">JR</a>
<br>
<a href="authServlet">Authentication Servlet</a>
<br>
<a href="catalogServlet">Catalog Servlet</a>
<br>
<a href="redirectServlet">Redirect Servlet</a>
</body>
</html>