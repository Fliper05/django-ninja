# Task Manager API Documentation
## Overview
This API allows you to perform CRUD operations on a Task model.

## Endpoints
### GET /tasks/
Returns a list of all tasks.

### POST /tasks/
Creates a new task. The body of the request should be a JSON object with the following fields:

title: The title of the task.
description: The description of the task.
status: The status of the task. Can be ‘created’, ‘in_progress’, or ‘completed’.
### PUT /tasks/{task_id}/
Updates an existing task. The body of the request should be a JSON object with the fields you want to update.

### DELETE /tasks/{task_id}/
Deletes an existing task.

## Running the Application
To run the application, use the following command:

`docker-compose up`

or if you don't want to use docker, you can install the app by creating a venv and running the `python manage.py runserver` command manually. Just note that you will have to migrate the database and setup any other peresquities.