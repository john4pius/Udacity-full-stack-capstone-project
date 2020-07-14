# Udacity-full-stack-capstone-project

This project allow students to apply the skills learnt in this program.



### Aims:
1. Create data models representing `Movies`, `Actors` in `models.py`.  
2. use `auth.py` to verify permissions of the user role.  
3. perform database migrations.  
4. API flask server for `CRUD` in `app.py`  
5. Automated tests in `test_app.py`  
6. deploy application to heroku.  

### Technologies
- Python/Flask
- Auth0
- SQLAlchemy
- Flask-Migrate
- Flask-Cors
- Flask-Script

### Getting Started


```
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ source ./setup.sh
$ python3 manage.py db init
$ python3 manage.py db migrate
```

### Running the server
To run the server, execute:
```
$ export FLASK_APP=app
$ export FLASK_ENV=development
$ FLASK_AP=app.py flask run
```
Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.
Setting the FLASK_APP variable to app directs flask to use the app.py file, which contains the main app methods.

### running tests

```
$ python3 test_app.py
```

### hosted heroku app




### Tokens

Authentication is done via Auth0 
Login with the following:

## Roles

1.Casting assistant:  
- to view actors `GET /actors (get:actors)`
- to view movies `GET /movies (get:movies)`

2.Casting Director:  
- to view actors `GET /actors (get:actors)`
- to view movies `GET /movies (get:movies)`
- update actors `PATCH /actors (update:actors)`
- update movies `PATCH /movies (update:movies)`
- add actors `POST /actors (post:actors)`
- remove actors `DELETE /actors (delete:actors)`

3.Executive Producer:  
- to view actors `GET /actors (get:actors)`
- to view movies `GET /movies (get:movies)`
- update actors `PATCH /actors (update:actors)`
- update movies `PATCH /movies (update:movies)`
- add actors `POST /actors (post:actors)`
- remove actors `DELETE /actors (delete:actors)`
- add movies `POST /movies (post:movies)`
- remove movies `DELETE /movies (delete:movies)`

## endpoints

---

```
GET /
```
- description: simple health check
- request arguments: `None`
- returns a status health check of the app

--- 
Resource Movies:

  
```
GET /movies  
```

- description: list of movies
- required-permission: `get:movies`
- request arguments: None
- returns: list of movies
```
{
    "success": True,
    "movies": [{ 
      id: 1,
      title: "Dwayne Johnson", 
      release_date: "Tue, 14 July 2020 00:00:00 GMT"
    }]
}
```

---

```
POST /movies  
```
- description: creates movies
- required-permission: `post:movies`
- request arguments: 
  - title (required): `string`
  - release_date (required): `string`

- returns: status and data of newly created movie
```
{
    "success": True,
    "movies": [{ 
      id: 2,
      title: "MI3", 
      release_date: "Mon, 13 July 2020 00:00:00 GMT"
    }]
}
```

---

```
PATCH /movies/<id>
```
- description: updates movie
- required-permission: `patch:movies`
- request arguments: 
  - title (optional): `string`
  - release_date (optional): `date`

- returns status of updated movie
```
{
    "success": True,
    "movies": [{ 
      id: 2,
      title: "MI2", 
      release_date: "Mon, 13 July 2020 00:00:00 GMT"
    }]
}
```

---

```
DELETE /movies/<id>
```
- description: deletes movie
- required-permission: `delete:movies`
- request arguments: None
- return status of deleted movie
```
{
    "success": True,
    "delete": 2
}
```

---

Resource Actors:

```
GET /actors  
```
- description: list of actors
- required-permission: `get:actors`
- request arguments: None
- returns a list of actors

```
{
    "success": True,
    "actors": [{ 
      id: 1,
      name: "Dwayne Johnson", 
      age: 53,
      gender: "Male"
    }]
}
```

---

```
POST /actors  
```
(requires authorization header of `post:actors`)
- description: create actor
- required-permission: `post:actors`
- request arguments: 
  - name (required): string
  - age (required): number
  - gender (required): string

- returns status of created actor
```
{
    "success": True,
    "actors": [{ 
      id: 2,
      name: "Mark", 
      age: 45,
      gender: "Male"
    }]
}
```

---

```
PATCH /actors/<id>
```
(requires authorization header of `patch:actors`)
- description: updates actor
- request arguments:
  - name (optional): string
  - age (optional): number
  - gender (optional): string

- returns status of updated actor

```
{
    "success": True,
    "actors": [{ 
      id: 1,
      name: "Mark", 
      age: 46,
      gender: "Male"
    }]
}
```

---

```
DELETE /actors/</id>
```
- description: deletes actor
- required-permission: `delete:actors`
- request arguments: None
- return status of deleted actor
```
{
    "success": True,
    "delete": 2
}
```

---


👤 **John Pius**

- Github (https://github.com/john4pius)
- Linkedin (https://www.linkedin.com/in/john-pius)
- Twitter (@John4pius)


## 🤝 Contributing
Contributions, issues and feature requests are welcome!


## Show your support

Give a ⭐️ if you like this project!