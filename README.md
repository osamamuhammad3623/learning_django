# Django learning project
- Learning Django back-end framework by applying this simple project.
- It's a simple discussion board, with even more simple front-end.

## Project Description
- A board consists of zero or more topics.
- A topic has zero or more comments on it.
- Users must register/sign up to able to post a topic.
- Only admin/s can add boards, but users can add topics & comments in boards.

## Database Description
- A board record has an ID, name & description.
- A topic record has an ID, subject (title) and foreign keys to its board and author.
- A comment record has an ID, the comment/message, and foreign keys to its topic and author.
- User (Django's default authentication model).