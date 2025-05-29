# app/fhir_import/routes.py
from flask import Blueprint, jsonify
from datetime import datetime
from app.extensions import db
from app.import_job.model.import_job import ImportJob

import_bp = Blueprint('fhir', __name__)

@import_bp.route('/trigger', methods=['POST'])
def create_entry():
    try:
        job = ImportJob(
            pipeline_id=1,
            starttime=datetime.utcnow(),
            status='STARTED',
            triggered_by='admin',
            created_at=datetime.utcnow()
        )
        db.session.add(job)
        db.session.commit()

        return jsonify({
            'import_id': job.import_id,
            'pipeline_id': job.pipeline_id,
            'starttime': job.starttime.isoformat(),
            'status': job.status,
            'triggered_by': job.triggered_by,
            'created_at': job.created_at.isoformat()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
