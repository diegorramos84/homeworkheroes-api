# homeworkheroes-api

This is the backend of the HomeworkHeroes app

## Installation
Begin by using pip to install Pipenv and its dependencies
``` bash
pip install pipenv
```
Then change directory to the folder containing your Python project and initiate Pipenv,
```bash
cd homeworkheroes-api
pipenv install
```

## Usage

Available endpoints:

### Students

```python
<!-- Student model for registration -->
  {
    "name": "Oreo Choc",
    "email": "oreochoc@mail.com",
    "school": "Best shcool of London",
    "school_class": "3C",
    "date_of_birth": "YYYYMMDD",
    "level": 1,
    "password": "secret",
    "avatar": "avatar_url",
    "role": "student"
  }
```

| Method | URL | Description |
|:-------------:|:-------------:|:-----:|
| `GET` | `/students` | list all students with their assignments if any |
| `POST` | `/register` | create a new student |
| `POST` | `/login` | login as a student |
| `POST` | `/logout` | logout student |
| `GET` | `/students/id` | get a student by its ID |

### Teachers

```python
<!-- Teacher moder for registration -->
  {
    "name": "Mr. Teacher",
    "email": "teacher@mail.com",
    "school": "Best shcool of London",
    "school_class": "3C",
    "level": 1,
    "password": "secret",
    "role": "teacher"
  }
```

| Method | URL | Description |
|:-------------:|:-------------:|:-----:|
| `POST` | `/register` | create a new teacher |
| `POST` | `/login` | login as a teacher |
| `POST` | `/logout` | logout teacher |

### Homework

```python
<!-- Homework model for creating or updating -->
  {
    "subject": "This is a subject",
    "content": "I am content",
    "extra_resources": "www.youtube.com", -> this field is optional
    "teacher_id: 1
  }
```

| Method | URL | Description |
|:-------------:|:-------------:|:-----:|
| `GET` | `/homework` | list all homework available |
| `POST` | `/homework` | create a new homework for a teacher |
| `GET` | `/homework/id` | get a homework by its ID |
| `PATCH` | `/homework/id` | update a specific homework |
| `DELETE` | `/homework/id` | delete a specific homework |

### Assignments

```python
<!-- Assignment model for creating or updating -->
  {
    "deadline": "YYYYMMDD",
    "feedback": "I am a feedback from a teacher",
    "completed": "I am false by default"
    "student_id": 1,
    "homework_id": 1
  }
```

| Method | URL | Description |
|:-------------:|:-------------:|:-----:|
| `GET` | `/assignments` | list all assignments available |
| `POST` | `/assignments` | create a new assignments to a student using a specific homework |
| `GET` | `/assignments/id` | get a assigment by its ID |
| `PATCH` | `/assignments/id` | update a specific assignment (only deadline if available) |
| `DELETE` | `/assignments/id` | delete a specific assigment |


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
