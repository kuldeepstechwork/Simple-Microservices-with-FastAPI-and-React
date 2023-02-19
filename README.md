# Simple-Microservices-with-FastAPI-and-React
Simple Microservices App with FastAPI and React

Introduction
This project is a simple microservices app that is built using Python FastAPI for the backend and React for the frontend. The app utilizes RedisJSON as a database and uses Redis Streams for event dispatch.
Here we have two repositories. Frontend and Backend. The Frontend repo contains the code for the Frontend and the Backend repo contains the code for the Backend.

Prerequisites
Before starting this project, make sure that you have the following tools installed:

For Backend:- 
1. First we need to install python 3.10 
2. Install the packages listed in the requirements.txt file inside the Backend repo. To install the packages we can directly use the command  pip install -r            requirements.txt 
  
Setting up the Environment:-
Create a new Python virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate

For Frontend:-
Create a new React project and install the required npm packages:
npx create-react-app my-app
cd my-app
npm install


Running the App:-
1. Start the Redis JSON and Redis Streams databases.
2. Start the FastAPI server by running the following command: uvicorn main:app --reload
3. Start the React app by running the following command: npm start

Features:-
1. User-friendly interface built with React.
2. Backend built with Python FastAPI, a modern and fast framework for building APIs.
3. Database powered by RedisJSON, a NoSQL database.
4. Event dispatch using Redis Streams, an event bus similar to RabbitMQ or Apache Kafka.

Conclusion:-
This project provides a simple but powerful way to build microservices apps with Python and React. The use of RedisJSON and Redis Streams allows for easy data storage and event dispatch, making it a great choice for microservices apps.
