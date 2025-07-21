# Spirit-D
This is the first init of the project. General goal is to create a drivers app for sharing enjoyable roads, rating them, generating roadtrips, using meta-data (type of car, hp, drivers style, ...) to find the next best Spirited Drive and more. Stay tuned.

Progress notes:
21.7.2025: Adding requirements.txt and trying to create PostgreSQL in Docker container
Requirements.txt had to be done in the virtual envi and bcs it was empty (no libs), I downloaded pandas and then used pip freeze > requirements.txt
Postgre is still in progress, managed to get Docker, pull postgre image and create container with it but struggle a bit with the access proposed by datacamp tutorial (https://www.datacamp.com/tutorial/postgresql-docker?dc_referrer=https%3A%2F%2Fwww.google.com%2F), hence went with approach proposed here (https://www.youtube.com/watch?v=Hs9Fh1fr5s8). Will follow up on both as they seem reasonable. Alternatively going with: https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/. Also, need to follow up with the postgis extensions: https://hub.docker.com/r/postgis/postgis/