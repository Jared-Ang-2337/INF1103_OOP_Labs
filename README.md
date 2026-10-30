Build and run Docker with
docker build -t inf1103-inventory .
docker run --rm -it -v "${PWD}:/app" -w /app inf1103-inventory