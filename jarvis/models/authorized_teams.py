from jarvis_run import db


#  DB Configurations Go Here
class AuthorizedTeams(db.Model):
    __tablename__ = 'authorized_teams'
    record_number = db.Column(db.Integer, primary_key=True, autoincrement="auto", unique=True)
    team = db.Column(db.String, nullable=False)
    team_token = db.Column(db.String, nullable=False)
    date_added = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<AuthorizedTeams(record_number='%s', team='%s', team_token='%s', date_added='%s' )>" % \
               (self.record_number, self.team, self.team_token, self.date_added)
