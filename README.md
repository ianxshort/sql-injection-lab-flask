# SQLi Lab: Authentication Bypass Demonstration
 
Features a hands-on project that demonstrates SQL injection vulnerabilities, explanations, and fixes using Flask and SQLite 

## About This Project
I worked on building two versions of a login application in order to understand how SQL injection works and the techniques to prevent them

- vulnerable-app/: App contains intentionally vulnerable code 

- secure-app/: Implements parameterized queries to ensure proper security

This project demonstrates:
- How SQL Injection works in applications
- How attackers can exploit authentication flaws 
- How to fix SQL injection vulnerabilities 
- Why input handling is a critical component in backend development 


## Technologies Used 
- Python (Flask)
- SQLite 
- HTML/CSS
- SQL Injection concepts 


# OWASP TOP 10 Mapping 
This project features a vulnerability listed on the OWASP Top 10: 
    - A03:2021 – Injection

The vulnerable applications exhibits a very common real-world coding vulnerability, while the secure version follows OWASP-recomended remediation techniques 


# Demonstrated Vulnerabilities 
1. Tautology Authentication Bypass
The exploitation of always true conditions to bypass authentication

    - Example payload:
    admin' OR '1'='1' --

    - Result: Successful login regardless of credentials 

2. Boolean-Based SQL injection
Using true/false responses to extract database information

    - Example payload:
    ianshor5' AND SUBSTR(password,1,1)='1' --

    - Result: Attackers can extract information without direct input 

Documentation featuring attack explanations, fixes, and screenshots are available below 

- [Tautology Authentication Bypass](docs/injection-example1.md)

- [Boolean-Based SQL injection](docs/injection-example2.md)


## How to Run 

1. Clone the Repository 

    git clone https://github.com/ianxshort/sql-injection-lab-flask.git

    cd sql-injection-lab-flask

2. Install the Dependencies 

    pip install flask

3. Run Vulnerable Application

    cd vulnerable-app

    python app.py

4. Run the Secure Application
    
    cd secure-app

    python app.py

Visit in Browser:

http://127.0.0.1:5000



## Project Signifigance 

SQL injections remains to be one of the most critical and persistant vulnerabilities within cybersecurity, hence it's placement within the OWASP Top 10 

This lab is a displays how little mistakes in coding logic can lead to to:
    - Unauthorized access 
    - Privilege Escalation (admin)
    - Database Exposure through injected queries 



## Disclaimer

    The creation of this project was strictly for educational purposes. All vulnerabilities displayed were intentionally executed in a controlled environment 


## Author 

    Ian Short 
    Cybersecurity Student

    Github: https://github.com/ianxshort
