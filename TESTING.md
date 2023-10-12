# Table of Contents

- [Validator Testing](#validator-testing)
  * [HTML](#html)
  * [CSS](#css)
  * [Javascript](#javascript)
  * [Python](#python)
  * [Lighthouse](#lighthouse)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Manual Testing](#manual-testing)

## Validator Testing

### HTML

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). See results in below table.

| Page             	| Logged out 	| Logged in  	|
|------------------	|------------	|------------	|
| Home             	| No errors  	| No errors  	|
| About Us         	| No errors  	| No errors  	|
| Courses          	| No errors  	| No errors  	|
| Groups           	| No errors  	| No errors  	|
| Individual       	| No errors  	| No errors  	|
| Camps            	| No errors  	| No errors  	|
| Course Detail    	| No errors  	| No Errors  	|
| Add a Course     	| N/A        	| No Errors  	|
| Edit a Course    	| N/A        	| No errors  	|
| Delete a Course  	| N/A        	| No errors  	|
| Timetable        	| No errors  	| No errors  	|
| Contact Us       	| No errors  	| No errors  	|
| Contact Success   | No errors   | No errors   |
| Cart             	| No error   	| No errors  	|
| Checkout         	| No errors  	| No errors  	|
| Checkout Success  | N/A       	| No errors  	|
| login            	| No errors  	| N/A        	|
| logout           	| N/A        	| No errors  	|
| signup           	| No errors  	| N/A        	|
| Profile          	| N/A        	| No errors  	|
| Students         	| N/A        	| No errors  	|
| Add a Student    	| N/A        	| No errors  	|
| Edit a Students  	| N/A        	| No errors  	|
| Delete a Student 	| N/A        	| No Errors  	|
| 400              	| No errors  	| No Errors  	|
| 403              	| No errors  	| No Errors  	|
| 404              	| No errors  	| No errors  	|


### CSS
No errors were found when passing my CSS file through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

### Javascript

No errors were found when passing my javascript through [Jshint](https://jshint.com/)

### Python

All Python files were run through [Pep8](https://pep8ci.herokuapp.com/) with no errors found. 


## Lighthouse

| Page             	| Performance 	| Accessibility 	| Best Practises 	| SEO 	|
|------------------	|-------------	|---------------	|----------------	|-----	|
| Home             	| 96          	| 97            	| 83             	| 90  	|
| About Us         	| 95          	| 96            	| 92             	| 100 	|
| Courses          	| 97          	| 98            	| 92             	| 90  	|
| Groups           	| 94          	| 98            	| 92             	| 90  	|
| Individual       	| 97          	| 98            	| 92             	| 90  	|
| Camps            	| 97          	| 98            	| 92             	| 90  	|
| Course Detail    	| 96          	| 90            	| 92             	| 100 	|
| Add a Course     	| 98          	| 96            	| 100            	| 100 	|
| Edit a Course    	| 97          	| 96            	| 92             	| 100 	|
| Delete a Course  	| 97          	| 96            	| 92             	| 100 	|
| Timetable        	| 95          	| 98            	| 83             	| 90  	|
| Contact Us       	| 97          	| 98            	| 92             	| 90  	|
| Contact Success   | 97            | 98              | 100             | 100   |
| Cart             	| 97          	| 83            	| 92             	| 90  	|
| Checkout         	| 90          	| 96            	| 92             	| 100 	|
| Checkout success 	| 97          	| 98            	| 83             	| 100 	|
| login            	| 98          	| 98            	| 92             	| 100 	|
| logout           	| 97          	| 98            	| 92             	| 100 	|
| signup           	| 98          	| 98            	| 92             	| 100 	|
| Profile          	| 99          	| 96            	| 92             	| 100 	|
| Students         	| 97          	| 98            	| 92             	| 100 	|
| Add a Student    	| 98          	| 98            	| 92             	| 100 	|
| Edit a Students  	| 98          	| 96            	| 92             	| 100 	|
| Delete a Student 	| 96          	| 96            	| 92             	| 100 	|


## Manual Testing

### Site Navigation

| Element            	| Action 	| Expected Result                  	| Pass/Fail 	|
|--------------------	|--------	|----------------------------------	|-----------	|
| Logo               	| Click  	| Redirect to home                 	| Pass      	|
| Home               	| Click  	| Redirect to home                 	| Pass      	|
| About Us           	| Click  	| Open About us page               	| Pass      	|
| Courses            	| Click  	| Open dropdown menu               	| Pass      	|
| Group              	| Click  	| Open Group classes page          	| Pass      	|
| Individual         	| Click  	| Open Individual classes page     	| Pass      	|
| Camp               	| Click  	| Open Camp page                   	| Pass      	|
| Timetable          	| Click  	| Open Timetable page              	| Pass      	|
| Contact Us         	| Click  	| Open Contact us page             	| Pass      	|
| Login icon         	| Click  	| Open dropdown menu               	| Pass      	|
| Register           	| Click  	| Open Register page               	| Pass      	|
| Login              	| Click  	| Open Login page                  	| Pass      	|
| Cart icon          	| Click  	| Open cart page                   	| Pass      	|
| Search field       	| Click  	| Allow user to enter search input 	| Pass      	|
| Search icon        	| click  	| Display search results           	| Pass      	|
| All Navbar Links   	| Hoover 	| Text color changes to dark blue  	| Pass      	|
| Navbar active link 	| active 	| Text color changes to dark blue  	| Pass      	|

### Home Page

| Element                	| Action 	| Expected Result               	| Pass/Fail 	|
|------------------------	|--------	|-------------------------------	|-----------	|
| Courses Button         	| Click  	| Open courses page             	| Pass      	|
| Contact us Button      	| Click  	| Redirect to Contact Us page   	| Pass      	|
| Read More - Camps      	| Click  	| Opens Camps page              	| Pass      	|
| Read More - Individual 	| Click  	| Opens Individual Classes page 	| Pass      	|
| Read More - Group      	| Click  	| Opens Groups page             	| Pass      	|
| Carrousel Indicators   	| Click  	| Change to next testimonials   	| Pass      	|

### Footer

| Element            	| Action 	| Expected Result                             	| Pass/Fail 	|
|--------------------	|--------	|---------------------------------------------	|-----------	|
| Facebook icon      	| Click  	| Redirect to Facebook page opens on new tab  	| Pass      	|
| Instagram icon     	| Click  	| Redirect to Instagram page opens on new tab 	| Pass      	|
| Twitter icon       	| Click  	| Redirect to Twitter page opens on new tab   	| Pass      	|
| Private Policy     	| Click  	| Open private Policy in new tab              	| Pass      	|
| Newsletter         	| Click  	| Subscribe user                              	| Pass      	|

### Timetable

| Element   	| Action 	| Expected Result                              	| Pass/Fail 	|
|-----------	|--------	|----------------------------------------------	|-----------	|
| Read More 	| Click  	| Opens course detail page for selected course 	| Pass      	|

### Contact Us

| Element       	| Action 	| Expected Result              	| Pass/Fail 	|
|---------------	|--------	|------------------------------	|-----------	|
| Name field    	| Click  	| Allows User to input name    	| Pass      	|
| Email field   	| Click  	| Allows user to input Email   	| Pass      	|
| Subject Field 	| Click  	| Allows user to input subject 	| Pass      	|
| Message Field 	| Click  	| Allows user to enter message 	| Pass      	|
| Send          	| Click  	|                              	| Pass      	|
| Map           	| Click  	| Allows to move map           	| Pass      	|
| Map +         	|        	| Zooms map in                 	| Pass      	|
| Map -         	|        	| Zooms map out                	| Pass      	|

### Course Detail Page

| Element               	          | Action 	| Expected Result                                                                               	| Pass/Fail 	|
|-----------------------------------|--------	|-----------------------------------------------------------------------------------------------	|-----------	|
| Minus icon/down arrow 	          | Click  	| Decrement course quantity                                                                     	| Pass      	|
| Minus icon/down arrow 	          | Click  	| Wont allow user to select less than 1                                                         	| Pass      	|
| Plus icon/ up arrow   	          | Click  	| Increment course quantity                                                                     	| Pass      	|
| Plus icon/ up arrow   	          | Click  	| Will not allow users to select greater quantity than number of places available for the course 	| Pass      	|
| Quantity box          	          | Click  	| Allows user to enter a number quantity                                                        	| Pass      	|
| Quantity Box          	          | Click  	| Will not allow users to select greater quantity than number of places available for the course  | Pass        |
| Keep shopping         	          | Click  	| Redirects user to courses page                                                                	| Pass      	|
| Add to Cart           	          | Click  	| Adds course/es to the cart                                                                    	| Pass      	|
| Admin logged in - Edit Link      	| Click  	| Redirect to edit course page                                                                    | Pass      	|
| Admin logged in - Delete link    	| Click  	| Delete course                                                                                  	| Pass      	|

###  Add Course Page

| Element                          	| Action 	| Expected Result                                 	| Pass/Fail 	|
|----------------------------------	|--------	|-------------------------------------------------	|-----------	|
| Category field                   	| Click  	| Display dropdown options and allow selection    	| Pass      	|
| Level Field                      	| Click  	| Display dropdown options and allow selection    	| Pass      	|
| Name Field                       	| Click  	| Allow user to input course name                 	| Pass      	|
| Description field                	| Click  	| Allow user to enter course description          	| Pass      	|
| Duration Field                   	| Click  	| Allow user to enter class duration              	| Pass      	|
| Start Date Field                 	| Click  	| Display calendar for date selection             	| Pass      	|
| Start Time field                 	| Click  	| Allow user to enter start time                  	| Pass      	|
| End Date Field                   	| Click  	| Display calendar for date selection             	| Pass      	|
| Day of the Week field            	| Click  	| Display dropdown and allow selection            	| Pass      	|
| Image button                     	| Click  	| Allow selection on an image                     	| Pass      	|
| Image button                     	| Click  	| Default image is used if no image is selectec   	| Pass      	|
| Places Field                     	| Click  	| Enter number of places available for the course 	| Pass      	|
| Cancel Button                    	| Click  	| Returns to courses page                         	| Pass      	|
| Add a Course button (form valid) 	| Click  	| Form submit - create course                     	| Pass      	|

### Profile Page

| Element              	| Action 	| Expected Result                                                   	| Pass/Fail 	|
|----------------------	|--------	|-------------------------------------------------------------------	|-----------	|
| Email Field          	| Click  	| User can enter/save email to profile                              	| Pass      	|
| Phone Field          	| Click  	| User can enter/save phone number to profile                       	| Pass      	|
| Add a Sudent button  	| Click  	| Opens add student form                                            	| Pass      	|
| View students button 	| Click  	| Redirects to students page                                        	| Pass      	|
| Update information   	| Click  	| Updates email and phone fields                                    	| Pass      	|
| Order number link    	| Click  	| Opens order details - checkout success page for that order number 	| Pass      	|

### Students Page

| Element                	| Action 	| Expected Result                 	| Pass/Fail 	|
|------------------------	|--------	|---------------------------------	|-----------	|
| Add Student Button     	| Click  	| Opens add student form page     	| Pass      	|
| Back to Profile Button 	| Click  	| User redirected to Profile page 	| Pass      	|
| Edit link              	| Click  	| Opens edit student form         	| Pass      	|
| Delete link            	| Click  	| Student is deleted              	| Pass      	|

### Add a Student

| Element                    	| Action 	| Expected Result                                                          	| Pass/Fail 	|
|----------------------------	|--------	|--------------------------------------------------------------------------	|-----------	|
| Name Field                 	| Click  	| Allow user to input student name                                         	| Pass      	|
| Surname Field              	| Click  	| Allow user to input student surname                                      	| Pass      	|
| Date of Birth Field        	| Click  	| Display calendar for birthdate selection                                 	| Pass      	|
| Date of Birth Field        	| Click  	| Year displayed on calendar limited by Function: min 3 years old - max 14 	| Pass      	|
| Gender Field               	| Click  	| Display dropdown options and allow selection                             	| Pass      	|
| Level Field                	| Click  	| Display dropdown options and allow selection                             	| Pass      	|
| Special requirements field 	| Click  	| Text field to enter special requirements if any.                         	| Pass      	|
| Add Student to my profile  	| Click  	| Form Submit - Create student on profile                                  	| Pass      	|
| Cancel                     	| Click  	| Returns user to profile page                                             	| Pass      	|

###  Edit Course/Student Pages

| Element       	| Action 	| Expected Result                 	| Pass/Fail 	|
|---------------	|--------	|---------------------------------	|-----------	|
| Update Button 	| Click  	| Course is updated               	| Pass      	|
| Update Button 	| Click  	| Student is updated               	| Pass      	|
| Cancel Button 	| Click  	| User redirected to courses page 	| Pass      	|
| Cancel Button 	| Click  	| User redirected to Profile page 	| Pass      	|

###  Delete Course/ Student Pages

| Element       	| Action 	| Expected Result                 	| Pass/Fail 	|
|---------------	|--------	|---------------------------------	|-----------	|
| Delete Button 	| Click  	| Course is deleted               	| Pass      	|
| Delete Button 	| Click  	| Student is deleted               	| Pass      	|
| Cancel Button 	| Click  	| User redirected to courses page 	| Pass      	|
| Cancel Button 	| Click  	| User redirected to Students page 	| Pass      	|


### Cart

| Element               	| Action 	| Expected Result                                                 	| Pass/Fail 	|
|-----------------------	|--------	|-----------------------------------------------------------------	|-----------	|
| Minus icon/down arrow 	| Click  	| Decrement course quantity                                       	| Pass      	|
| Minus icon/down arrow 	| Click  	| Wont allow user to select  quantity less than 1                 	| Pass      	|
| Plus icon/up arrow    	| Click  	| Increment course quantity                                       	| Pass      	|
| Plus icon/up arrow    	| Click  	| User cannot select quantity over the number of places available 	| Pass      	|
| Quantity Box          	| Click  	| Allows user to enter quantity in numbers                        	| Pass      	|
| Quanity Box           	| Click  	| User cannot select quantity over the number of places available 	| Pass      	|
| Update Link           	| Click  	| Updates the quantity and total of cart                          	| Pass      	|
| Remove Link           	| Click  	| Removes course from cart                                        	| Pass      	|
| Keep Shopping Button  	| Click  	| Redirect user to Courses page                                   	| Pass      	|
| Secure Checkout       	| Click  	| Redirect user to checkout page                                  	| Pass      	|

### Checkout

| Element                                	| Action 	| Expected Result                                                                          	| Pass/Fail 	|
|----------------------------------------	|--------	|------------------------------------------------------------------------------------------	|-----------	|
|                                        	| Click  	|                                                                                          	| Pass      	|
| Link- Create an Account                	| Click  	| Redirect to Login page                                                                   	| Pass      	|
| Link - login                           	| Click  	| Redirect to Sign up form                                                                 	| Pass      	|
| Student Select box                     	| Click  	| Display dropdown with students on the profile to allow student selection                 	| Pass      	|
| Link to create Student - not logged in 	| Click  	| Redirect to login page                                                                   	| Pass      	|
| Link to create student - logged in     	|        	| Redirect to student's page                                                               	| Pass         	|
| Full name field                        	| Click  	| Allow user to input full name                                                            	| Pass      	|
| Email field                            	| Click  	| Allow user to input Email                                                                	| Pass      	|
| Email field                            	| Click  	| If email is saved on profile will be displayed on the form                               	| Pass      	|
| Phone number field                     	| Click  	| Allow user to input phone number                                                         	| Pass      	|
| Phone number field                     	| Click  	| If phone i saved on profile will be displayed on the form                                	| Pass      	|
| Postal code field                      	| Click  	| Allow user to input eircode                                                              	| Pass      	|
| Payment - Stripe                       	| Click  	| Allow user to input card details                                                         	| Pass      	|
| Adjust cart button                     	| Click  	| Redirect user to cart page                                                               	| Pass      	|
| Complete order button - disable       	| Click  	| Button disable until user selects student                                                	| Pass      	|
| Complete order button                  	| Click  	| Submit order and complete purchase - user redirected to order details (checkout success) 	| Pass      	|


### Django All Auth Pages

| Element            	          | Action                               	| Expected Result                                            	| Pass/Fail 	|
|-------------------------------|--------------------------------------	|------------------------------------------------------------	|-----------	|
| SIGN UP                     	|                                      	|                                                            	|           	|
| Email field                 	| Leave empty                          	| Form won't submit                                          	| Pass      	|
| Email field        	          | Insert incorrect format              	| Error message displays                                     	| Pass      	|
| Email field        	          | Insert correct format                	| On submit: Form submit                                     	| Pass      	|
| Email confirmation 	          | Insert incorrect format              	| Form won't submit                                          	| Pass      	|
| Email confirmation 	          | Insert incorrect format              	| On Submit: Form submit                                     	| Pass        |
| Email confirmation 	          | Insert duplicate mail                	| On submit: Form Submit                                     	| Pass      	|
| User name Field    	          | Insert correct format                	| On Submit: Form Submit                                     	| Pass      	|
| User name field    	          | Insert incorrect format              	| Error message displays                                     	| Pass        |
| Password field     	          | Insert incorrect format              	| Form won't submit                                          	| Pass      	|
| Password field     	          | Insert incorrect format              	| Error message displays                                     	| Pass      	|
| Password field     	          | Password doesn't match               	| Form won't submit                                          	| Pass      	|
| Password field     	          | Password doesnt match                	| Error message displays                                     	| Pass      	|
| Password field     	          | Insert correct format and match      	| On submit: form submit                                     	| Pass      	|
| Sign up ( form valid)   	    | Click                                	| Form Submit                                                	| Pass      	|
| Sign up (form valid)          | Click                                	| Message to confirm sign up                                 	| Pass      	|
| Sign up (form valid)          | Click                                	| Success message alerts user to check email for validation  	| Pass      	|
| LOGIN
| User name Field 	            | Leave empty             	            | Form won't submit                                          	| Pass      	|
| User name Field 	            | Insert wrong username   	            | Form won't Submit                                          	| Pass      	|
| User name field 	            | Insert wrong username   	            | Error message displays                                     	| Pass          	|
| Password field  	            | Leave empty             	            | Form won't submit                                          	| Pass      	|
| Password field  	            | Leave empty             	            | Error message displays                                     	| Pass      	|
| Password field  	            | Insert wrong password   	            | Form won't submit                                          	| Pass      	|
| Password field  	            | Insert wrong password   	            | Error message displays                                     	| Pass      	|
| Login button (form valid)   	| Click                   	            | Form Submit                                                	| Pass      	|
| Login button  (form valid)  	| Click                   	            | Redirect to home page                                      	| Pass      	|
| Login button  (form valid)    | Click                   	            | Success message confirming login                           	| Pass      	|
| LOG OUT                                                                                                                                           |
| Logout button  	              | Click                 	              | Redirect to home page                                      	| Pass      	|
| Logout button              	  | Click                      	          | Success message confirming logout appears                  	| Pass      	|

## Trouble shooting

- **Bug**: After implementing the ability to select a student for a course on the checkout app, I encountered an issue. When a user tried to purchase more than one of the same course, they could only select one student for all of those courses.  
- **Fix**: To address this issue, I made modifications in the checkout.html template. I added an if statement inside the for loop responsible for checking items in the cart. Now, if the item quantity is greater than one, an additional for loop is introduced to separate the course quantities into individual lines. This allows the user to select a student for each course they intend to purchase.

- **Bug**: When adding a student in the form, I noticed that it was possible to select a future date of birth, which should not be allow for the purpose of this app.
- **Fix**: To address this issue, I implemented a function that restricts the range of selectable years on the calendar. The minimum age allowed is 3 years, and the maximum age is 14, ensuring that the selected date of birth falls within this range.

- **Bug**: Initially, during the development of the checkout app, users could make purchases without being logged in. This posed a challenge in terms of tracking users and students.
- **Fix**: To rectify this, I have now restricted the checkout process to only logged-in users. Furthermore, in order to complete the checkout, a user must both log in and have at least one student associated with their profile. This ensures that the selected course on the checkout is correctly assigned to a specific student, enhancing tracking and organization. 

- **Bug**:   During the development of the purchasing app, it was functional, but there was no tracking of the quantity purchased for each course. Given that these courses have limited spots due to safety and student-teacher ratio guidelines, it was essential to find a way to limit the quantity and decrease availability with each purchase.
- **Fix**: To address this, I incorporated a variable into the checkout function to monitor the remaining available spots after order confirmation and subsequently decrease the availability accordingly. This ensures that the course's availability is accurately managed as each user makes a purchase.


## Unfixed bugs

- **Bug**: The course availability doesn't update until the order is completed, which may lead to overbooking.
- **Fix**: To address this issue, one potential solution is to explore a queuing system that would allow for real-time updates of course availability. However, due to time constraints and the fact that this is beyond the scope of the current project, this issue remains unresolved for now.

- **Bug**: Presently, it's possible to select the same student for multiple courses in the checkout, which can lead to inaccuracies.
- **Fix**: To address this, a function that ensures once a student has been assigned to a course, they cannot be selected again for another course during the same checkout process should be implemented. This would prevent any unintended duplication and maintain accurate student-course associations.  