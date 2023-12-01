# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

ADD ./bot /app/bot
ADD .env /app/.env
ADD requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV NAME TELEGRAM_API_KEY
ENV NAME USER_ID
ENV NAME TRADED_QUANTITY
ENV NAME LARGE_TRADED_QUANTITY
ENV NAME SYMBOL

CMD ["python", "-m", "bot"]