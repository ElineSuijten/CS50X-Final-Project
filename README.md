# The Biology Quiz
### Made by: Eline Suijten
### Video Demo: https://youtu.be/eP3H7dag5GQ
## Background Information:
This project was the final project for the course CS50x Introduction to Programming. With zero programming experiences I started this course. Therefore, the final project was my first programming project. I can not wait to learn more and see my improvements over time!

## Technologies used:
* Python (Flask)
* SQlite3
* HTML5
* CSS3
* Jinja2
* Bootstrap 5.1

# Description of the Project
My final project is a website where the user can test their biology knowledge with a quiz that consists of 25 questions. The users have to register and login in order to take te quiz. The user is able to see their own most recent score as well as their three highest scores. After they have completed the quiz for at least one time, they can view the quiz answers.

## Files
### app.py
This is the main file. This file disables caching of responses. It also configures Flask to store sessions on the local filesystem. The file also configures CS50's SQL module to use the database "users.db". The file consists the functions for the quiz and it includes the quiz questions. This was done with the help of a YouTube video from Laeew Khan (https://www.youtube.com/watch?v=PXnS8ftfCr8&t=744s), which showed how to implement an quiz webapp in Flask.

Furthermore, the file consists of the routes. Login stored the 'user_id' in 'session', so that it is "remembered" who is logged in. If the user has succesfully registerer or logged in, the user is redirected to the homepage (index.html) via "/". 'Logout' clears 'session'.

### users.db
This is the SQlite database with two tables: 'userssite', and 'results'. The table 'userssite' consists of the user_id, the username and the hashed password. The table 'results' stores the results of the quiz per user.

### styles.ccs
This css stylesheet is used to style and layout the quiz webapp.

### layout.html
This is the basic layout of the website. The other html pages are extensions of this page (with the use of Jinja2). The footer and navbar are stylezed with Bootstrap(5.1).

### index.html
This is the homepage. It consists of an introduction text and a button which will direct you to the login page if you are not already logged in or to the quiz page if you are already logged in.

### login.html
This html consists the login form.

### register.html
This html consists the register form.

### apology.html
If the users input at the register form is blank or the username already exist, an apology is showed. The apology is an error message with an image. This apology is also shown if the passwords at the register form do not match or when the login data is not recognized.

### answers.html
This html showes the correct quiz answers.

### scores.html
Here the most recent score for the user is shown as well as a table with the three highest scores of the current user. If the user hasn't completed the quiz at least one time, a message is shown that states that the user first has to complete the quiz before a score is shown. Also the amount of times the quiz is taken by the current user is shown.

### quiz.html
This file consist the information for the quiz page. It shows the quiz questions and the answer options are showed with radio buttons.

# What is CS50x?
Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web programming. Languages include C, Python, and SQL plus HTML, CSS, and JavaScript. Problem sets inspired by the arts, humanities, social sciences, and sciences. Course culminates in a final project. Designed for concentrators and non-concentrators alike, with or without prior programming experience. Two thirds of CS50 students have never taken CS before. Among the overarching goals of this course are to inspire students to explore unfamiliar waters, without fear of failure, create an intensive, shared experience, accessible to all students, and build community among students.
(https://cs50.harvard.edu/x/2023/)