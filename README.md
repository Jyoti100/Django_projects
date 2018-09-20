# Django_projects

# Overview
  The uploded projects are helpful to the beginners of Django framework.
  
 # Requirements
    1. Virtual Environments
    2. Django 2.1
    3. Python 3.7.0
    4. SQLITE3
    
 # Technologies used
    1.Python
    2.Html
    3.CSS
    4.BootStrap
    
    
  # Project Details
  1. UrlMapping->UrlMapPrj
      This Project describes how Url Mapping done in Django and Navigation from one webpage to another.
      
  2. UrlMapping->SlugUrl
      This project describes how to use Slug Url(Human readable Url) in Django.
      
  3. UrlMapping->Polls & PollsMaster
      This project vote for correct answers to your question.
      
  4. Practice -> OverI
      In this projects I have created a sample blog application and admin page. Authenticated user can view the recent posts from author       and also he can provide feedback to posts.
      
  5. CrudOp -> Employee
       Here the Authenticated admin can view the details of employee, he can add/edit/delete new employee. If admin is tried to access          the employee without logged in, he will be redirect to the login page. The logged Out and Signup options are provided to the            user. Generic and Function based views are used.
        
   # How to Use
    - Navigate to the Crudop directory( cd crudop)
    - Activate the virtual Environment (env\Scripts\activate )
    - Navigate to employee project ( cd employee )
    - Run the django project ( python manage.py runserver )
    
    You can run these applications in other devices also (Mobile, other PC's ), but you should be connected to the same network.
    Ex: 
    Suppose you are running the application in "121.12.12.12" IP address , provide this to ALLOWED_HOST of settings.py file
    ALLOWED_HOST = ['122.12.12.12']
    Run using below command 
    python manage.py runserver 0.0.0.0:8000
    Open other device brower and provide URL as : "122.12.12.12:8000/(your url)"
    
