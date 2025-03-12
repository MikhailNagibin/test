from flask import *
from flask import flash
from forms import *
import datetime


app = Flask(__name__)
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(days=365)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["SECRET_KEY"] = "secret_key"



@app.route("/", methods=["GET", "POST"])
def all_days():
    form = AutorisationForm()
    data = ["23 января 2023 года", [(1, True), (1, False), (2, True), (1, False)]]
    return render_template(
        "all_days.html", title="Просмотр всех дней", form=form, message="", data=data)


if __name__ == "__main__":
    # conn = get_db_connection()
    # cur = conn.cursor()
    app.run(host='0.0.0.0', port=8000, debug=True)
