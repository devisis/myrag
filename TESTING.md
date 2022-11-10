# Testing

To return to readme documentation please click here [README.md](README.md)


## Manual Testing

### User Story Testing
combination of readme bullet points with features screenshots


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
![create durag](documentation/testing/html/edit-durag.png)

#### Basket
![basket](documentation/testing/html/basket.png)

#### Checkout
![checkout](documentation/testing/html/checkout.png)

#### Checkout Success
![chekout success](documentation/testing/html/checkout-success.png)

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

![Jigaw validation](documentation/testing/jigsaw_validation.png)

### Python

[PEP8](http://pep8online.com/)

My code was copied and pasted into the pep8 checker to see if all of my code was pep8 complient. I had a few files which exceeded the length required but it was a quick fix.

## Browser Compatibility

I have navigated through the site using three main internet browsers, chrome, firefox and edge. I am yes to come across any compatibility issues.

### Chrome

![Chrome](documentation/testing/chrome.png)

### Firefox 

![Firefox](documentation/testing/firefox.png)

### Edge

![Edge](documentation/testing/edge.png)

## Browser Responsiveness

I used chrome developer settings to test the responsiveness of the site on 3 devices with varying sizes. Iphone 5, the Iphone12 and the Ipad Air.

### Iphone 5SE

![Iphone 5SE](documentation/testing/iphone_5se.png)

### Iphone 12

![Iphone 12](documentation/testing/iphone_12.png)

### Ipad Air

![Ipad Air](documentation/testing/ipad_air.png)


## Lighthouse

## Bugs


### Fixed Bug

- Users were able to access parts of the site by using the url or back button when logged out.
- Users were able to make a reservation for a past date.
- Users were able to make a reservation for 0 seats.
- Users were able to view, update and delete reservations made by all users.

### Unfixed Bug

- Users are able to book for any time they want.
- According to a test user the date-time function was buggy, as it was fine on my iOS it seems to be an Android issue.
    - ![Test user booking bug](documentation/testing/test_user_booking.jpg)