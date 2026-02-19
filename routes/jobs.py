# Job Listings Endpoints

from flask import Blueprint, jsonify, request
from models import JobListing

# Create a Blueprint for job listings routes
jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('/jobs', methods=['GET'])
def get_job_listings():
    """
    Get a list of job listings.
    """
    listings = JobListing.query.all()
    return jsonify([job.to_dict() for job in listings]), 200

@jobs_bp.route('/jobs', methods=['POST'])
def create_job_listing():
    """
    Create a new job listing.
    """
    data = request.get_json()
    new_job = JobListing(
        title=data['title'],
        description=data['description'],
        location=data['location'],
        salary=data['salary']
    )
    new_job.save()
    return jsonify(new_job.to_dict()), 201

# Register the Blueprint in your app
# app.register_blueprint(jobs_bp)