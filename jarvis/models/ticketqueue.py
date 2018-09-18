from jarvis_run import db


#  DB Configurations Go Here
class TicketQueue(db.Model):
    __tablename__ = 'ticket_queue'
    record_number = db.Column(db.Integer, primary_key=True, autoincrement="auto", unique=True)
    case_number = db.Column(db.String, nullable=False)
    creation_timestamp = db.Column(db.Integer, nullable=False)
    requestor_uid = db.Column(db.String, nullable=False)
    requester_uname = db.Column(db.String, nullable=False)
    ackedby_uid = db.Column(db.String)
    ackedby_uname = db.Column(db.String)
    acked_timestamp = db.Column(db.Integer)
    closedby_uname = db.Column(db.String)
    closedby_uid = db.Column(db.String)
    closed_timestamp = db.Column(db.Integer)
    priority = db.Column(db.String, default="P3")
    escalated = db.Column(db.String, default="N")
    escalatedby_uname = db.Column(db.String)
    escalatedby_uid = db.Column(db.String)
    escalation_timestamp = db.Column(db.Integer)
    description = db.Column(db.String)
    casetype = db.Column(db.String)

    def __repr__(self):
        return "<TicketQueue(record_number='%s', case_number='%s', creation_timestamp='%s', requestor_uid='%s', " \
               "requester_uname='%s', ackedby_uid='%s', ackedby_uname='%s', acked_timestamp='%s', closedby_uname='%s', " \
               "closedby_uid='%s', closed_timestamp='%s', priority='%s', escalated='%s', escalatedby_uname='%s', " \
               "escalatedby_uid='%s', escalation_timestamp='%s', description='%s', casetype='%s')>" % \
               (self.record_number, self.case_number, self.creation_timestamp, self.requestor_uid,
                self.requester_uname,
                self.ackedby_uid, self.ackedby_uname, self.acked_timestamp, self.closedby_uid, self.closedby_uname,
                self.closed_timestamp, self.priority, self.escalated, self.escalatedby_uname, self.escalatedby_uid,
                self.escalation_timestamp, self.description, self.casetype)
