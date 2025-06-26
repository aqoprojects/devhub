💻 DevHub
DevHub is a developer-centric platform where users can create profiles, showcase their skills and projects, connect with other developers, and collaborate. With secure custom authentication and a modular backend design, DevHub provides a seamless and secure experience for networking and project discovery in the dev community.

✨ Features
  - Custom Authentication system (no third-party packages)
  - Argon2id password hashing for strong security
  - Create and edit profiles, including bio and avatar
  - Add, edit, and delete projects
  - Tag projects with technologies used
  - Add and edit technical skills
  - Rate and review other developers' projects
  - See average ratings and detailed reviews on project pages
  - Send and receive direct messages with other developers
  - View other developer profiles and their public projects
  - Attach source code links (e.g., GitHub) to projects
  - Fully responsive design for desktop and mobile

LIVE LINK: https://devhubb.pythonanywhere.com/

🛠️ Backend Architecture
The backend is custom-built for control, scalability, and security:

✅ Custom Forms for posting and updating data (projects, skills, reviews, messages)

✅ Custom Authentication Backend with complete control over login and registration logic

✅ Argon2id Password Hasher for top-tier password security

✅ Custom Database Router for future scalability (e.g., separating user and content databases)

✅ Modular Models Structure: all models are organized inside a models module within their respective Django apps

✅ Custom Validators for fields like usernames, project links, and skill inputs to enforce strict validation

LIVE LINK: https://devhubb.pythonanywhere.com/

📁 Tech Stack
Frontend: HTML, CSS (Tailwind or custom), JavaScript (optionally React/Vue if used)
Backend: Django
Database: PostgreSQL, MYSQL or SQLite (sqlite3 was used for test host)
Authentication: Custom, using Argon2id hashing (via argon2-cffi or Django's argon2)

Hosting: pythonanywhere

Other Tools: Django widget-tweaks, django eviron (to secure sensitive datat)...

📌 Future Improvements
Real-time messaging using WebSockets (Django-channels, redis)
Project bookmarks / likes
Notification system (new reviews, total weekly project views , messages, follows)
adding other technologies for project enhancement and automation purposes e.g (docker, celery, redis, reactJs, aws hosting, REST API ..)

LIVE LINK: https://devhubb.pythonanywhere.com/
