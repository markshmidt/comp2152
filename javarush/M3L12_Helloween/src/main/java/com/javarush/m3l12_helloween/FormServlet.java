package com.javarush.m3l12_helloween;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet(name = "FormServlet", value = "/formServlet")
public class FormServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        System.out.println("LOG: doPost IN formServlet");

        response.setContentType("text/html");
        PrintWriter writer = response.getWriter();

        String name = request.getParameter("username");
        String age = request.getParameter("userage");
        String gender = request.getParameter("gender");
        String country = request.getParameter("country");
        String[] courses = request.getParameterValues("courses");

        try {
            writer.println("<p>Name: " + name + "</p>");
            writer.println("<p>Age: " + age + "</p>");
            writer.println("<p>Gender: " + gender + "</p>");
            writer.println("<p>Country: " + country + "</p>");
            writer.println("<h4>Courses</h4>");
            for(String course: courses)
                writer.println("<li>" + course + "</li>");
        } finally {
            writer.close();
        }
    }
}
