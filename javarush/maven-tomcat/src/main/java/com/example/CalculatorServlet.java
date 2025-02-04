package com.example;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

public class CalculatorServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        // Get the session and retrieve the "sum" attribute
        HttpSession session = request.getSession();
        Integer sum = (Integer) session.getAttribute("sum");
        if (sum == null) {
            sum = 0; // Initialize sum if it's not in the session
        }

        // Get the "n" parameter from the request
        String n = request.getParameter("n");
        int value = (n != null) ? Integer.parseInt(n) : 0;
        sum += value;

        if (n != null) {
            try {
                sum += Integer.parseInt(n);
            } catch (NumberFormatException e) {
                response.getWriter().println("Invalid number format: " + n);
                return;
            }
        } else {
            response.getWriter().println("Parameter 'n' is missing.");
            return;
        }

        // Save the updated sum in the session
        session.setAttribute("sum", sum);

        // Write the response
        PrintWriter out = response.getWriter();
        out.println("<html>");
        out.println("<head><title>CalculatorServlet</title></head>");
        out.println("<body>");
        out.println("<h1>Sum = " + sum + "</h1>");
        out.println("</body>");
        out.println("</html>");
    }

}
