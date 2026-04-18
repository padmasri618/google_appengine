from flask import Flask, render_template_string, request, redirect, session
import random, os

app = Flask(__name__)
app.secret_key = "easy_key"

# Simple Login Page
LOGIN_HTML = """
<body style="text-align:center; padding:50px; font-family:sans-serif;">
    <h1>Cloud Login</h1>
    <form method="POST">
        <input type="text" name="u" placeholder="User" required><br><br>
        <input type="password" name="p" placeholder="Pass" required><br><br>
        <button type="submit">Login</button>
    </form>
    <p style="color:red">{{ err }}</p>
</body>
"""

# Simple Portal Page
PORTAL_HTML = """
<body style="text-align:center; padding:50px; font-family:sans-serif;">
    <h1>Cloud Portal</h1>
    <p><strong>Fact:</strong> {{ fact }}</p>
    <br>
    <a href="/portal">New Fact</a> | <a href="/logout">Logout</a>
</body>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['u'] == 'admin' and request.form['p'] == '123':
            session['user'] = 'admin'
            return redirect('/portal')
        return render_template_string(LOGIN_HTML, err="Try Again!")
    return render_template_string(LOGIN_HTML, err="")

@app.route('/portal')
def portal():
    if 'user' not in session: return redirect('/')
    facts = ["Cloud is scalable", "Cloud is cheap", "Cloud is fast"]
    return render_template_string(PORTAL_HTML, fact=random.choice(facts))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
