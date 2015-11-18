from flask import Flask
from flask import request
app = Flask(__name__)

acronyms_to_expansions = {
    "WTF": "what the fuck",
    "CYA": "cover your ass",
    "OP": "original poster",
    "NIMBY": "not in my back yard",
    "FUD": "fear, uncertainty, and doubt"
}

@app.route("/", methods=["POST"])
def acronym_expand_handler():
    try:
        acronym = request.form['text'].strip()
        expansion = acronyms_to_expansions.get(acronym, None)

        if expansion:
	    return expansion
        else:
	    error_message = "Sorry, I couldn't find an expansion for %s." % acronym
	    return error_message

    except Exception, ex:
         return "An error occured processing your acronym. WTF!"

if __name__ == "__main__":
    app.run()

