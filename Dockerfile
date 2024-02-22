# pull the latest image
FROM python:3.11

# the working directory
WORKDIR /usr/src/app

# install pipenv
RUN pip install pipenv

# Copy the pipfiles
COPY Pipfile Pipfile.lock ./

#install the project dependencies
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of the files
COPY . .

# Expose the port outside the container
EXPOSE 5000

# Define the env variable
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the app
CMD [ "pipenv", "run", "flask", "run" ]