from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///users.db")

# Quiz made with help from YouTube (Reference: Laeeq Khan - https://www.youtube.com/watch?v=PXnS8ftfCr8&t=744s)
class Question:
    q_id = -1
    question = ""
    option1 = ""
    option2 = ""
    option3 = ""
    correctOption = -1

    def __init__(self, q_id, question, option1, option2, option3, correctOption):
        self.q_id = q_id
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.correctOption = correctOption

    def get_correct_option(self):
        if self.correctOption == 1:
            return self.option1
        elif self.correctOption == 2:
            return self.option2
        else:
            return self.option3

# Quiz Questions
q1 = Question(1, "Q1. What does DNA stand for?", "Deoxyribonucleid Acid", "Deoxyribonucleid Alleles", "Dehydrogenated Acid", 1)
q2 = Question(2, "Q2. What was Charles Darwin known for?", "The theory of natural selection", "The law of specific nerves energies", "Recapitulation Theory", 1)
q3 = Question(3, "Q3. What is the correct equation for photosynthesis?", "6O2 + C6H12O6 → 6CO2 + 6H2O ", "C6H6O12 + 6H2O → 6O2 + 6CO2", "6CO2 + 6H2O → C6H12O6 + 6O2", 3)
q4 = Question(4, "Q4. What element accounts for more than 60 percent of the human body?", "Oxygen", "Carbon", "Nitrogen", 1)
q5 = Question(5, "Q5. Enzymes are mostly made of ...?", "Sugars", "Proteins", "Fats", 2)
q6 = Question(6, "Q6. What organic compound provides energy in living cells?", "TPA", "DNA", "ATP", 3)
q7 = Question(7, "Q7. Which four letters in DNA are used to denote the genetic code?", "ATHP", "ACGH", "ATCG", 3)
q8 = Question(8, "Q8. Which organ is responsible for filtering blood and releasing waste?", "Kidneys", "Pancreas", "Gallbladder", 1)
q9 = Question(9, "Q9. Which of the following terms refers to an animal that eat both animals and plants?", "herbivore", "Omnivore", "Carnivore", 2)
q10 = Question(10, "Q10. What is Mycology?", "The study of Bacteria", "The study of Macroevolution", "The study of Fungi", 3)
q11 = Question(11, "Q11. Which of the following terms refers to a DNA change that can lead to new characteristics?", "Defection", "Mutation", "Completion", 2)
q12 = Question(12, "Q12. Antonie van Leeuwenhoek was the first scientist to observe...?", "Viruses", "Bacteria", "Cells", 2)
q13 = Question(13, "Q13. RNA is made from DNA by a process called ...?", "Translation", "Transcription", "Synthesis", 2)
q14 = Question(14, "Q14. Why is a gene?", "A segment of DNA that codes for a protein", "A part of a cell in which you can find the DNA", "A set of two chromosomes", 1)
q15 = Question(15, "Q15. What is the male sex hormone?", "Progesterone", "Testosterone", "Estrogen", 2)
q16 = Question(16, "Q16. Male mosquitoes take their food from?", "Human Blood", "Animal Blood", "Sap of plants", 3)
q17 = Question(17, "Q17. Which branch of Zoology deals with the scientific study of animal behavior?", "Ecology", "Physiology", "Ethology", 3)
q18 = Question(18, "Q18. With iodine you can test for?", "Carbohydrates", "Proteins", "Fats", 1)
q19 = Question(19, "Q19. You can find DNA in the nucleus and in the ... of cells?", "Ribosomes", "Mitochondria", "Golgi bodies", 2)
q20 = Question(20, "Q20. How do viruses reproduce?", "They divide by mitosis", "They insert DNA in the host cell", "Sexually, by external fertilization", 2)
q21 = Question(21, "Q21. What structure is responsible for moving the chromosomes during mitosis?", "The spindle", "The membrane", "The mitochondria", 1)
q22 = Question(22, "Q22. Evolution occurs through the procces of?", "Asexual reproduction", "External Fertilization", "Natural Selection", 3)
q23 = Question(23, "Q23. Diseases that are carried by animals are reffered to as?", "Pathogens", "Animal Bound", "Zoonotic", 3)
q24 = Question(24, "Q24. A human have ... autosomes and .. sex chromosomes?", "22 pairs, 1 pair", "20 pairs, 2 pairs", "10 pairs, 2 pairs", 1)
q25 = Question(25, "Q25. If a person receives an X and a Y chromose, that person is?", "Female", "Blonde", "Male", 3)

questions_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25]

# Apology Function (reference: cs50x pset9, finance https://cs50.harvard.edu/x/2022/psets/9/finance/)
def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions_list = questions_list)

@app.route("/answers")
def answers():
    return render_template("answers.html", questions_list = questions_list)

@app.route("/scores", methods=['POST', 'GET'])
def submit():
    user_id = session["user_id"]

    # User reached route via POST
    if request.method == "POST":

        # Counter for amount of correct answers
        correct_count = 0

        # Count amount of correct answers
        for question in questions_list:
            q_id = str(question.q_id)
            selected_option = request.form[q_id]
            correct_option = question.get_correct_option()
            if selected_option == correct_option:
                correct_count = correct_count + 1

        # Insert the amount of correct answers in the results database
        results_db = db.execute("INSERT INTO results (user_id, result) VALUES (?, ?)", user_id, correct_count)
        resultsdb = db.execute("SELECT result FROM results WHERE user_id = ?", user_id)
        result = resultsdb[-1]["result"]

        # Select amount of correct options from result database
        score_counter = db.execute("SELECT COUNT(result) FROM results WHERE user_id = ?", user_id)
        score_counter = score_counter[0]["COUNT(result)"]

        # Select the top three high scores from the user in the results database
        high_scores = db.execute("SELECT result FROM results where user_id = ? ORDER BY result DESC LIMIT 3", user_id)

        # If the quiz is done only once, show only one high score
        if score_counter == 1:
            high1 = high_scores[0]["result"]
            return render_template("scores.html", result = result, results_db=results_db, score_counter=score_counter, high1 = high1)

        # If the quiz is done twice show only two high scores
        elif score_counter == 2:
            high1 = high_scores[0]["result"]
            high2 = high_scores[1]["result"]
            return render_template("scores.html", result = result, results_db=results_db, score_counter=score_counter, high1 = high1, high2 = high2)

        # If the quiz is done three times or more show the highest three scores
        elif score_counter >= 3:
            high1 = high_scores[0]["result"]
            high2 = high_scores[1]["result"]
            high3 = high_scores[2]["result"]
            return render_template("scores.html", result = result, results_db=results_db, score_counter=score_counter, high1 = high1, high2 = high2, high3 = high3)

    #User reached route via GET
    else:
        high_scores = db.execute("SELECT result FROM results where user_id = ? ORDER BY result DESC LIMIT 3", user_id)
        score_counter = db.execute("SELECT COUNT(result) FROM results WHERE user_id = ?", user_id)
        score_counter = score_counter[0]["COUNT(result)"]
        resultsdb = db.execute("SELECT result FROM results WHERE user_id = ?", user_id)

        if score_counter >= 3:
            high1 = high_scores[0]["result"]
            high2 = high_scores[1]["result"]
            high3 = high_scores[2]["result"]
            result = resultsdb[-1]["result"]
            return render_template("scores.html", score_counter=score_counter, high1 = high1, high2 = high2, high3 = high3, result = result)
        elif score_counter == 2:
            high1 = high_scores[0]["result"]
            high2 = high_scores[1]["result"]
            result = resultsdb[-1]["result"]
            return render_template("scores.html", score_counter=score_counter, high1 = high1, high2 = high2, result = result)
        elif score_counter == 1:
            high1 = high_scores[0]["result"]
            result = resultsdb[-1]["result"]
            return render_template("scores.html", score_counter=score_counter, high1 = high1, result = result)

    return render_template("scores.html", score_counter=score_counter)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM userssite WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page 2
        return redirect("/")

    # User reached route via GET 
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "GET":
        return render_template("register.html")

    else:
                # Ensure username was submitted
        username = request.form.get("username")
        if not username:
            return apology("must provide username", 400)

        # Ensure password was submitted
        password = request.form.get("password")
        if not password:
            return apology("must provide password", 400)

        # Ensure confirmation was submitted
        confirmation = request.form.get("confirmation")
        if not confirmation:
            return apology("must provide confirmation", 400)

        # Check if password and confirmation match
        if password != confirmation:
            return apology("Passwords don't match", 400)

        # Hash password
        hash = generate_password_hash(password)

        # Check if username doesn't already exist
        try:
            new = db.execute("INSERT INTO userssite (username, hash) VALUES (?, ?)", username, hash)
        except:
            return apology("Username already exist")

        session["user_id"] = new

        return redirect("/")
