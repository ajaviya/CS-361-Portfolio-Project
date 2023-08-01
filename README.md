# CS-361-Portfolio-Project
---------------------------

## Communication Contract

### How to programatically REQUEST data from my microservice:
My microservice will be running continuously in the background. My partner's main project file contains a function, check_login, which will prompt the user to enter a username and password. This information will be assigned to variables which are then stored in a JSON file. This function will then make a POST request to the /login url. I have placed an example call below:

data = {"username": username, "password": password}

response = requests.post("http://localhost:5000/login", json=data)

This triggers a request for data from my microservice

### How to programatically RECEIVE data from my microservice:
When my microservice gets this call at the login URL, it has a function, validate_login, which gets a handle on the JSON file. It then extracts the username and password variables the user entered. It then checks an internal database of valid username-password combinations, and if the input is valid, it sends a JSON containing a variable, "validated" with a value of True, and if the input is invalid, the variable's value is set to False. My partner's main project will then utilize this JSON file to branch execution in his code depending on the variable's value. 

This is how it receives data from my microservice.

### ULM Sequence Diagram

![image](https://github.com/ajaviya/CS-361-Portfolio-Project/assets/92184420/86b8aa6c-4b48-4108-969b-269ccfc61f60)
