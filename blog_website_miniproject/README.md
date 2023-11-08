# Miniproject - Blog Website

This documentation explains a Flask-based blog application that allows users to register, log in, create, edit, and delete posts, comment on posts, and view all blog posts. It uses Flask extensions like Flask-Bootstrap, Flask-CKEditor, Flask-Gravatar, and Flask-SQLAlchemy to enhance the functionality and design.

## Purpose

The purpose of this application is to provide a simple blogging platform for users. It enables user registration, authentication, and basic CRUD operations for blog posts. Users can also leave comments on posts.

## Dependencies

- `Flask`: A micro web framework for Python.
- `Flask-Bootstrap`: Integration of the Bootstrap framework into Flask.
- `Flask-CKEditor`: A CKEditor extension for Flask.
- `Flask-Gravatar`: Gravatar support for Flask.
- `Flask-Login`: User session management.
- `Flask-SQLAlchemy`: SQLAlchemy integration with Flask.
- `Werkzeug`: A Python library for password hashing and checking.

## Usage

1. Users can register and log in using the registration and login forms.
2. Registered users can create, edit, and delete blog posts.
3. Users can view all blog posts on the home page.
4. Users can click on a post to view the full post and leave comments.
5. Admin users (user ID 1) can create, edit, and delete posts.
6. Admin users can also perform CRUD operations on posts.
7. Users can log out to end their session.

## User Roles

- Admin Users: User ID 1 is considered an admin user with special privileges.

## Database Tables

1. `BlogPost`: Stores information about blog posts.
2. `User`: Stores user data, including email, hashed password, and name.
3. `Comment`: Stores user comments on blog posts.

## Gravatar

The application uses the Gravatar service to display user avatars based on their email addresses.

## Password Hashing

User passwords are hashed using the PBKDF2 algorithm to ensure security.

## Decorators

- `admin_only`: Ensures that only admin users can access specific routes and perform certain actions.

## Routing

- `/register`: User registration and account creation.
- `/login`: User login.
- `/logout`: User logout.
- `/`: Home page displaying all blog posts.
- `/post/<int:post_id>`: View a specific blog post and add comments.
- `/new-post`: Create a new blog post.
- `/edit-post/<int:post_id>`: Edit an existing blog post.
- `/delete/<int:post_id>`: Delete a blog post.
- `/about`: About page.
- `/contact`: Contact page.

## License

This application is provided for educational and personal use. Please respect any licensing and usage restrictions associated with the dependencies and Flask extensions used in the application.

Enjoy using this Flask-based blog application for managing your blog and posts!
