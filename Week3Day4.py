
Part I - What is a wrapper? (not rapper)
A wrapper function is making your code more efficient and DRY (keep it in one language) by wrapping it in a method we can invoke when we need it.
In terms of Python and APIs we want to wrap our api calls in a method so we don't have to fill our code repeating endpoints
when we built SQL and it was wrapped in the Python language - 

APIs and wrappers
Application Program Interface - external db interfaces - opening up data to the world
API keys are used to limit who and how many requests can be made in a given time frame.

Part II - API Limitations/API Keys
API key requirement
API keys are used to limit who and how many requests can be made in a given time frame, bc you dont want anyone to DDoS the system with a hashkey.
When you get a key to an API make sure to see if there are limitations and what those limitations are

Part III - Gitignore and Environmental Variables
NEVER EVER EVER push your KEY to GitHub
You can create a gitignore file and choose which files to not push to github - it will automatically ignore that part of the file when you push to github.
-a (looks for all files.
gitignore will not send the files over movies/gitignore to get it done - a lot in Phase 2.
API keys can be stored in the file and not go anywhere.
You can also use Environmental Variables.

Part IV - Brief Extension of RESTful API Practices
when you build a RESTful API - it does not live on the server. 
only deals with HTTP methods - GET, POST, PUT, DELETE.
RESTful design position

make the code so that it is always useful, can be re-used.


