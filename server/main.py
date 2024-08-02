from flask import Flask, request
from flask_cors import CORS
from models import Contact, db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

db.init_app(app)
CORS(app, supports_credentials=True)

@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    return [contact.to_dict() for contact in contacts], 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
