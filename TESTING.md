# Testing

To return to readme documentation please click here [README.md](README.md)


## Manual Testing

### User Story Testing

#### View & Navigation

##### Owner
- As an owner I can upload pictures of durags so that I can show off my product.
![Create Durag](documentation/testing/manual/create-durag.png)
![See Gallery](documentation/features/browse-selection.gif)


- As an owner I can see pending orders so that I can deliver to the right address.
![Pending Orders](documentation/testing/manual/pending-orders.png)

##### Admin
- As an admin I can access the backend through login so that I can access data securely.
![Backend](documentation/testing/manual/backend.png)

##### User
- As a user I can see the gallery I so that I know what designs are on offer.
![See Gallery](documentation/features/browse-selection.gif)

- As a user I can see contact information I so that have ways to contact the owner for information.
![Contact Information](documentation/features/footer.png)

- As a user I can see my order history so that I can view my past orders.
![Order History](documentation/features/order-history.png)

- As a user I can see delivery information so that I see its being delivered to the right place.

![Delivery Information](documentation/features/checkout-confirmation.gif)

- As a user I can enter payment information so that I can make a purchase.
![Enter Payment Information](documentation/features/checkout-form.gif)


#### Registration & User Accounts

##### Admin
- As an owner I can create and delete users so that I can perform data maintenance.
![Create Delete Users](documentation/testing/manual/update-users.png)

- As an owner I can update user records  so that I can perform data maintenance.
![Update Users](documentation/testing/manual/update-users.png)

##### User
- As a user I can register an account so that I can sign up to myrag.
![Register Account](documentation/features/registration.png)

- As a user I can create a profile so that I can save my information. 
![Create Profile](documentation/features/default-delivery-information.png)

- As a user I can update profile so that I can make changes to saved information.
![Update Profile](documentation/features/default-delivery-information.png)

- As a user I can sign in and out so that I can securely access saved information.
![Sign In](documentation/features/login.png)
![Sign Out](documentation/features/sign-out.png)

#### Purchasing & Checkout

##### User
- As a user I can save delivery information so that I can fast track checkout.
![Save Delivery Information](documentation/features/checkout-confirmation.gif)

- As a user I can see order confirmation
![See Order Confirmation](documentation/features/checkout-confirmation.gif)




## Code Validation

### HTML

I checked all my templates for html errors using [Nu Html Checker](https://validator.w3.org/). These are the page errors before I proceeded to fix them.

#### Homepage
![home](documentation/testing/html/home.png)

#### Contact
![contact](documentation/testing/html/home.png)

#### Newsletter
![newsletter](documentation/testing/html/newsletter.png)

#### All Durags
![all durags](documentation/testing/html/all-durags.png)

#### Durag Details
![durag details](documentation/testing/html/durag-details.png)

#### Edit Durag
![edit durag](documentation/testing/html/edit-durag.png)

#### Create Durag
![create durag](documentation/testing/html/create-durag.png)

#### Basket
![basket](documentation/testing/html/basket.png)

#### Checkout
![checkout](documentation/testing/html/checkout.png)

#### Checkout Success
![checkout success](documentation/testing/html/checkout-success.png)

#### Profile
![profile](documentation/testing/html/profile.png)

#### Register
![register](documentation/testing/html/register.png)

#### Login
![login](documentation/testing/html/login.png)

#### Logout
![logout](documentation/testing/html/logout.png)


### CSS 

[Jigsaw](https://jigsaw.w3.org/)

I copied and pasted my css into the input section and checked my css. Everything seems to be in order with nothing wrong.

#### Base
![Base](documentation/testing/css/base-css.png)

#### Checkout
![Checkout](documentation/testing/css/checkout-css.png)

#### Home
![Home](documentation/testing/css/home-css.png)

#### Products
![Producs](documentation/testing/css/products-css.png)

#### Profiles
![Profiles](documentation/testing/css/profile-css.png)

### Python

[PEP8](http://pep8online.com/)

My code was copied and pasted into the pep8 checker to see if all of my code was pep8 compliant. I had a few files which exceeded the length required but it was a quick fix. I also used the problems tab in the gitpod ide.


## Browser Compatibility

I have navigated through the site using three main internet browsers, chrome, firefox and edge. I am yes to come across any compatibility issues.

### Chrome

![Chrome](documentation/testing/browser/chrome.png)

### Firefox 

![Firefox](documentation/testing/browser/firefox.png)

### Edge

![Edge](documentation/testing/browser/edge.png)

## Browser Responsiveness

I used chrome developer settings to test the responsiveness of the site on 3 devices with varying sizes. iPhone 5, the iPhone 12 Pro and the Ipad Air.

### iPhone 5SE

![iPhone 5SE](documentation/testing/browser/iPhone-5se.png)

### iPhone 12

![iPhone 12](documentation/testing/browser/iPhone-12pro.png)

### Ipad Air

![Ipad Air](documentation/testing/browser/ipad-air.png)


## Lighthouse

I used the Lighthouse automated tool from Developer Tools to perform site quality tests. The result is shown below.



#### Homepage
![home](documentation/testing/lighthouse/home.png)

#### Contact
![contact](documentation/testing/lighthouse/home.png)

#### Newsletter
![newsletter](documentation/testing/lighthouse/newsletter.png)

#### All Durags
![all durags](documentation/testing/lighthouse/all-durags.png)

#### Durag Details
![durag details](documentation/testing/lighthouse/durag-details.png)

#### Edit Durag
![edit durag](documentation/testing/lighthouse/edit-durag.png)

#### Create Durag
![create durag](documentation/testing/lighthouse/create-durag.png)

#### Basket
![basket](documentation/testing/lighthouse/basket.png)

#### Checkout
![checkout](documentation/testing/lighthouse/checkout.png)

#### Checkout Success
![checkout success](documentation/testing/lighthouse/checkout-success.png)

#### Profile
![profile](documentation/testing/lighthouse/profile.png)

#### Register
![register](documentation/testing/lighthouse/register.png)

#### Login
![login](documentation/testing/lighthouse/login.png)

#### Logout
![logout](documentation/testing/lighthouse/logout.png)

## Bugs


### Fixed Bug

- Users were able to access parts of the site by using the url or back button when logged out.
- Users were redirected to missing success page after login.
- Placeholder image link was broken for durags with no image url.


### Unfixed Bug

- The toast pops up on pages it perhaps should not.