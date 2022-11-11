# Myrag

## Introduction
Myrag is a online store specialising in selling a range of colourful durags. The name plays on the item of focus - durag, and aims to help the end user feel a personal connection to the item.

### Site Owner Goal
Make a profit through the sale of headwraps using this website and to build a community of users.

### External User Goal
Find out more information about these custom headwraps and make an informed secure purchase.

### User Stories

### View & Navigation

![Desktop View](documentation/epics/view-navigation-us.png)

### Registration & User Accounts

![Desktop View](documentation/epics/registration-useraccounts-us.png)

### Customisation

![Desktop View](documentation/epics/customisation-us.png)

### Purchasing & Checkout

![Desktop View](documentation/epics/purchasing-checkout-us.png)


### Wireframes

#### Main Page

![Mobile View](documentation/wireframes/main.png)

#### Colour Customisation

![Mobile View](documentation/wireframes/color-custom.png)

#### Material Customisation

![Mobile View](documentation/wireframes/material-custom.png)

#### Custom Message

![Mobile View](documentation/wireframes/message-custom.png)
 
#### Gallery

![Mobile View](documentation/wireframes/gallery.png)
 
#### FAQ & Delivery

![Mobile View](documentation/wireframes/faq-delivery.png)
 
#### Register

![Mobile View](documentation/wireframes/register.png)
 
#### Sign in

![Mobile View](documentation/wireframes/sign-in.png)
 
#### Profile Information & Card Details

![Mobile View](documentation/wireframes/profile.png)
 
#### Order History

![Mobile View](documentation/wireframes/order-history.png)
 
#### Customer Reviews

![Mobile View](documentation/wireframes/see-reviews.png)
![Mobile View](documentation/wireframes/write-review.png)
 
#### Order List

![Mobile View](documentation/wireframes/order-list.png)
 
#### Upload to gallery

![Mobile View](documentation/wireframes/gallery-upload.png)


### Entity Relationship Diagram

![ERD](documentation/wireframes/erd.png)


### Methodology - Agile

I decided to take an agile approach for the construction of my site. I made use of the projects section on GitHub, to impliments a MoSCoW prioritization technique.
I molded a user story template and used this to create, and organise my user stories into 3 seperate lists. Lists which defined where each user story was, in terms of progress.
To-do, in progress and done, all adequately named for the goal at hand.

![Projects Board](documentation/wireframes/projects-board.png)


### SEO & Marketing

#### FB Mockup

I created a facebook page for fans of myrag to have a space to communicate questions and find out more information.

![Facebook page myrag](documentation/marketing/myrag-fb-page.png)


#### Sitemap & Robots


## Design

### Color Scheme

![Color pallet](documentation/features/color-palette.png)

I wanted the background to have dark but positive colours. I explored this by using lighter and darker blues throughout the website. This was to give the product images the ambience needed to thrive and take center stage.


### Font Choice

I went on google fonts and browsed through a selection of fonts. I used a variety of sample text to have visual comparison and settled on what I found to be a sleek font for the headings (Prata) of my webpages and a tidy font (Lato) for the data. 


### CRUD Functionality

#### Admin 
- The admin users of myrag have the ability to delete products.
- The admin users of myrag have the ability to create products.
- The admin users of myrag have the ability to update products.
- The admin users of myrag have the ability to delete users.

#### User
- The user has the ability to edit the amount of items in their basket.
- The user has the ability to delete and item from their basket.
- The user has the ability to add an item to their basket.


## Features 

### General

#### Navbar
![Navbar](documentation/features/navbar.png)

#### Footer
![Footer](documentation/features/footer.png)


### Acces to Site

#### Login Page
![Login Page](documentation/features/login.png)

#### Registration Page
![Registration Page](documentation/features/registration.png)


### Main Page

#### Shop Now Call To Action Button
![Shop Now](documentation/features/jumbotron-shop-now.png)

#### Free Delivery Banner
![Free Delivery Banner](documentation/features/free-delivery.png)

#### Gallery of Menu
![Gallery of Menu](documentation/features/browse-selection.gif)


### Product

#### Product Selection
![Product Selection](documentation/features/shop-durag.png) 

#### Product Details
![Product Details](documentation/features/durag-details)

### Add Multiple Durags to basket
![Add to Basket](documentation/features/add-multiple-durags.png)

### Product Admin

#### Product Edit
![Product Edit](documentation/features/edit-durag.png) 

#### Product Add
![Product Add](documentation/features/create-durag.png) 

#### Product Delete
![Product Delete](documentation/features/manage-durag-crud.png) 


### Basket

#### Show Basket
![Show Basket](documentation/features/shopping-basket.png)

#### Remove From Basket
![Remove Basket](documentation/features/shopping-basket-delete.gif)

#### Update Basket Qauntity
![Basket Qauntity](documentation/features/shopping-basket-update.gif)


### Checkout

#### Checkout Page
![Checkout Page](documentation/features/checkout-form.gif)

#### Checkout Confirmation
![Checkout Confirmation](documentation/features/checkout-confirmation.gif)


### Profile

#### Default Delivery Information
![Defaul Delivery Information](documentation/features/default-delivery-information.png)

#### Order History
![Order History](documentation/features/order-history.png)

### Future Features

## Technologies Used

- Git used for version control.
- HTML / CSS3 / [Bootstrap v4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) were used for the structure and overall look and feel of the website.
- [Python] was used for the navigation and maneuverability of the site.
- [Django](https://www.djangoproject.com/) was used as the framework.
- [GitHub](https://github.com/) was used for securely storing code.
- [Gitpod](https://gitpod.io/) is the cloud based IDE.
- Python3 is used for the main code logic.
- PostgreSQL is used for storing data.
- [Heroku](https://heroku.com/) was used for live deployment.
- [ShareX](https://getsharex.com/) for capturing screenshots.
- [Font Awesome](https://fontawesome.com/) was used for the icons seen around the website.
- [Google Fonts](https://fonts.google.com/) was used to select fonts for the website.
- [Coolers](https://coolors.co/) was used as inspiration when selecting color combinations for the website.
- [Draw.io](https://app.diagrams.net/) was used to construct my erd.
- [XML-Sitemaps](https://www.xml-sitemaps.com/) was used to create my sitemap.


## Testing

To view all testing documentation please refer to [TESTING.md](TESTING.md)

## Deployment

### Heroku
The site was deployed using [Heroku](https://heroku.com/). The app can be found using this link - [Myrag](https://myrag.herokuapp.com/).

The steps are as follows:

- Log-in or Sign-up to Heroku.
- From the Dashboard click "New" then "Create New App".
- Enter a project name (unique), select a region then press "Create app".
- This will create an app and open the deploy tab. From here select the "Settings" tab.
- Set your Environment Variables by navigating to Reveal Config Vars. (mention which config vars just the keys no values and env files)
Scroll up and head to the "Deploy" section to choose deployment method. Select "GitHub" and in the "connect to GitHub" section link your GitHub account.
- Scroll down to the manual deploy option and select "Deploy Branch".
- The app will now be built. Once completed a 'Your App Was Successfully Deployed' message and a link will appear.

Make sure you set up these config vars.
- CLOUDINARY_URL
- DATABASE_URL
- EMAIL_HOST_PASS
- EMAIL_HOST_USER
- SECRET_KEY
- STRIPE_PUBLIC_KEY
- STRIPE_SECRET_KEY

### Environ Variables
- Create env.py file.
This file will contain all your keys and database settings.
- Set up these Variables
    - DATABASE_URL (Obtained from heroku)
    - CLOUDINARY_URL (Obtained from cloudinary dashboard once signed up)
    - SECRET_KEY (This is a key made by yourself)
    - DEVELOPMENT
    - SECRET_KEY
    - STRIPE_PUBLIC_KEY
    - STRIPE_SECRET_KEY

### Gmail Email Variables
- Login/Create gmail account
- Navigate to see all settings after clicking on the settings cog.
- Navigate to accounts and import then other google account settings.
- Navigate to security found on the side menu and follow the two step verification instructions.
- Navigate to security app passwords, select mail, select device.
- Select other then write django as the title then copy app password. This will be your EMAIL_HOST_PASS.
- Your EMAIL_HOST_USER is your gmail address.

### Stripe
- Sign up and navigate to the developers tab where you will see API Keys.
- Copy STRIPE_PUBLIC_KEY & STRIPE_SECRET_KEY amd set Heroku Config Vars.

You can test the payment functionality using default card numbers.
- Successful payment 4242 4242 4242 4242
- Requires authentication 4000 0025 0000 3155
- Failed payment 400 0000 0000 9995

### Cloudinary
- Create account/sign in
- Navigate to the dashboard and copy the environment variable
- Add CLOUDINARY_URL to env.py

### Local Deployment

To make a local copy of this project, you can clone it by typing the following in your IDE terminal:

- `git clone https://github.com/devisis/myrag.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/devisis/myrag)

Once your project is ready for coding, you must download the required dependencies from the requirements.txt file. You can type:

- `pip3 install -r requirements.txt`

Please note, for this particular project, there aren't any required dependencies, however, the file is still necessary in order to get the application running on Heroku.
Additionally, Heroku will require a `Procfile`, so you can type:

- `echo web: node index.js > Procfile`

## Credits

### Durag Images

- [Dragon](https://images.unsplash.com/photo-1588704428799-7e0aa46c45cb?ixlib=rb-4.0.3&[label](https://unsplash.com/photos/_bzkoVmkf7E)ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fGR1cmFnfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60)
- [Purple](https://images.unsplash.com/photo-1521129334744-e49785eaf335?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwcm9maWxlLXBhZ2V8NHx8fGVufDB8fHx8&auto=format&fit=crop&w=500&q=60)
- [Black](https://images.pexels.com/photos/8475095/pexels-photo-8475095.jpeg?auto=compress&cs=tinysrgb&w=400)
- [Bandana](https://unsplash.com/photos/_bzkoVmkf7E)
- [Blue](https://www.pexels.com/photo/a-man-looking-at-his-phone-while-sitting-on-a-sofa-7327099/)
- [Red](https://www.pexels.com/photo/man-holding-cigarette-13245646/)
- [White](https://images.pexels.com/photos/13008268/pexels-photo-13008268.jpeg?auto=compress&cs=tinysrgb&w=600)
- [Yellow](https://images.pexels.com/photos/7562692/pexels-photo-7562692.jpeg?auto=compress&cs=tinysrgb&w=400&lazy=load)

### Learning Resources

- [Django Documentation](https://docs.djangoproject.com/en/4.1/)
- [Stack Overflow](https://stackoverflow.com/)
- [W3schools](https://www.w3schools.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/4.6/getting-started/download/)
- [Geeks for Geeks](https://www.geeksforgeeks.org/)
- [Code Institute](https://codeinstitute.net/)

A lot of inspiration has derived from the Code Institute Boutique Ado walkthrough project. It has helped me by in creating a guide for me to follow and adapt. Many thanks to my teachers for creating such a well structured guide and my mentor for help and support.

## Acknowledgements

Firstly I would like to take the opportunity to thank Tim Nelon my mentor for his feedback, advice, time and support. He has helped me come a long way.

Second I would like to thank all Code Institute Tutors, Student Care and Slack for giving me access to all the knowledge needed.
