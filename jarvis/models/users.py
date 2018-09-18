from jarvis_run import db


#  DB Configurations Go Here
class Users(db.Model):
    __tablename__ = 'users'
    record_number = db.Column(db.Integer, primary_key=True, autoincrement="auto", unique=True)
    user_name = db.Column(db.String, nullable=False)
    slack_id = db.Column(db.String, nullable=False)
    date_added = db.Column(db.Integer, nullable=False)
    user_role = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Users(record_number='%s', user_name='%s', slack_id='%s', date_added='%s', user_role='%s')>" % \
               (self.record_number, self.user_name, self.slack_id, self.date_added, self.user_role)
