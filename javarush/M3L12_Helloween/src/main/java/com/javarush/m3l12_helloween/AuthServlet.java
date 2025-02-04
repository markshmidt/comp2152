package com.javarush.m3l12_helloween;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Map;
import java.util.Set;

@WebServlet(name = "AuthServlet", value = "/authServlet")
public class AuthServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        System.out.println("LOG: doGet IN authServlet");

        String lgn = request.getParameter("login");
        String pwd = request.getParameter("password");

        PrintWriter writer = response.getWriter(); // (1) СОЗДАЛИ ОБЪЕКТ PrintWriter
        writer.println("<html><body>");
        writer.println("<h1>AUTHORISATION</h1>");
        writer.println("<br>");

        Map<String, String[]> parameterMap = request.getParameterMap();

        Set<String> strings = parameterMap.keySet();
        for (String string : strings) {
            writer.println(string);
        }
        writer.println("<br>");

        for (String[] value : parameterMap.values()) {
            for (String s : value) {
                writer.println(s);
            }
        }
        writer.println("</body></html>");
        
    }
}