Pet Adoption App
================

This is a simple web application developed using Flask and SQLAlchemy, that helps manage pet adoption.

Features
--------

-   List all available pets
-   Add new pets to the adoption list
-   Edit the details of existing pets
-   Track the adoption status of each pet

Setup and Installation
----------------------

1.  Clone the repository:

    bashCopy code

    `git clone https://github.com/yourusername/pet-adoption-app.git
    cd pet-adoption-app`

2.  Create and activate a virtual environment:

    bashCopy code

    `python3 -m venv env
    source env/bin/activate`

3.  Install the requirements:

    bashCopy code

    `pip install -r requirements.txt`

4.  Set up the database:

    Open PostgreSQL with the command `psql -d postgres` in your terminal.

    Then, create the database:

    bashCopy code

    `CREATE DATABASE pet_adopt;`

    Exit PostgreSQL and seed the database:

    bashCopy code

    `python3 seed.py`

5.  Run the server:

    bashCopy code

    `flask run --debug`

Now, navigate to `http://localhost:5000` in your web browser to access the application.

Usage
-----

-   Navigate to `http://localhost:5000/add` to add a new pet.
-   Click on the name of a pet in the list to view and edit details.
-   Mark a pet as adopted by toggling the 'Available' checkbox in the pet's details page.

Technologies Used
-----------------

-   Python
-   Flask
-   SQLAlchemy
-   WTForms
-   PostgreSQL
-   Bootstrap

This application is a great example of how to build a CRUD application using Flask and SQLAlchemy with a PostgreSQL database. You can use it as a starting point for more complex projects.