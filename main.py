from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager
from data import db_session
from data.models import Jobs, User, Department
from forms.register import RegisterForm
from sqlalchemy import func
app = Flask(__name__)
app.config["SECRET_KEY"] = "yandex_lyceum"
loginManager = LoginManager(app)

@loginManager.user_loader
def user_loader():
    pass

@app.route("/")
def index():
    session = db_session.create_session()
    data = session.query(Jobs, User).where(Jobs.team_leader == User.id).all()
    return render_template("index.html", data=data)

@app.route("/register")
def register():
    form: RegisterForm = RegisterForm()
    if form.validate_on_submit():
        pass
    return render_template("register.html", form=form, title="Регистрация")

db_session.global_init("db/mars.db")

session = db_session.create_session()

# region Data

# user = Usre()
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
# departments = session.query(Department).all()
# for d in departments:
#     session.delete(d)

# session.commit()
# department = Department()
# department.title = "Department of transportation"
# department.chief = 4
# department.email = "transport@mars.org"
# department.members = "3, 1"
# session.add(department)

# department = Department()
# department.title = "Department of construction"
# department.chief = 6
# department.email = "build@mars.org"
# department.members = "1, 4, 2"
# session.add(department)

# department = Department()
# department.title = "Department of of construction"
# department.chief = 6
# department.email = "build2@mars.org"
# department.members = "3, 2, 5"
# session.add(department)

# department = Department()
# department.title = "Department of biological research"
# department.chief = 3
# department.email = "bio@mars.org"
# department.members = "4, 1, 3"
# session.add(department)

# department = Department()
# department.title = "Department of geological exploration"
# department.chief = 2
# department.email = "geo@mars.org"
# department.members = "4"
# session.add(department)
# session.commit()
# endregion
data = session.query(Department).join(User).filter(User.id.in_(func.aggregate_strings(Department.members, ", ")))
for dep in data:
    print(dep.title, dep.members)

# app.run(host="127.0.0.1", port=5000, debug=True)
