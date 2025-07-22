# Spirit-D
This is the first init of the project. General goal is to create a drivers app for sharing enjoyable roads, rating them, generating roadtrips, using meta-data (type of car, hp, drivers style, ...) to find the next best Spirited Drive and more. Stay tuned.


# Progress notes:

##

## 22.7.2025: Postgre followup
So the oficial docker manual (+ the YT video) worked the best hence just running `docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres` to run the container. The image is already pulled, hence the run command with extra args and last `-d postgres` to say which image to run. Then to run the DB itself just hit `docker exec -it some-postgres psql -U postgres`. -it is there for interactivity and -U for required username (given I havent mentioned one, this seems default), rest follows syntax: docker exec [options] container_command [arguments]. The `psql` is the actual command to run the DB.
But few things need to be added. First porting: `docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres`. And volume to save the data event when I remove the container. Hence remove all `docker rm -f some-postgres` and do `docker volume create postgres-data` to create volume to mounted to future containers to save the data. Now I can do `docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -v postgres-data:/var/lib/postgresql/data -d postgres`. Now when removing and running again the container, old data should stay. The location of the volume is there set within the container directory, just to be clear.
But I want to run postgres with postgis extension, hence changing the last part to `-d postgis/postgis` image. 
To use the postgis extension, I need to run `CREATE EXTENSION postgis;` within the psql, then I can create a table using postgis, e.g. like `CREATE TABLE example(id integer, geom geometry(LineString))`.

Now I want to add some data via Python (gpxpy, psycopg2). Followin this to clone just testfile: https://stackoverflow.com/questions/600079/how-do-i-clone-a-subdirectory-only-of-a-git-repository.

## 21.7.2025: Adding requirements.txt and trying to create PostgreSQL in Docker container
Requirements.txt had to be done in the virtual envi and bcs it was empty (no libs), I downloaded pandas and then used pip freeze > requirements.txt
Postgre is still in progress, managed to get Docker, pull postgre image and create container with it but struggle a bit with the access proposed by datacamp tutorial (https://www.datacamp.com/tutorial/postgresql-docker?dc_referrer=https%3A%2F%2Fwww.google.com%2F), hence went with approach proposed here (https://www.youtube.com/watch?v=Hs9Fh1fr5s8). Will follow up on both as they seem reasonable. Alternatively going with: https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/. Also, need to follow up with the postgis extensions: https://hub.docker.com/r/postgis/postgis/