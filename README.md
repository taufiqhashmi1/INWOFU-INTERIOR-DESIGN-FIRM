# INWOFU - Interior Design Portfolio Website

A dynamic and elegant portfolio website for a luxury interior design firm, built with Python (Django) and Tailwind CSS. The project features a custom CMS for managing projects and an immersive, animated frontend.

![INWOFU Screenshot](placeholder.png) ## About The Project

This project is a fully-featured, custom-coded portfolio website designed to showcase high-end interior design projects. It combines a sophisticated, animated user experience on the frontend with a powerful, easy-to-use content management system on the backend, all powered by Django. The site is designed to be fully responsive and easily maintainable.

## Key Features

* **Dynamic Project Management:** Create, update, and delete interior design projects. Each project has its own dynamically generated detail page.
* **Full CMS Backend:** The user-friendly Django Admin panel allows the site owner to manage all project content, including titles, descriptions, and multiple gallery images per project, without touching any code.
* **Interactive Frontend:**
    * An immersive 3D intro animation built with **Three.js**.
    * A responsive, auto-scrolling project carousel using **SwiperJS**.
    * A seamless marquee of company stats.
    * CSS animations for a polished user experience.
* **Fully Responsive Design:** A mobile-first approach ensures a seamless experience on all devices, complete with a collapsing hamburger menu.
* **Functional Contact Form:** Captures user inquiries and saves them directly to the database.

## Tech Stack

* **Backend:**
    * Python 3.11+
    * Django 5.0+
* **Frontend:**
    * HTML5
    * Tailwind CSS
    * JavaScript (ES6+)
* **JavaScript Libraries:**
    * SwiperJS (for carousels)
    * Three.js (for the 3D intro)
* **Development Tools:**
    * `django-tailwind` for seamless Tailwind CSS integration.
    * `django-browser-reload` for efficient development.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.11+ and Pip installed.
* A virtual environment tool (`venv`).

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your_username/inwofu.git](https://github.com/your_username/inwofu.git)
    cd inwofu
    ```
2.  **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```
4.  **Install Tailwind CSS dependencies:**
    ```sh
    python manage.py tailwind install
    ```
5.  **Run database migrations:**
    ```sh
    python manage.py migrate
    ```
6.  **Create a superuser to access the admin panel:**
    ```sh
    python manage.py createsuperuser
    ```
7.  **Start the development server:**
    ```sh
    # First terminal: start the Tailwind CSS watcher
    python manage.py tailwind start
    # Second terminal: start the Django server
    python manage.py runserver
    ```

## Usage

Access the admin panel at `http://127.0.0.1:8000/admin/` to log in and start adding new projects. Upload a thumbnail and multiple gallery images for each project to see them appear on the homepage carousel and their respective detail pages.
