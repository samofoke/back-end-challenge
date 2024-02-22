# back-end-challenge

### running the project
- running `docker-compose up --build` will build project and run it.

### for the ENV
- creating a .env file on the root folder.
~~~
MONGO_URI = mongodb+srv://adminname:password@data-test-cluster.frt9pjx.mongodb.net/my-data-test

JWT_SECRET_KEY = the generated key
~~~
### In terms of JWT for generating a secret key
- you will to run `python` in your terminal and `import secrets` and after run `secrets.SystemRandom().getrandbits(128)`

### used postman to test the endpoiints
- for example `http://172.19.0.2:5000/api/v1/user`
~~~
{
  "name": "Sam",
  "surname": "Thor",
  "email": "sam.thor@gmail.com",
  "password": "StrongPassword1234",
  "role": "SUPER"
}

laogin 

{
    "email": "sam.thor@gmail.com",
    "password": "StrongPassword1234"
}
~~~
- getting the user `http://127.0.0.1:5000/api/v1/user/:user_id`