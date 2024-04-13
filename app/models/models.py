from app.extensions import db
from datetime import datetime, timezone

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    trips = db.relationship('Trip', backref='user', lazy=True)

class Trip(db.Model):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    start_location_latitude = db.Column(db.String(50), nullable=False)  # Changed to String
    start_location_longitude = db.Column(db.String(50), nullable=False)  # Changed to String
    end_location_latitude = db.Column(db.String(50), nullable=False)  # Changed to String
    end_location_longitude = db.Column(db.String(50), nullable=False)  # Changed to String
    trip_duration = db.Column(db.String(255), nullable=False)
    time_of_trip = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


    def to_dict(self):
        return {
            "start_location": {
                "latitude": self.start_location_latitude,
                "longitude": self.start_location_longitude
            },
            "end_location": {
                "latitude": self.end_location_latitude,
                "longitude": self.end_location_longitude
            },
            "trip_duration": self.trip_duration,
            "time_of_trip": self.time_of_trip.strftime("%Y-%m-%d %H:%M:%S")
        }
