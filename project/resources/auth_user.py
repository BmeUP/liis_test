def is_user_auth(session, user, name, password, salt):
    with session() as ses:
            user = ses.query(user).filter_by(name=name).all()
            if user:
                return user[0].check_password(password, salt)
            else:
                return "There is no user with this name => {}".format(name)
