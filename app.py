from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("dictionary.csv")


@app.route("/")
def home():
    return render_template("word.html")


@app.route("/api/v1/<word>/")
def api(word):
    definition = df.loc[df["word"] == word]["definition"].squeeze()

    result_dict = {"Word": word, "Definition": definition}
    return result_dict


if __name__ == "__main__":
    # port= is optional - only if running multiple apps
    app.run(debug=True)
