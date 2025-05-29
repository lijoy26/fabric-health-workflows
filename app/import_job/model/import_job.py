# app/models/import_job.py
from datetime import datetime
from app import db

class ImportJob(db.Model):
    __tablename__ = 'import_jobs'

    import_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pipeline_id = db.Column(db.Integer, nullable=False)
    starttime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    endtime = db.Column(db.DateTime)
    status = db.Column(db.String, nullable=False)
    triggered_by = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)