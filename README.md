# Simple Django Product Catalog

## Overview

This repository contains a basic Django web application designed to function as a minimalist product catalog or item listing page.

The project demonstrates the core functionality of connecting a Django view to a database model to retrieve and display data, as seen in the index view. It also includes a placeholder view for future functionality.

## Features

- Responsive Product Grid: Displays products in a responsive grid layout using Bootstrap's column system (e.g., 2, 3, or 4 cards per row depending on screen size).

- Django Admin Integration: Supports managing Product and Offer data via the built-in Django administrative interface.

- Static Image Serving: Configured to serve product images locally, solving external hotlinking issues.

- Clean Price Formatting: Prices are displayed without unnecessary trailing decimals (e.g., Rs.134000 instead of Rs.134000.0).

## Prerequisites

Before running this application, you need to have the following installed on your system:

- Python (3.8 or newer recommended)

- pip (Python package installer)

- Git (for cloning the repository)

## Installation and Setup

Follow these steps to get your development environment running locally.

1. Clone the Repository

Clone the project files from GitHub and navigate into the main directory (where manage.py is located):
```
git clone <repository-url>
cd simple-django-product-catalog
```

2. Create and Activate Virtual Environment

It is best practice to install dependencies in an isolated environment.

On Mac/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

On Windows:
```
python -m venv venv
.\venv\Scripts\activate
```

3. Install Dependencies

Install the necessary packages using the provided requirements.txt file:
```
pip install -r requirements.txt
```

4. Database Setup

Apply migrations to create the database tables (Product and Offer):
```
python manage.py migrate
```

5. Create Superuser (for Admin Access)

Create an administrative user account so you can log into the Django Admin and add data.
```
python manage.py createsuperuser
```

## Adding Product Images

To ensure images display correctly for all users (solving hotlinking errors), images must be hosted inside the project:

Create the Static Folder: Ensure you have the structure products/static/products/ inside your project.

Upload Images: Save your product images (e.g., iphone_14_pro_max.jpg) inside the products/static/products/ folder.

Update Admin: In the Django Admin, update the product's image_Url field to just the file path, e.g., products/iphone_14_pro_max.jpg.

## Running the Application

1. Start the Development Server

Run the local Django development server:
```
python manage.py runserver
```

2. Access the Site

The application will now be running on your local machine:

Feature

URL

Product List
```
http://127.0.0.1:8000/
```
Admin Panel
```
http://127.0.0.1:8000/admin
```
"New Product" View
```
http://127.0.0.1:8000/new
```
Note: You must log into the Admin Panel to add Product and Offer data before anything will appear on the main / page.

>Important Security Note
The settings.py file contains sensitive data (like the SECRET_KEY). When pushing to GitHub, ensure that you have configured your environment to load the SECRET_KEY from a secure source (like a local .env file that is listed in your .gitignore).

