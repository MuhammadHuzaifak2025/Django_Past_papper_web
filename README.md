## Django Past Papper Web
## Overview

The `Web_pastpaper` app is a Django-based application designed to provide an API for retrieving past examination papers based on subject codes. The app utilizes Django REST Framework for API creation and manages data related to subjects, years, and examination papers through Django models.

## Features

- Retrieve past papers for a given subject code.
- Get links to various types of examination papers, including midterms, finals, and lab exams.
- Provides data in JSON format for easy integration with frontend applications or other services.

## Requirements

- Python 3.x
- Django 3.x or higher
- Django REST Framework 3.x or higher

## Installation

1. **Clone the repository:**
    ```sh
    git clone git@github.com:MuhammadHuzaifak2025/Django_Past_papper_web.git
    cd Web_pastpaper
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## Usage

### API Endpoint

- **Endpoint:** `/api/papers/<subject_code>/`
- **Method:** GET

This endpoint retrieves all the past papers related to the given subject code.

### Example Request

```http
GET /api/papers/MATH101/
