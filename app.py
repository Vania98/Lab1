from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lab4_1dq9_user:u6CG9nUNTSMSRCZSKQPnKe6VwKv2hr6H@dpg-d0dkcqmuk2gs73d7e0rg-a.oregon-postgres.render.com/lab4_1dq9'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route('/add', methods=['POST'])
def add_user():
    data = request.get_json()
    print(data)
    new_user = User(name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added!'})

@app.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([{'id': u.id, 'name': u.name} for u in users])

if __name__ == '__main__':
    app.run(debug=True)
