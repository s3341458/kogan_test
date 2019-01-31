# Cheng's Kogan Test

This project is for my [Kogan Code Chanllenge](https://kogan-recruitment.herokuapp.com/challenge/e7611d8085963218c6701087fadbe79c/)

## Local installation

The local development environment requires:

 - [Docker](https://docs.docker.com/)
 - [Docker Compose](https://docs.docker.com/compose/install/)

 See these links to install on your system.

### manual test

Start up the website:

    docker-compose up

Open any browser and visit [Test Website](http://127.0.0.1:4000/)

### autotest

Run unit tests:

    docker-compose run --rm api_consumer pytest

### Needs to mention

+ The main logic and fun stuff is in [api.py](https://github.com/s3341458/kogan_test/blob/master/flask_api_consumer/api.py)
+ Due to the time limitation, I ignored pydoc stuff although I know it is a important thing that you want to test.
+ Due to the time limitation, I ignored the error handlings part which is actually really important for handling api response.
+ I used a more "functional" way to do the work instead of a more "Pythonic" way for interests reason.
  This does not mean I can not write "Pythonic" code or I do not like "Python".
