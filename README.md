# PP-Budgerigar

This project aims to assist clinicians in analyzing their patients more effectively by gathering information from their daily activities. Currently, the project has a data collection interface called AWARE that can gather the daily information of every patient who uses it. To help clinicians analyze their patients more objectively, a visualization system is needed to process and display the data collected. This will be a valuable tool for clinicians, who will no longer have to rely solely on patient reports to make informed decisions.

**Project Directory**

<details>
<summary>Click to expand directory</summary>
   
- [Project Structure](#project-structure)

</details>

## Project Structure

The project's directory structure is as follows:

```plaintext
< PROJECT ROOT >
   |
   |-- clinic/                             # App handling clinic functionalities
   |    |-- migrations/                    # Database migration scripts
   |    |-- template/                      # Templates for the clinic app
   |    |-- __pycache__/                   # Compiled Python files
   |    |-- admin.py                       # Admin configurations
   |    |-- apps.py                        # App configurations
   |    |-- models.py                      # Database models
   |    |-- tests.py                       # Testing scripts
   |    |-- urls.py                        # URL definitions
   |    |-- views.py                       # Logic for handling requests/responses
   |
   |-- core/                               # Core functionalities
   |    |-- __pycache__/                   # Compiled Python files
   |    |-- asgi.py                        # Entry point for ASGI
   |    |-- settings.py                    # Global settings
   |    |-- urls.py                        # URL definitions
   |    |-- wsgi.py                        # Entry point for WSGI
   |
   |-- db/                                 # Database related directory
   |
   |-- home/                               # Home app
   |    |-- migrations/                    # Database migration scripts
   |    |-- templates/                     # Templates for the home app
   |    |    |-- chartView/                # Chart view templates
   |    |    |    |-- dailyDuration.html   # Daily duration chart
   |    |    |    |-- dailyUnlock.html     # Daily unlock chart
   |    |    |    |-- index.html           # Index page for chart view
   |    |    |    |-- weeklyDuration.html  # Weekly duration chart
   |    |    |    |-- weeklyUnlock.html    # Weekly unlock chart
   |    |    |-- homepage/                 # Homepage templates
   |    |    |    |-- addPatient.html      # Add patient page
   |    |    |    |-- chart.html           # Chart page
   |    |    |    |-- client_table.html    # Client table page
   |    |    |    |-- index.html           # Homepage index
   |    |    |    |-- viewPatient.html     # View patient page
   |    |-- __pycache__/                   # Compiled Python files
   |    |-- admin.py                       # Admin configurations
   |    |-- apps.py                        # App configurations
   |    |-- forms.py                       # Forms definitions
   |    |-- models.py                      # Database models
   |    |-- tests.py                       # Testing scripts
   |    |-- urls.py                        # URL definitions
   |    |-- views.py                       # Logic for handling requests/responses
   |
   |-- nginx/                              # Nginx configurations and related files
   |-- static/                             # Static files (CSS, JS, images, etc.)
   |
   |-- .env                                # Environment variables
   |-- .gitignore                          # Git ignore configurations
   |-- admin_volt_pro.rar                  # Archived file
   |-- build.sh                            # Shell script for building
   |-- CHANGELOG.md                        # Changelog file
   |-- db.sqlite3                          # SQLite3 database
   |-- docker-compose.yml                  # Docker compose configurations
   |-- Dockerfile                          # Docker configurations
   |-- env.sample                          # Environment sample file
   |-- gunicorn-cfg.py                     # Gunicorn configurations
   |-- LICENSE.md                          # License information
   |-- manage.py                           # Django manage script
   |-- README.md                           # This README file
   |-- README_deploy.md                    # Deployment instructions
   |-- render.yaml                         # Render configurations
   |-- requirements.txt                    # Python dependencies
   |-- ************************************************************************
