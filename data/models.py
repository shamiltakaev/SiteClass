import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import datetime
from werkzeug.security import check_password_hash, generate_password_hash


class User(SqlAlchemyBase):
    __tablename__ = "users"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(
        sqlalchemy.String, index=True, unique=True, nullable=True)
    modified_date = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.datetime.now)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    jobs = orm.relationship("Jobs", back_populates="user")

    def set_data(self, surname: str, name: str, age: int, position: str,
                 speciality: str, address: str, email: str,
                 password: str = "", modified_date: datetime.datetime = datetime.datetime.now()):
        self.surname = surname
        self.name = name
        self.age = age
        self.position = position
        self.speciality = speciality
        self.address = address
        self.email = email
        self.modified_date = modified_date
        self.set_password(password)

    def set_password(self, password: str):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
    
    def __repr__(self):
        return f"{self.id} - {self.name}"


class Jobs(SqlAlchemyBase):
    __tablename__ = "jobs"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.datetime.now)
    end_date = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    team_leader = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship("User")

    def set_data(self, team_leader: int, job: str, work_size: int, collaborators: str, is_finished: bool = None,
                 start_date: datetime.datetime = None,
                 end_date: datetime.datetime = None):
        self.team_leader = team_leader
        self.job = job
        self.work_size = work_size
        self.collaborators = collaborators
        if is_finished is not None:
            self.is_finished = is_finished
        if start_date:
            self.start_date = start_date
        if end_date:
            self.end_date = end_date

    def __repr__(self):
        return f"{self.id} - {self.job}"


class Department(SqlAlchemyBase):
    __tablename__ = "departments"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chief = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    members = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)

    user = orm.relationship('User')

    def __repr__(self):
        return f'<Department> {self.id} {self.title} {self.email}'