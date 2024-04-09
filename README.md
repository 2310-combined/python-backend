
# Streaming On The Go BE Python Repo

## Introduction

This repository contains the backend code for the Capstone 2310 project Streaming On The Go, implemented in Python with Flask. It includes RESTful APIs, database models, and migrations necessary for the project's functionality. We used Pytest to test the routes and models.

## Contributors 

- **Scott DeVoss** - *[LinkedIn](https://www.linkedin.com/in/scott-devoss/), [GitHub](https://github.com/scottdevoss)*  
- **Nathan Lambertson** - *[LinkedIn](https://www.linkedin.com/in/nathan-lambertson/), [GitHub](https://github.com/lambo1986)*

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.12 or higher
- PostgreSQL 14 or higher
- Git

## Getting Started

Follow these steps to get your development environment set up:

1. **Clone the Repository**

   ```
   git clone git@github.com:2310-combined/python-backend.git
   ```

2. **Setup Python Virtual Environment**

   ```
   python3 -m venv venv
   source venv/bin/activate
   python3 -m pip install --upgrade pip
   ```

3. **Install Dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Database Setup**

   After installing PostgreSQL, create a database for the project and update the `SQLALCHEMY_DATABASE_URI` in your configuration to point to your database. (You may want to create a .env in the root directory to hide credentials)

5. **Run Migrations**

   ```
   flask db upgrade
   ```

6. **Run the Application**

   ```
   flask run
   ```

## Testing

To run tests, ensure you have pytest installed:

```
pip install pytest
```

Then execute the tests using:

```
pytest
```

## Useful Commands

Here are some additional commands that may be useful during development:

- **Install Flask-CORS**

  ```
  pip install flask-cors
  ```

- **Initialize Database**

  ```
  flask db init
  ```

- **Create a Migration**

  ```
  flask db migrate -m "custom message"
  ```

- **Apply Migrations**

  ```
  flask db upgrade
  ```

## Endpoints

Note: Endpoints examples use flask local host.
Here are the endpoints you can use to access the database:

- Post User

```
POST http://127.0.0.1:5000/users

{
  "email": "example@mails.com",
  "first_name": "Joe",
  "last_name": "Dude"
}
```

- Show User

```
GET http://127.0.0.1:5000/users/:id
```

- Index Users

```
GET http://127.0.0.1:5000/users
```

- Update User

```
PUT http://127.0.0.1:5000/users/:id

!Coming Soon!
```

- Create Trip

```
POST http://127.0.0.1:5000/users/:id/trips

{
  "start_location": "-541343, 24734",
  "end_location": "-45458 349043",
  "trip_duration": "704",
  "time_of_trip": "2024-03-23 13:11:01"
}
```

- Index User's Trips

```
GET http://127.0.0.1:5000/users/:id/trips
```

- Delete Trip

```
DELETE http://127.0.0.1:5000/trips/:id
```

## Contributing

If you have a recommendation for improvements, please feel free to make a pull request!

## Acknowledgments 
  - Project concept by [Jamie Francisco](https://www.linkedin.com/in/jamiefrancisco/)
  - Technical direction, consultation, and moral support by [Jeremiah Black](https://www.linkedin.com/in/jeremiah-blackol/) and [Khoa Nguyen](https://www.linkedin.com/in/khoa-n323/)
  - This project completed by Mod 4 students at [Turing School of Software and Design](https://turing.edu/)