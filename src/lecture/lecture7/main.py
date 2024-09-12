from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")

    return render_template("search.html", keyword=keyword, jobs=jobs)

if __name__ == "__main__":
    app.run("localhost")

# from extractors.indeed import extract_indeed_jobs
# from extractors.wwr import extract_wwr_jobs
# from file import save_to_file

# keyword = input("What do you want to search for?")

# indeed = extract_indeed_jobs(keyword)
# wwr = extract_wwr_jobs(keyword)
# jobs = indeed + wwr

# save_to_file(keyword, jobs)