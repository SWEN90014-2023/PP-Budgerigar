# PP-Budgerigar

This project aims to assist clinicians in analyzing their patients more effectively by gathering information from their daily activities. Currently, the project has a data collection interface called AWARE that can gather the daily information of every patient who uses it. To help clinicians analyze their patients more objectively, a visualization system is needed to process and display the data collected. This will be a valuable tool for clinicians, who will no longer have to rely solely on patient reports to make informed decisions.

**Project Directory**

<details>
<summary>Click to expand directory</summary>
   
- [Project Structure](#project-structure)
- [Database Structure](#database-structure)

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


## Database Structure

The project's database structure is as follows:
**Purpose**: Stores information about clinicians (medical users).
- **doc_id** (Primary Key): Unique identifier for clinicians.
- **username**: Clinician's username for login.
- **password**: Clinician's password for login authentication.
- **name**: Clinician's name.
- **phone**: Clinician's phone number (optional).

## patientInfo Table
**Purpose**: Stores information about patients, including their associated clinician.
- **pa_id** (Primary Key): Unique identifier for patients.
- **doc_id** (Foreign Key): Relates to the clinician (clinicianInfo table) ID.
- **name**: Patient's name.
- **password**: Patient's password for login authentication.
- **age**: Patient's age (optional).
- **sex**: Patient's gender (optional).
- **info**: Additional patient information, can be stored using a text field.
- **create_time**: Timestamp of record creation.

## screen Table
**Purpose**: Stores raw screen usage data.
- **_id** (Primary Key): Unique identifier for data entries.
- **timestamp**: Timestamp, records the time of data.
- **device_id**: Unique identifier for devices.
- **screen_status**: Screen status (e.g., on or off).

## daily_unlock Table
**Purpose**: Records the number of device unlocks on a daily basis categorized by specific time intervals.
- **id** (Primary Key): Auto-incremented identifier for entries.
- **date**: The date of record.
- **device_id**: Identifier for devices.
- Hourly categorized unlocks (e.g., `0_2_unlocks`): Count of unlocks.

## daily_durations Table
**Purpose**: Records the total duration of device usage on a daily basis categorized by specific time intervals.
- **id** (Primary Key): Auto-incremented identifier for entries.
- **date**: The date of record.
- **device_id**: Identifier for devices.
- Hourly categorized durations (e.g., `0_2_duration`): Duration of usage in hours/minutes.

## weekly_unlocks Table
**Purpose**: Records the number of device unlocks on a weekly basis categorized by weekdays.
- **id** (Primary Key): Auto-incremented identifier for entries.
- **week_start**: The starting date of the week.
- **device_id**: Identifier for devices.
- Weekday categorized unlocks (e.g., `Monday`, `Tuesday`): Count of unlocks.

## weekly_durations Table
**Purpose**: Records the total duration of device usage on a weekly basis categorized by weekdays.
- **id** (Primary Key): Auto-incremented identifier for entries.
- **week_start**: The starting date of the week.
- **device_id**: Identifier for devices.
- Weekday categorized durations (e.g., `Monday`, `Tuesday`): Duration of usage in hours/minutes.

