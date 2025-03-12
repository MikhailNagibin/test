from flask import *
from flask import flash
from flask_login import *
from forms import *
import datetime


app = Flask(__name__)
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(days=365)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["SECRET_KEY"] = "secret_key"



@app.route("/", methods=["GET", "POST"])
def all_days():
    if current_user.is_authenticated:
        return redirect("/inventory_see")
    form = AutorisationForm()
    return render_template(
        "auth_templates/login.html", title="Авторизация", form=form, message=""
    )




if __name__ == "__main__":
    # conn = get_db_connection()
    # cur = conn.cursor()
    app.run(host='0.0.0.0', port=8000, debug=True)
