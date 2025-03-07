from flask import Flask, render_template, redirect, url_for, request
from ioform import IOForm
from converter import ConversionHelper
from utils import get_placeholder_text

app = Flask(__name__)
app.config["SECRET_KEY"] = "ore no taisetsu na kagi desu"

@app.route("/update-format<string:format>")
def update_format(format):
	return redirect(url_for("home", conversion_format=format))

@app.route("/", methods=["GET", "POST"])
def home():
	conversion_format = request.args.get("conversion_format", "Convert to")
	
	placeholder_texts = get_placeholder_text(conversion_format)
	
	form = IOForm()
	if form.validate_on_submit():
		converted_text = ConversionHelper.convert_text(form.input_text.data, conversion_format)
		form.output_text.data = converted_text
		form.input_text.data = ""
	
	return render_template("app.html", form=form, btn_text=conversion_format, placeholder_texts=placeholder_texts)

if __name__ == "__main__":
	app.run(debug=True)