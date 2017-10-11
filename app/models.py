# _*_ coding: utf-8 _*_
__author__ = 'Yujia Lian'
__date__ = '7/28/17 4:16 PM'

from datetime import datetime
from app import db


# Member model
class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # member id
    name = db.Column(db.String(100), unique=True)  # nick name
    pwd = db.Column(db.String(100))  # password
    email = db.Column(db.String(100), unique=True)  # email address
    phone = db.Column(db.String(11), unique=True)  # phone number
    info = db.Column(db.Text)  # personal infomation
    face = db.Column(db.String(255), unique=True)  # head image
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # register time
    uuid = db.Column(db.String(255), unique=True)  # unique id for user
    userlogs = db.relationship("Userlog", backref="user")  # Member ship record foreign key relationship
    comments = db.relationship("Comment", backref="user")  # comments
    moviecols = db.relationship("Moviecol", backref='user')  # movie collection

    def __repr__(self):
        return "<User %r>" % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# Membership login record
class Userlog(db.Model):
    __tablename__ = "userlog"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # member login id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # member id
    ip = db.Column(db.String(100))  # login ip
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # login time

    def __repr__(self):
        return "<Userlog %r>" % self.id


# label
class Tag(db.Model):
    __tablename__ = "tag"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # id
    name = db.Column(db.String(100), unique=True)  # title
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # add time
    movies = db.relationship("Movie", backref='tag')  # Movie foreign key value

    def __repr__(self):
        return "<Tag %r>" % self.name


# Movie
class Movie(db.Model):
    __tablename__ = "movie"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text)
    logo = db.Column(db.String(255), unique=True)
    star = db.Column(db.SmallInteger)
    playnum = db.Column(db.BigInteger)
    commentnum = db.Column(db.BigInteger)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    area = db.Column(db.String(255))
    release_time = db.Column(db.Date)
    length = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    comments = db.relationship("Comment", backref='movie')
    moviecols = db.relationship("Moviecol", backref='movie')  # movie collection

    def __repr__(self):
        return "<Movie %r>" % self.title


# Future preview movie
class Preview(db.Model):
    __tablename__ = "preview"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # id
    title = db.Column(db.String(255), unique=True)  # title
    logo = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Preview %r>" % self.title


class Comment(db.Model):
    __tablename__ = "comment"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # id
    content = db.Column(db.Text)  # comment content
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # comment movie
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # comment user
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # comment time

    def __repr__(self):
        return "<Comment %r>" % self.id


# movie collection
class Moviecol(db.Model):
    __tablename__ = "moviecol"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # id
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # comment movie
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # comment user
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # comment time

    def __repr__(self):
        return "<Moviecol %r>" % self.id


# Authority
class Auth(db.Model):
    __tablename__ = "auth"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # id
    name = db.Column(db.String(100), unique=True)  # name
    url = db.Column(db.String(255), unique=True)  # adress
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # add time

    def __repr__(self):
        return "<Auth %r>" % self.name


# role
class Role(db.Model):
    __tablename__ = "role"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # id
    name = db.Column(db.String(100), unique=True)  # name
    auths = db.Column(db.String(600))  # Auths that belong to certain role
    admins = db.relationship("Admin", backref='role')  # Administrator
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Role %r>" % self.name


# Admin
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # member id
    name = db.Column(db.String(100), unique=True)  # nick name
    pwd = db.Column(db.String(100))  # password
    is_super = db.Column(db.SmallInteger)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    adminlogs = db.relationship("Adminlog", backref='admin')  # Administrator login record foreign key
    oplogs = db.relationship("Oplog", backref='admin')  # administrator login foreign key

    def __repr__(self):
        return "<Admin %r>" % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# Admin login record
class Adminlog(db.Model):
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True)  # admin login id
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # admin id
    ip = db.Column(db.String(100))  # login ip
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # login time

    def __repr__(self):
        return "<Adminlog %r>" % self.id


# Modify record
class Oplog(db.Model):
    __tablename__ = "oplog"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # admin login id
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # admin id
    ip = db.Column(db.String(100))  # operation ip
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # operation time
    reason = db.Column(db.String(600))  # reason

    def __repr__(self):
        return "<Oplog %r>" % self.id

        # if __name__ == "__main__":
        # db.create_all()

        # role = Role(
        # name="Admin",
        # auths=""
        # )
        # db.session.add(role)
        # db.session.commit()

        # from werkzeug.security import generate_password_hash
        # admin = Admin(
        #     name="imoocmovie",
        #     pwd=generate_password_hash("imoocmovie"),
        #     is_super=0,
        #     role_id=1
        # )
        # db.session.add(admin)
        # db.session.commit()
