# from flask import render_template, redirect, Blueprint
# from flask_login import login_user, logout_user, login_required

# from forms.login import LoginForm
# from forms.register import RegisterForm


# from data import db_session
# from data.user import User


# user_bp = Blueprint(
#     'users',
#     __name__,
#     template_folder='templates'
# )


# @user_bp.route("/register", methods=["GET", "POST"])
# def register():
#     form: RegisterForm = RegisterForm()
#     print(form.data)
#     print(form.validate_on_submit())
#     if form.validate_on_submit():
#         print("Hello")
#         if form.password.data != form.password_again.data:
#             return render_template('register.html', title='Регистрация',
#                                    form=form,
#                                    message="Пароли не совпадают")
#         db_sess = db_session.create_session()
#         if db_sess.query(User).filter(User.email == form.email.data).first():
#             return render_template('register.html', title='Регистрация',
#                                    form=form,
#                                    message="Такой пользователь уже есть")

#         db_sess = db_session.create_session()
#         user = User(form.name.data, form.about.data, form.email.data, form.password.data)
#         db_sess.add(user)
#         db_sess.commit()
#         return redirect("/login")
    
#     return render_template('register.html', title='Регистрация', form=form)



# @user_bp.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         db_sess = db_session.create_session()
#         user = db_sess.query(User).filter(
#             User.email == form.email.data).first()
#         if user and user.check_password(form.password.data):
#             login_user(user, remember=form.remember_me.data)
#             return redirect("/")
#         return render_template('login.html',
#                                message="Неправильный логин или пароль",
#                                form=form)
#     return render_template('login.html', title='Авторизация', form=form)


# @user_bp.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect("/")
