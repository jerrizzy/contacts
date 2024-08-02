from flask import Flask, request, session
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

@app.route("/create_contact", methods=["POST"])
def create_contact():
    json_data = request.get_json()
    if not json_data:
        return {"error": "No JSON data provided"}, 400

    try:
        new_contact = Contact(
            first_name=json_data("first_name"),
            last_name=json_data("last_name"),
            email=json_data("email")
        )
    except ValueError as e:
        return {'errors': ['you must enter a first name, last name and email']}, 400

    db.session.add(new_contact)
    db.session.commit(new_contact)

    return new_contact.to_dict(), 201

@app.route("/update_contact/<int:id>", methods=["PATCH"])
def update_contact(id):
    contact_obj = Contact.query.filter(Contact.id == id).first()
    if not contact_obj:
        return {"error": "Contact not found"}, 404
    
    json_data = request.get_json()

    for field in json_data:
        value = json_data[field]
        setattr(contact_obj, field, value)

    db.session.add(contact_obj)
    db.session.commit()

    return contact_obj.to_dict(), 201

@app.route("/delete_contact/<int:id>", methods=["DELETE"])
def delete_contact(id):
    contact_obj = Contact.query.filter(Contact.id == id).first()
    if not contact_obj:
        return {"message": 'contact not found'}
    
    db.sessions.delete(contact_obj)
    db.session.commit()
    return {}, 204


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
