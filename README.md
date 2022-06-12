# Myrag

## Introduction
My rag is a custom headwrap website where customers can sort through options to pick and purchase a personalised headwrap based on color, material, style and custom message.


# UX

## Site Owner Goal
Make a profit through the sale of headwraps using this website.

## External User Goal
Find out more information about these custom headwraps and make a purchase.

## User Stories

### View & Navigation
![Desktop View](documentation/epics/view-navigation-us.png)

### Registration & User Accounts
![Desktop View](documentation/epics/registration-useraccounts-us.png)

### Customisation
![Desktop View](documentation/epics/customisation-us.png)

### Purchasing & Ceckout
![Desktop View](documentation/epics/purchasing-checkout-us.png)
 

#### Main Page

![Desktop View](documentation/wireframes/)
![Mobile View](documentation/wireframes/main.png)

#### Colour Customisation

![Desktop View](documentation/wireframes/)
![Mobile View](documentation/wireframes/color-custom.png)

#### Material Customisation

![Desktop View](documentation/wireframes/)
![Mobile View](documentation/wireframes/material-custom.png)

#### Custom Message

![Desktop View](documentation/wireframes/)
![Mobile View](documentation/wireframes/message-custom.png)
 
#### Gallery

![Desktop View](documentation/wireframes/)
![Mobile View](documentation/wireframes/gallery.png)
 
#### FAQ & Delivery

![Desktop View](documentation/wireframes/)
![Mobile View](documentation/wireframes/faq-delivery.png)
 
#### Register

![Desktop View](documentation/wireframes/)
![Mobile View](documentation/wireframes/register.png)
 
#### Sign in

![Desktop View](documentation/wireframes/)
![Mobile View](documentation/wireframes/sign-in.png)
 
#### Profile Information & Card Details

![Desktop View](documentation/wireframes/)
![Mobile View](documentation/wireframes/profile.png)
 
#### Order History

![Desktop View](documentation/wireframes/)
![Mobile View](documentation/wireframes/order-history.png)
 
#### Customer Reviews

![Desktop View](documentation/wireframes/)
![Mobile View](documentation/wireframes/see-reviews.png)
![Mobile View](documentation/wireframes/write-reviews.png)
 
#### Order List

![Desktop View](documentation/wireframes/)
![Mobile View](documentation/wireframes/order-list.png)
 
#### Upload to gallery

![Desktop View](documentation/wireframes/)
![Mobile View](documentation/wireframes/gallery-upload.png)
 



## Technologies Used

- Git used for version control.
- [GitHub]() was used for securely storing code.
- [Gitpod](https://gitpod.io/) is the cloud based IDE.
- Python3 is used for the main code logic.
- [Django](https://www.djangoproject.com/) was used as the framework
- PostgreSQL
- [Heroku](https://heroku.com/) was used for live deployment.
- [ShareX](https://getsharex.com/) for capturing screenshots.

## Testing

<!-- To view all testing documentation please refer to [TESTING.md](TESTING.md) -->

### Deployment

The site was deployed using [Heroku](https://heroku.com/). The app can be found using this link - [Myrag](https://myrag.herokuapp.com/).

The steps are as follows:

- Log-in or Sign-up to Heroku.
- From the Dashboard click "New" then "Create New App".
- Enter a project name (unique), select a region then press "Create app".
- This will create an app and open the deploy tab. From here select the "Settings" tab.
- Set your Environment Variables by navigating to Reveal Config Vars.
Scroll up and head to the "Deploy" section to choose deployment method. Select "GitHub" and in the "connect to GitHub" section link your GitHub account.
- Scroll down to the manual deploy option and select "Deploy Branch".
- The app will now be built. Once completed a 'Your App Was Successfully Deployed' message and a link will appear.

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

### Acknowledgements

- Thank you to my mentor for help and support.
