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

| Page             	| Logged out      	| Logged in  	|
|------------------	|-----------------	|------------	|
| Home             	| No errors       	| No errors  	|
| About Us         	| No errors       	| No errors  	|
| Courses          	| No errors       	| No errors  	|
| Groups           	| No errors       	| No errors  	|
| Individual       	| No errors       	| No errors  	|
| Camps            	| No errors       	| No errors  	|
| Course Detail    	| No errors       	| No Errors  	|
| Add a Course     	| N/A             	| No Errors  	|
| Edit a Course    	| N/A             	| No errors  	|
| Delete a Course  	| N/A             	| No errors  	|
| Timetable        	| No errors       	| No errors  	|
| Contact Us       	| No errors       	| No errors  	|
| Cart             	| img error       	|            	|
| Checkout         	| error for label 	|            	|
| login            	| No errors       	| N/A        	|
| logout           	| N/A             	| No errors  	|
| signup           	| No errors       	| N/A        	|
| Profile          	| N/A             	| No errors  	|
| Students         	| N/A             	|            	|
| Add a Student    	| N/A             	| No errors  	|
| Edit a Students  	| N/A             	| No errors  	|
| Delete a Student 	| N/A             	| No Errors  	|
| 400              	|                 	|            	|
| 403              	|                 	|            	|
| 404              	| No errors       	|            	|

Duplicate attribute class: As this attribute in within a for loop is multiplied with each student added on the table

### CSS
No errors were found when passing my CSS file through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

### Javascript

No errors were found when passing my javascript through [Jshint](https://jshint.com/)

### Python

All Python files were run through [Pep8](https://pep8ci.herokuapp.com/) with no errors found. 

Webhook
 Map webhook events to relevant handler functions
 46: E501 line too long (86 > 79 characters)

## Lighthouse