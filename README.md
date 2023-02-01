# Simple-Microservices-with-FastAPI-and-React
Simple Microservices App with FastAPI and React

Introduction
This project is a simple microservices app that is built using Python FastAPI for the backend and React for the frontend. The app utilizes RedisJSON as a database and uses Redis Streams for event dispatch.

Prerequisites
Before starting this project, make sure that you have the following tools installed:

Python 3.x
Node.js and npm
Redis JSON
Redis Streams

Setting up the Environment
Create a new Python virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate

Install the required Python packages:
pip install fastapi[all]
pip install redis


Create a new React project and install the required npm packages:
npx create-react-app my-app
cd my-app
npm install


Running the App
Start the Redis JSON and Redis Streams databases.

Start the FastAPI server by running the following command:
uvicorn main:app --reload

Start the React app by running the following command:
npm start

Features
User-friendly interface built with React.
Backend built with Python FastAPI, a modern and fast framework for building APIs.
Database powered by RedisJSON, a NoSQL database.
Event dispatch using Redis Streams, an event bus similar to RabbitMQ or Apache Kafka.
Conclusion
This project provides a simple but powerful way to build microservices apps with Python and React. The use of RedisJSON and Redis Streams allows for easy data storage and event dispatch, making it a great choice for microservices apps.
