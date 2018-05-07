import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Ensure environment variable is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # obtain cash for user
    cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
    total_cash = int(cash[0]["cash"])

    # select stock and amount for user
    portfolio_stocks = db.execute(
        "SELECT symbol, name, price, number, value FROM shareportfolio WHERE id = :id", id=session["user_id"])

    # variable for total value
    total_value = 0
    length = len(portfolio_stocks)

    for portfolio_stock in portfolio_stocks:
        for i in range(0, length):
            stock = portfolio_stocks[i]["symbol"]
            number = portfolio_stocks[i]["number"]
            stock_value = portfolio_stocks[i]["number"] * portfolio_stocks[i]["price"]
            total_value = stock_value + total_cash
            db.execute("UPDATE shareportfolio SET value = :value WHERE id = :id AND symbol = :stock",
                       id=session["user_id"], stock=stock, value=stock_value)

    return render_template("index.html", stocks=portfolio_stocks, cash=usd(total_cash), total=usd(total_value))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":

        # check that symbol and number of shares are provided
        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("must provide symbol and number of shares")
        if request.form.get("shares").isdigit() == False:
            return apology("must provide whole numebr")
        # ensure proper symbol
        quote = lookup(request.form.get("symbol"))
        if not quote:
            return apology("Invalid Symbol")

        # assign variables for shares and price
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        price = round(float(quote["price"]), 2)
        cost = round(float(price * shares), 2)
        stock_value = shares * price

        # ensure proper number of shares
        if shares < 0:
            return apology("Shares must be positive integer")

        # get user cash balance
        balance = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])

        # check if enough money to buy shares
        if not balance or float(balance[0]["cash"]) < cost:
            return apology("Insufficient funds")

        # update history table with the buy
        else:
            db.execute("UPDATE users SET cash = cash - :cost WHERE id = :id", cost=cost, id=session["user_id"])
            db.execute("INSERT INTO history (shares, symbol, price, userid) VALUES(:shares, :symbol, :price, :userid)",
                       shares=shares, symbol=symbol, price=price, userid=session["user_id"])

        # populate the portfolio table with new stock holding or add to position
        has_stock = db.execute("SELECT symbol FROM shareportfolio WHERE symbol = :symbol AND id = :id",
                               symbol=symbol, id=session["user_id"])

        if not has_stock:
            db.execute("INSERT INTO shareportfolio (id,symbol,price,number,value) VALUES (:id,:symbol,:price,:number,:value)",
                       id=session["user_id"], symbol=symbol, price=price, number=shares, value=cost)
        else:
            db.execute("UPDATE shareportfolio SET number = number + :number WHERE id = :id AND symbol = :symbol",
                       id=session["user_id"], symbol=symbol, number=shares)
            db.execute("UPDATE shareportfolio SET price = :price WHERE id = :id AND symbol = :symbol",
                       id=session["user_id"], symbol=symbol, price=price)
            db.execute("UPDATE shareportfolio SET value = value + :value WHERE id = :id AND symbol = :symbol",
                       id=session["user_id"], symbol=symbol, value=stock_value)

        # return to history so user can see transactions
        return redirect("/")

    elif request.method == "GET":
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # get history details from history table
    history = db.execute("SELECT shares, symbol, price, datetime FROM history WHERE userid = :id", id=session["user_id"])

    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    if request.method == "POST":

        # Ensure username submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")

    # if user reached via POST check for valid symbol
    elif request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide symbol")

        # use lookup function to get current stock info
        quote = lookup(request.form.get("symbol"))

        # check stock exists
        if quote == None:
            return apology("invalid symbol")

        # display info given by quote list
        else:
            return render_template("quoted.html", name=quote['name'], symbol=quote['symbol'], price=quote['price'])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    if request.method == "POST":

        # Check username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Check password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Check password confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide password confirmation", 400)

        # Check passwords are matching
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Sorry, passwords didn't match.")

        # Hash password and store password
        hashed_password = generate_password_hash(request.form.get("password"))

        # Add user to database
        result = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)",
                            username=request.form.get("username"), hash=hashed_password)

        if not result:
            return apology("The username is already taken")

        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        sell_symbol = db.execute("SELECT symbol FROM shareportfolio WHERE id = :id", id=session["user_id"])
        return render_template("sell.html", symbol=sell_symbol)

    else:
        # check that symbol and number of shares are provided
        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("must provide symbol and number of shares")
        if request.form.get("shares").isdigit() == False:
            return apology("must provide whole number")
        # ensure proper symbol
        quote = lookup(request.form.get("symbol"))
        if not quote:
            return apology("Invalid Symbol")

        # assign variables for shares and price
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        price = round(float(quote["price"]), 2)
        cost = round(float(price * shares), 2)
        stock_value = price * shares

        # ensure proper number of shares
        if shares < 0:
            return apology("Shares must be positive integer")

        # get user cash balance
        shareholding = db.execute("SELECT number FROM shareportfolio WHERE id = :id AND symbol = :symbol",
                                  id=session["user_id"], symbol=symbol)

        # check if enough money to buy shares
        if not shareholding or shareholding[0]["number"] < shares:
            return apology("Insufficient shares")

        else:
            db.execute("UPDATE shareportfolio SET number = number - :number WHERE id = :id AND symbol = :symbol",
                       id=session["user_id"], symbol=symbol, number=shares)
            db.execute("UPDATE shareportfolio SET price = :price WHERE id = :id AND symbol = :symbol",
                       id=session["user_id"], symbol=symbol, price=price)
            db.execute("UPDATE shareportfolio SET value = value - :value WHERE id = :id AND symbol = :symbol",
                       id=session["user_id"], symbol=symbol, value=stock_value)
            # return to index
            return redirect("/")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
