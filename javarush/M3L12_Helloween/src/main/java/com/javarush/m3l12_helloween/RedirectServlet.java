package com.javarush.m3l12_helloween;

import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet(name = "redirectServlet", value = "/redirectServlet")
public class RedirectServlet extends HttpServlet {

        public void init() {
            System.out.println("LOG: INIT REDIRECT SERVLET");
        }
        public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {

            RequestDispatcher requestDispatcher = request.getRequestDispatcher("/catalogServlet");
            try {
                requestDispatcher.forward(request,response);
            } catch (ServletException e) {
                throw new RuntimeException(e);
            }

            // response.sendRedirect("https://bing.com");
//            response.sendRedirect("/catalogServlet");

        }

    }
