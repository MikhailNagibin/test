from flask import *
from flask import flash
from flask_login import *
from user import User
from forms import *
from our_requests import *
import datetime


app = Flask(__name__)
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(days=365)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["SECRET_KEY"] = "secret_key"
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/", methods=["GET", "POST"])
def autorisation(): # Для всех
    if current_user.is_authenticated:
        return redirect("/inventory_see")
    form = AutorisationForm()
    if form.validate_on_submit():
        us = get_user_by_email(cur, form.email.data.lower())
        if us and us[0][4] == generate_password(form.password.data):
            user = User(*us[0])
            login_user(user, remember=True)
            return redirect("/inventory_see")
        return render_template(
            "auth_templates/login.html",
            title="Авторизация",
            form=form,
            message="Неправильный логин или пароль",
        )
    return render_template(
        "auth_templates/login.html", title="Авторизация", form=form, message=""
    )




if __name__ == "__main__":
    conn = get_db_connection()
    cur = conn.cursor()
    app.run(host='0.0.0.0', port=8000, debug=True)
