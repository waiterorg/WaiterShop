# WaiterShop
---

### Setup

1. Download the Repository to your local machine <br>
2. Create a Virtual Environment in the [WaiterShop](./) folder with this command below <br>
   `python -m venv venv`
3. Activate the environment with this command <br>
   `.\venv\Scripts\activate`
4. Install the dependencies <br>
   `pip install -r requirements.txt `

### Running the Application

1. Activate the environment with this command. <br>
   `.\venv\Scripts\activate`
2. Start the application by running this command (_Run the command where [manage.py](./WaiterShop/manage.py) is
   located_) <br>
   ` python manage.py runserver`

### Accessing the Admin Panel

1. You can access the admin panel by running the server and opening <http://localhost:8000/admin>
2. Run `python manage.py createsuperuser` to create a user to access the admin panel.
3. Set up the Username and Password
4. You can log in and change the database values anytime.



## How buy products
  1. In home or our products page click on one item
  2. you should see price and detail of those item
  3. if you want it, click add to cart
  4. login to site
  5. you can back to products page with continue shopping botton and add other items in your cart
  6. or click on proceed to checkout for buy your cart items
  7. fill your shipping adress form
  8. if you have shipping address in site,you can use Use default shipping address checkbox
  9. choice your payment option
  10. click continue to checkout


## User Stories
  - A user can rate products if logged in .
  - A user can have refund request on 'request-refund/' endpoint .
  - A user can have coupon for reduce the price .
  - A user can search products on top navigation .


## Features
  
  - category
    - items ordered by category
    - can click on category name and just see items for those category

  

## Dependencies
  - Python
  - Django
  - SQLite
  - DRF
  - Django Packages

## What the app looks like
![ScreenShot](screenshots/ScreenshotHome.png)


![ScreenShot](screenshots/ScreenshotAboutUs.png)

# RESTAPI
  this api is based on JWT Auth, if you dont know RESTfulAPI what is it, visit https://restfulapi.net/ .
## URLs
  - http://127.0.0.1:8000/api/rest-auth/login/
  - http://127.0.0.1:8000/api/v1/products/
  - http://127.0.0.1:8000/api/v1/products/8/
  - http://127.0.0.1:8000/api/v1/about-us/
  - http://127.0.0.1:8000/api/v1/contact-us/
  - http://127.0.0.1:8000/api/v1/order-summary/
  - http://127.0.0.1:8000/api/v1/checkout/
