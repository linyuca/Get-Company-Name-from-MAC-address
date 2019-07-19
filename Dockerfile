FROM python:2.7-alpine

ENV MY_KEY $MY_KEY

RUN pip install maclookup
WORKDIR /usr/src/app
COPY ass.py ./

ENTRYPOINT ["python", "./ass.py"]

# build it
#  docker build --build-arg MY_KEY=$MY_KEY -t my-image .
#  docker build -t my-image .

# run it
# docker run -e MY_KEY=$MY_KEY --rm --name my-running-one my-image '2c:d0:2d:b2:57:7a'

# delete container
# docker container prune

# delete images
# docker image rm <image id>

