# Clinical Trials at NYC Hospital

## Introduction
The idea of this project was based around the healthcare industry. This is a industry that i currently work in. With the recent COVID-19 pandemic brining the entire world to stand still, healthcare and more imprtantly, clinical research are in the spotlight more than ever before. This website allows users to search through clinical trials, view details about the trial and enroll in it. In order to enroll in a trial, a user mist first register on the website. With some many clinical trials out there, this website dispplays the trials in a nice compact and easy to read format.

## Version Control


## User Experience
The user experience I wanted the user to be able to look and find the information as quickly as possible. The website is easy and straight forward to register and sign up to and I wanted the main content of the website to be accessible to all users and only registered users have the ability to enroll in a study.

## Design

### Icons

    The Icons used are created with the help of the following sites:
    - [fontawesome](https://fontawesome.com/start)
    - [favicon](https://www.favicon.io/) 

## User stories
My goal was to have give the user a simple a straight forward website to find a clinical trial. Alot of hospitals do not put alot of effort into their CT (clinical trial) websites. They usually just post a title of a CT and a few paragraphs about it using alot of medical terms. This can leave the user unsure what the actual disease that is being treated and if they are eligible or not. This website displays the disease and enrollment criteria very clearly for the user to see.

User Stories can be found at https://github.com/users/jcurran1289/projects/2 


* As a **User**, I can easily navigate through the list clinical trials
* As a **User**, I can easily search clinical trials through disease site
* As a **User**, I want to be able to have the same functionalities on different devices (mobile, tablet and PC).
* As a **User**, I want to be able to sign up for an account.
* As a **Registered User**, I can easily login and logout of my account.
* As a **Registered User**, I can easily post questions on the clinical trials page
* As a **Registered User**, I can easily enroll in a study 
* As a **Site Owner/Superuser**, I can create new clinical trials.
* As a **Site Owner/Superuser**, I want to be able to edit and delete clinical trials.
* As a **Site Owner/Superuser**, I want to be able to access the admin section of the site to view questions and delete them.

## Data Models

### Post
This data model is used to store all the relevant information about a listed clinical trial:
| Field            | Data Type       | Purpose                                                | Form Validation                  |
|------------------|-----------------|--------------------------------------------------------|----------------------------------|
| title            | CharField       | Name of clinical trial                                 | required, max length 200, unique |
| slug             | SlugField       | Urls and unique identifier                             | required, max length 200, unique |
| author           | ForeignKey      | User that created the post                             | on_delete                        |
| IRB_number       | CharField       | Institutional Review Board Application Number          | max length 200, default is 101   |
| prin_invest      | CharField       | Principal Investigator of the trial                    | max length 200, default is name  |
| contact_name     | CharField       | Name of person to contact for details about the trial  | max length 400, default is name  |
| contact_email    | CharField       | Email of person to contact for details about the trail | max length 200, default is null  |
| primary_disease  | CharField       | what disease the study is researching                  | max length 5000                  |
| eligible_age_min | IntegerField    | Minimum age to enroll in the trial                     | default is 0                     |
| eligible_age_max | IntegerField    | Maximum age to enroll in the trial                     | default is 100                   |
| gender           | IntegerField    | Emailgender eligibility                                | default is 0                     |
| main_image       | CloudinaryField | To store images                                        |                                  |
| content          | CharField       | The full description of the trial                      | max length 5000                  |
| no_participants  | ManyToManyField | The number of participants enrolled in the trial       |                                  |
| status           | IntegerField    | The current status of the trial                        | default is 0                     |
| start_dt         | DateField       | The date the trial began enrolling                     | default is 2022-09-22            |
| end_dt           | DateField       | The date the trail stops enrolling                     | default is 2022-09-22            |
| created_on       | DateField       | The date the post was created in the database          |                                  |
| updated_on       | DateField       | The date the post was last updated in the database     |                                  |

- [x] Create - Admin can create posts via django administration interface
- [x] Read - Every user can read the stock details in their page 
- [x] Update - Admin can Update stock via django administration
- [x] Delete - Admin can Delete stock via django administration


| Field      | Data Type     | Purpose                                     | Form Validation             |
|------------|---------------|---------------------------------------------|-----------------------------|
| post       | ForeignKey    | One to many relation                        | required but automatic      |
| name       | CharField     | Name of user asking question                | required but automatic      |
| email      | EmailField    | To be stored in database                    | required but automatic      |
| body       | TextField     | To be shown, it is the question being asked | required                    |
| created_on | DateTimeField | To be shown below the question              | required but automatic      |
| approved   | BooleanField  | To let admin approve before publishing      | required, auto is False (*) |

(*) Please notice that in the current version and for better interactivity for the users, not yet approved comments are also shown on the site.

- [x] Create - Every registered and logged in user can ask questions to the study team about the study.
- [x] Read - Every user can read the comments of other users

## Testing
All the HTMl and CSS code works as expected and as well as going through the website manually, I have tested the HTML, CSS and Django code using third party validations such as Pep8 for Django and W3C validationf for HTML and CSS.

## Validation 

## Bugs
See issues in github

## Deploying to Heroku
Go onto Heroku
Login to my account.
Click create new app.
I choose a name for my project and the region that I am in (Eu).
Go to setting.
Click on reveal config vars
Add in CLOUDINARY_URL, DATABASE_URL and your secret_key
Go to resources and search for Postgres, and install the Heroku Postgres
Go to Deploy
Connect to github login.
Search for the project you wish to connect. Once found click the connect button After this I click the deploy button at the bottom.

## Tech used
