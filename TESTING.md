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

### Checkout