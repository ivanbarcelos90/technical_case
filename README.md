# Technical Case - Dadosfera

## How to start using
* You will need pipenv to install the dependencies. Install with `pip install pipenv`
* After that just run inside the repository folder `pipenv install` and all the dependencies will be installed
* Run data_request.py file to download the data.
* Run this cmd to set up the database: "docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=yourStrong(!)Password" -e "MSSQL_PID=Express" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest".

## The Flow
* Run enviroment.py. This py file is responsible to create the database and the table needed to storage and  process the data.
* You may have to run "sudo apt-get install unixodbc-dev" to run pyodbc package.
* After all set up, you can run result.py. This file will create and open a html file that will contain the required answers.

## Iterative Map (Bonus Question)
* You can run iterative_map.py to see the map of New York City with Pickups and theirs respective Dropoffs of the taxis trips of the year 2010.
* The total samples of the data is 1 million trips. You can change the amount of the trips with the variable sample at query_str.py.
* Each arrow on the map have a particular number, that indicate the trips, so you will be able to track the Pickup and the corresponding Dropoffs.
