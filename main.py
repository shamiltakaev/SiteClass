from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager
from data import db_session
from data.models import Jobs, User
app = Flask(__name__)
loginManager = LoginManager(app)

@loginManager.user_loader
def user_loader():
    pass

@app.route("/")
def index():
    session = db_session.create_session()
    data = session.query(Jobs, User).where(Jobs.team_leader == User.id).all()
    # jobs = session.query(Jobs).all()
    # users = session.query(User).all()
    # names = {name.id: tuple([name.surname, name.name]) for name in users}
    return render_template("index.html", data=data)

db_session.global_init("db/mars.db")

session = db_session.create_session()

# region Data

# user = User()
# user.set_data("Scott", "Ridley", 21, "captain", "research_engineer",
#               "module_1", "scott_chief@mars.org", password="cap")
# session.add(user)

# user = User()
# user.set_data("Weir", "Andy", 18, "chief scientist", "geologist",
#               "module_1", "andy_chief@mars.org", password="sci")
# session.add(user)

# user = User()
# user.set_data("Watny", "Mark", 25, "middle scientist", "biologist",

#               "module_2", "mak@mark.org", password="bio")
# session.add(user)

# user = User()
# user.set_data("Kapoor", "Venkat", 15, "pilot", "pilot, navigator",
#               "module_2", "kapoor@mars.org", password="pilot")
# session.add(user)

# user = User()
# user.set_data("Sanders", "Teddy", 27, "programmer", "IT specialist", 
#               "module_2", "sanders@mars.org", password="comp")
# session.add(user)

# user = User()
# user.set_data("Bean", "Sean", 17, "chief engineer", "builder", 
#               "module_1", "bean@mars.org", password="build")
# session.add(user)
# # session.commit()

# job = Jobs()
# job.set_data(1, 'deployment of residential modules 1 and 2', 15, '2, 3', False)
# session.add(job)

# job = Jobs()
# job.set_data(2, 'exploration of mineral resources', 15, '4, 3, 6', True)
# session.add(job)

# job = Jobs()
# job.set_data(3, 'development of a management system', 25, '5', False)
# session.add(job)

# job = Jobs()
# job.set_data(4, 'analysis of atmospheric air samples', 15, '4, 5', False)
# session.add(job)

# job = Jobs()
# job.set_data(5, 'Mars Rover maintenance', 5, '4', True)
# session.add(job)

# job = Jobs()
# job.set_data(7, 'preventive vaccinations of the crew', 7, '3', False)
# session.add(job)

# session.commit()
# endregion

app.run(host="127.0.0.1", port=5000, debug=True)
