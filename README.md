# Aqua Kids 

The live link here - [https://aqua-kids-c98054224c90.herokuapp.com/]

![AquaKids]()

## Table of contents
- [Aqua Kids](#aqua-kids)
 * [User Experience (UX)](#user-experience-ux)
    + [User Stories](#user-stories)
    + [Design](#design)
      - [Colour Scheme](#colour-scheme)
      - [Imagery](#imagery)
      - [Fonts](#fonts)
      - [Wireframes](#wireframes)
  * [Agile Methodology](#agile-methodology)
  * [E-commerce Data Model](#data-model)
  * [Web Marketing Strategies](web-marketing-strategies)
    + [Search Engine Optimization(SEO)](search-engine-optimization)
      - [Key words](key-words)
      - [Social Media Marketing](social-media-marketing)
      - [Email Marketing](email-marketing)
  * [Testing](#testing)
  * [Security Features and Defensive Design](#security-features-and-defensive-design)
    + [User Authentication](#user-authentication)
    + [Form Validation](#form-validation)
    + [Database Security](#database-security)
    + [Custom error pages:](#custom-error-pages-)
  * [Features](#features)
    + [Header](#header)
    + [Footer](#footer)
    + [Home Page](#home-page)
    + [About us](#about-us-page)
    + [Courses](#coures)
    + [Course Categories](#course-categories)
    + [Course Detail](#course-detail)
    + [Cart](#cart)
    + [Checkout](#checkout)
    + [Add a Course](#add-course)
    + [Edit a Course](#edit-course)
    + [Delete a Course](#delete-course)
    + [Timetable](#timetable)
    + [Contact Us](#contact-us)
* [User Account Pages](#user-account-pages)
    + [Profile](#my-books)
    + [Students](#students)
    + [Add a Student](#add-student)
    + [Edit a Student](#edit-student)
    + [Delete a Student](#delete-student)
    + [Pending Features](#future-features)
  * [Deployment - Heroku](#deployment---heroku)
  * [Cloning this repository](#cloning-this-repository)
  * [Languages](#languages)
  * [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  * [Credits](#credits)
  * [Acknowledgments](#acknowledgments)

# Aqua Kids

Aqua Kids is a swim school app designed exclusively for families seeking swimming classes for their children. With a dynamic platform caters to swimmers of all abilities, offering a comprehensive range of programs, including: Groups Classes, Individual Classes and Summer Camps. Aqua Kids lets users browse course descriptions and find suitable time slots for direct booking. The real-time course timetable shows the available spots.

## User Experience (UX)

A visitor to Aqua Kids is typically an enthusiastic parent or guardian, eager to provide their child with a safe and enjoyable swimming experience. They seek a supportive community where their child can learn, make friends, and develop strong swimming skills.

### User Stories

#### Viewing and Navigation

- As a user I want to view a list of swimming lessons so that I can select the course I am interested in.
- As a User I want to view individual course details so that I can identify the course, time, price, start and end date.
- As a User I want to view the timetable of course so that I can Identify the time and date that would suit me.


#### Registration and User Accounts

- As a User I want to easily Register an account so that I can have a personal account to view my profile.
- As a User I want to easily Log in and out of the account so that I can have access to my account when needed.
- As a User I want to be able to recover my password in case of forgetting it so that I can access my account.
- As a User I want to receive an email confirmation on account registration so that I can verify that my account registration was successful.
- As a User I want to personalize my user profile so that I can **view my purchase history, and save my contact details, my dependant details and payment details **.


#### Sorting and Searching

- As a User I want to sort the list of available courses so that I can easily identify all the courses available by type and level.
- As a User I want to Search for a course type so that I can select a specific type of course.
- As a User I want to search for a course level so that I can select a specific level for the course.
- As a User I want to easily see the course I was searching for and the number of results so that I can verify if the course I want is available.

#### Purchasing and Checkout

- As a User I want to easily select the course I want to purchase so that I can so I make sure I don't select the wrong course.
- As a User I want to view the course to purchase in my cart so that I can verify the information on the course I have selected.
- As a User I want to view my order confirmation so that I can verify all details are correct.
- As a User I want to receive an email confirming the purchase so that I can keep a record of my purchased course.
- As a User, I want to see the course availability so I can know if there are places left on the course I want to purchase.

#### Admin Site Management

- As an Admin I want to be able to add a course so that I can have new courses in the store.
- As an Admin I want to Edit/update a course so that I can change course details such as time, price, availability, and other course criteria.
- As an Admin I want to delete a course so that I can remove courses that are no longer available.

#### User stories for future implementation

The following user stories were left out of the project due to time constraints and labelled as "Won't Have" on the project board on GitHub. It is intended for these user stories to be implemented at a later date. 

- As a User I want to view the attendance to the purchased course so that I can know if I need to request make-up classes.

## Design


### Colour Scheme
Colour palette from Colormind

![colormind](https://res.cloudinary.com/dne60wscn/image/upload/v1696436010/AquaKids/Aqua%20Kids%20README/colormind3_d8zuwg.png)

Aqua Kids' website embodies an elegant and minimalist design, artfully blending various shades of blue against a pristine white backdrop. This carefully curated color scheme mirrors the tranquil allure of water, extending a warm invitation to users as they navigate the site and explore our course offerings. The goal is to maintain this unified color palette throughout the website, fostering a seamless and calming visual experience.

#### Imagery

Most of the images are taken from Pexels and Pixabay, and handled by Cloudinary. 

#### Fonts

Montserrat  imported via Google Fonts is the main font used for the website.  Sans Serif is the fallback font.

#### Wireframe

The project began as a wireframe in Balsamiq, serving as the initial foundation from which it evolved. This initial wireframe provided a starting point, allowing for a visual representation of the project's structure and layout.

![wireframe](https://res.cloudinary.com/dne60wscn/image/upload/v1696436015/AquaKids/Aqua%20Kids%20README/wireframehomepng_p5ggoi.png)
![wireframe](https://res.cloudinary.com/dne60wscn/image/upload/v1696436015/AquaKids/Aqua%20Kids%20README/wireframecourses_cypunr.png)
![wireframe](https://res.cloudinary.com/dne60wscn/image/upload/v1696436016/AquaKids/Aqua%20Kids%20README/wireframetimetable_ongf1w.png)
![wireframe](https://res.cloudinary.com/dne60wscn/image/upload/v1696436015/AquaKids/Aqua%20Kids%20README/wireframecontact_silyba.png)


## Agile Methodology 

GitHub projects were used to manage the development process using an agile approach. Please see a link to the project board [here](https://github.com/users/Ygallo/projects/4/views/1)

## E-commerce Data Model

In the inclusion of an e-commerce business model for the Aqua kids project , the primary focus aligns with B2C (Business-to-Consumer), where the aim is  to directly engage with parents and guardians seeking swimming lessons for their children. To achieve this, the  marketing strategies revolve around building trust with the target audience.

As an initial step to gauge the platform's viability, a Facebook page and a newsletter campaign was  incorporated into the project.While at this stage, the focus remains B2C, in the future an option to expand to B2B can be explored , such as partnerships with schools or community centres. 

Throughout the project, I applied the principles of Object-Oriented Programming (OOP). 

Django AllAuth was used for the user authentication system.


The **Category** entity categorises our classes into three distinct types: group classes, individual classes, and camps

The **Level** entity defines swim skill levels and their target audience within the school. 

The **Course** entity encompasses all swim school courses, each uniquely identified by an ID. It includes start date, start time, end date, day of the week, price, available places, and an associated image. The **Level** and **Category** are linked to the course through Foreign Keys.

**User** entity represents the registered users of the website, who can buy courses for their dependants. Each user has a unique ID, name, email, and password.

The **Student** entity represents minor participants in swimming classes. Each student is uniquely identified by an ID and includes basic details such as name, surname, date of birth, gender, and any special requirements. The student's swim skill **level** is stored as a Foreign Key, and the guardian's information is linked through the **User** model.

The **Order** model will handle all orders in the swim school. It includes fields for order number, user details (full name, email, phone number, eircode), date, order total, and grand total. The user profile is linked to the order via a foreign key.

The **OrderLineItem** model represents items within a shopping cart associated with a specific **order**. It references the **course**, quantity, and total cost for each line item. It also includes a foreign key to the order with a related name of 'line items'.


The diagram below details the database schema.

![datamodel](https://res.cloudinary.com/dne60wscn/image/upload/v1696752609/AquaKids/Aqua%20Kids%20README/DiagramDataBase_plxqg3.png)

## Testing

Testing and results can be found [here](https://github.com/Ygallo/aqua-kids/blob/main/TESTING.md)

## Security Features and Defensive Design

### User Authentication

The **login_required ** decorator is used to grant access to the profile page only to authenticated users. Non-authenticated users are automatically redirected to the login page. Additionally, exclusive access to create, edit, and delete courses is reserved for Admin users. Non-authorized users attempting to access these functionalities are redirected and presented with a corresponding access message. 

Only logged in User can create, edit, and delete a student in their profile.

### Database Security

To enhance security, I implemented specific measures in the project. Firstly, I ensured that sensitive information like the database URL and secret key was stored in the env.py file and that the env.py file is included in my gitignore file. By keeping these details separate and preventing them from being pushed to Github during the initial setup, I minimise the risk of unauthorised access or unwanted connections to the database.

Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site.

### Custom error pages:

Custom error pages were meticulously designed and implemented to provide users with comprehensive information when encountering errors and to guide them seamlessly back to the site. 

![error]()

- 400 Bad Request - We hit a little snag and are unable to handle this request.
- 403 Access Denied - Oops! It looks like you don't have permission to access this page.
- 404 Page Not Found - You've landed in the middle of the water. Hold on tight and we will take you back to safety.

## Web Marketing Strategies

### Search Engine Optimization(SEO)

#### Key words

![wordtraker](https://res.cloudinary.com/dne60wscn/image/upload/v1696436109/AquaKids/Aqua%20Kids%20README/wordtraker-learn-to-swim_jxdzfo.png)
![wordtraker](https://res.cloudinary.com/dne60wscn/image/upload/v1696436106/AquaKids/Aqua%20Kids%20README/wordtracker-swimming-school_pcd0kh.png)

At the project's outset, keyword research was conducted to identify crucial terms for my web app. Following this process, a set of both short and long-tail keywords was selected.

| Short-Tail                	| Long-Tail                             	|
|---------------------------	|---------------------------------------	|
| Swim class                	| Child-friendly swimming lessons        	|
| Kids swimming lessons     	| Indoor swimming lessons for kids      	|
| Learn to swim             	| Private swimming lessons for children 	|
| Swimming classes for kids 	| Summer swim camps for kids            	|
| Swimming skills           	| Top-rated swim instructors             	|
| Life skill                	|                                       	|
| Water safety for kids     	|                                       	|
| Indoor Swim               	|                                       	|
| Swimming school           	|                                       	|


#### Other SEO implementation, included
- A robots.txt file: created in the root directory of the project.
- A sitemap.xml file, generated at https://www.xml-sitemaps.com/ 
- Descriptive meta tags
- Descriptive Image descriptions  and image file name
- rel attributes on links to external resources

### Social Media Marketing

A Facebook Page was created to establish an online presence for the small budget, family-oriented business. This is the initial step to gauge the platform's popularity.

![Facebook](https://res.cloudinary.com/dne60wscn/image/upload/v1696753122/AquaKids/Aqua%20Kids%20README/Facebookpng_qcoxdc.png)
![Facebook](https://res.cloudinary.com/dne60wscn/image/upload/v1696752609/AquaKids/Aqua%20Kids%20README/Facebook_post_zlgohq.png)

### Email Marketing

We've implemented a newsletter signup form for its ease of setup and cost-effectiveness. It enables the swim school to reach interested subscribers and can effortlessly accommodate audience growth. Aqua Kids can design email content to share the latest news with its community.

## Features

## Header
- The school's logo is on the left of the navigation bar, with the search field in the middle, and two Font Awesome icons on the right: one for the user account and one for the cart.
- The header is present in all the pages and links back to the homepage.
- The Account navigation link is a drop down menu which includes the Sign up and Login links. 
- The navigation bar has a royal blue background with white text. It contains links to About Us, Courses (with a dropdown menu), Timetable, and Contact Us.
- The Account navigation link has a dropdown menu which includes the Sign up and Login links. 
- When an Admin user logs in, the Account dropdown menu displays the option 
'School Management.'
When a user logs in, the Account dropdown menu displays the option Profile, Students and Logout.
- The navigation bar is fully responsive, collapsing into a hamburger menu when the screen size becomes too small.
- The active navbar tab changes colour from white to dark blue.

![header]()


### Footer

- The footer section includes links to Facebook, Instagram and Twitter.
- Clicking the links in the footer opens a separate browser tab to avoid pulling the user away from the site.
- Below the social accounts there is a link to the privacy policy.
- On the opposite side you can find the newsletter signup form from Mail Chimp.

![footer]()

## Home Page

The homepage showcases a hero image with swim school information.
There's a section with images and descriptions for the three course categories. 
At the bottom of the page there is a carousel displaying customer pictures and testimonials. 

##About Us

The 'About Us' section highlights why users should choose the swim school for their kids, including the coaching philosophy and coach information.

## Courses

The course page shows the course image, name, and details about the intended audience, skills taught, and duration

At the bottom of the page there is a carousel displaying customer pictures and testimonials. 

## Course Categories

The courses dropdown on the navigation bar lets users select the course category: Group, Individual, or Camps.
When a category is selected, the page displays cards with available courses for that category.
Each card includes an image for the course level, a description of the intended audience, skills taught, and duration. 
The price and available places are displayed, along with a 'Read more' button that directs the user to the course detail page. 

## Course Detail

- The course detail section displays all the information for each available course. It includes course name, description, start date, start time, day of the week, price, available places, and image. 
-  Available places are represented by rounded pills: green (Bootstrap success) for more than 4 places, yellow (Bootstrap warning) for fewer than 4 places, and red (Bootstrap danger) with 'full' for no available places.
- "There's an input field for quantity, accompanied by Font Awesome icons for increasing and decreasing the quantity. A logic function prevents users from purchasing more than the available amount and less than one."
- The user can click on the Add to cart button or keep shopping button to browse more courses.

## Cart

- The cart page displays the courses the user intends to purchase.
- The course image, name, quantity and price are shown for each item.
- The user can adjust the quantity, and the price updates accordingly.
- The + and - icons, along with the quantity input, prevent the user from decreasing the quantity to 0 or exceeding the available places in the course.
- At the bottom of the page, there are two buttons: one to 'Keep Shopping' and redirect to the courses page, and the other to complete the purchase by clicking 'SECURE CHECKOUT

 
## Checkout

- The checkout page includes an order summary with the course name, quantity, a student selection dropdown, and the course price. 
- If the user has students in their profile, the selection box displays the student's name(s) for the user to choose. The purchase button remains disabled until a student is selected.
- If there are no students in the user's profile, they will be prompted to add a student before proceeding with the purchase.
- Opposite the summary, there's a form to complete the purchase. The user fills in fields for name, contact details, and card details.
After completing the order, the user can view the order confirmation.


### Checkout success

The order confirmation page displays information, including the order number, date, contact details, course details (including the students enrolled), and the grand total.  

## Add a Course Form

- The "Add a Course" functionality on a swim school website allows authorised administrators or staff members to create and publish new swimming courses. It's a crucial feature that enables the swim school to manage and expand its course offerings efficiently.
- The form will be displayed with the required fields for the category, level, name, start date, start time, end date, day of the week, price, available places, and an associated image. Failing to complete required fields will render an error message.
- Category, level, and days of the week fields offer dropdown menus with various options.
- The image field includes a default image for cases where the user doesn't upload one.

## Edit a Course

-  Only a logged-in Admin user can choose to edit a course. This is done by clicking the edit button on the course and course detail pages.
- If an unauthorised user tries to edit a course (by changing the URL) a message alerts them that only Admin users are allowed.
- The form opens with all fields populated with the original content.


## Delete a Course

- Only logged-in Admin users can delete a course.The deletion is done by clicking the delete button on the course or course detail pages. 
- The user is asked to confirm if they wish to delete the course or cancel.
- A message informs the user "The course was deleted successfully. 

## Timetable

- This section features a table listing all available class types and their respective times for the user.
- Each table row displays the course image, level, category, availability, day of the week, startime. 
- In the Action column, you'll find a Read More link to access the detailed page for each specific course.
- A 'for' loop ensures that each newly created course is automatically added to the timetable.
- In the availability row, an 'if' statement evaluates the availability of places. If many places are available, a rounded green pill (Bootstrap success) displays the available quantity. If there are fewer than 4 places, a yellow pill (Bootstrap warning) is shown. If no places are left, a red pill (Bootstrap danger) displays 'full'." 

## Contact Us

- This page will allow the user to get in contact with Aqua Kids. The user will be asked to submit their full name and email address, subject and message.
- To the right of the contact form, a grid column displays contact details using three Font Awesome icons for address, phone, and email, along with their corresponding information.
- Below the contact form, there's a Google Map of Dublin.

## User Account Pages

**Sign Up**
 ![signup]()

**Log In**

![login]()

**Log Out**

![signout]()

- The Signup, Login, and Log out functionality was implemented using Django allauth. This authentication package was integrated into the project, enabling seamless user registration, login, and logout processes.

- To enhance the user experience, success messages were incorporated to provide immediate feedback when users successfully log in or log out.

## Profile page

- The profile page displays the user/guardian contact details and the order  history. 
- There is a button to update the user’s email and phone number.
Two buttons redirect users to 'Add a Student' or 'View Students' pages.
 
## Students Page

- A table displays associated students, if any, on the profile.
- The rows displays student name, surname, date of Birth, Gender, level and an Action button. 
- The actions links for Edit and Delete, redirect to the corresponding pages. 

## Add a Student
- Displays a form that allows the user to add the students (dependents) that will be taking the courses. 
- The form  includes basic details such as name, surname, date of birth, gender, the student's swim skill **level** and any special requirements. 
- Upon completion of the form the user has the option to cancel or add the student to its profile. 

## Edit a Student

- Only logged-in users can edit a student that they have stored in their profile. 
- The form opens with all fields populated with the original content.
- A button allows for updating student information. Clicking it updates the student and redirects the user to the students' page. 
- There is a button to Cancel the action and return the user to the profile Page. 

## Delete a Student

- Only logged-in users can delete a student on. The deletion is done by clicking the delete button on . 
- The user is asked to confirm if they wish to delete the course or cancel.
- A message informs the user "The course was deleted successfully". 
- User is redirected to the students page. 


### Pending Features

## Deployment - Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Create the Heroku App:

- Logged in to [Heroku](https://dashboard.heroku.com/apps).
- On the main page clicked the button labeled **New** in the top right corner and from the drop-down menu select **"Create New App"**.
- Entered the chosen app name.
- Next select the region.
- Clicked on the **Create App** button.

### Attach the Postgres database:

- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.

### Prepare the environment and settings.py file:

- In my GitPod workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save files and make migrations.
- Add Cloudinary URL to env.py
- Add the cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR
- Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

### Create files / directories

- Create requirements.txt file
- Create  directories in the main directory for static and templates.
- Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi

### Update Heroku Config Vars

Add the following Config Vars in Heroku:
- SECRET_KEY value 
- CLOUDINARY_URL
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1

### Deploy

- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and clicked Enable Automatic Deploys. Every push to main will deploy a new version of this app. Deploys happen automatically.

The site is now live and operational.

## Languages

- Python
- HTML
- CSS
- Javascript

## Frameworks - Libraries - Programs Used
- [Django](https://www.djangoproject.com/)
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Logo](https://logo.com/)- to create the Logo for the website
- [PostgreSQL](https://www.postgresql.org/)
- [Heroku](https://dashboard.heroku.com/login)
- [Responsive](https://ui.dev/amiresponsive) - Used to verify responsiveness of website on different devices.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
- [Font Awesome](https://fontawesome.com/) 
- [GitHub](https://github.com/) - Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/)
- [W3C](https://www.w3.org/) 
- [PEP8 Online](http://pep8online.com/) 
- [Jshint](https://jshint.com/)
- [Colormind](http://colormind.io/bootstrap/)
- [Favicon](https://favicon.io/)
- [Lucidchart](https://lucid.app/documents#/dashboard) - to create the database design
- [Grammerly](https://app.grammarly.com/) - for proof reading the README.md
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) 
- [Cloudinary](https://cloudinary.com/): for hosting the uploaded images.
- [Bootstrap 4.6](https://getbootstrap.com/)
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables): Used to convert excel testing tables to markdown
- [jQuery- hidden value](https://stackoverflow.com/questions/2979772/set-value-of-hidden-field-in-a-form-using-jquerys-val-doesnt-work)
- [Date Input Widget](https://www.letscodemore.com/blog/how-to-add-date-input-widget-in-django-forms/#:~:text=In%20this%20case%2C%20we%20are,is%20rendered%20in%20the%20template.)

## Credits

- [W3Schools](https://www.w3schools.com/)
- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Stack Overflow](https://stackoverflow.com/)
- [Pexels](https://www.pexels.com/): All imagery on the site was sourced from Pexels.com
- [Pixabay](https://pixabay.com/): for more images.
- [Update View](https://pytutorial.com/django-updateview-example)
- [@login required](https://docs.djangoproject.com/en/4.2/topics/auth/default/)
- [Code Institute - Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1)
- [Page Turner Book Club](https://page-turner-bookclub.herokuapp.com/mybooks/)
- [Red Frog](http://www.redfrog.ie/)- Swim school website
- [Splashtastic](https://splashtastic.ie/) - Swim school website
- [iswim](https://iswim.ie/)
- [Products list page](https://bbbootstrap.com/snippets/bootstrap-ecommerce-category-product-list-page-93685579)

## Acknowledgments