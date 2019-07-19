Assignment 2

The API key need before start, I add a default one in case not been set
	export MY_KEY="at_EYedF482zqmiTdQyerFKVsBKlFNfc"

Build it
	docker build --build-arg MY_KEY=$MY_KEY -t my-image .

Run it
	docker run -e MY_KEY=$MY_KEY --rm --name my-running-one my-image '2c:d0:2d:b2:57:7a'

Delete container
	docker container prune

Delete images
	docker image rm <image id>


Test Report
-----------
$ export MY_KEY="at_EYedF482zqmiTdQyerFKVsBKlFNfc"

$ docker build --build-arg MY_KEY=$MY_KEY -t my-image .
  :
  :

$ docker run -e MY_KEY=$MY_KEY --rm --name my-running-one my-image '2c:d0:2d:b2:57:7a'
Mac address: 2c:d0:2d:b2:57:7a is for vendor: Cisco Systems, Inc

$ docker run -e MY_KEY=$MY_KEY --rm --name my-running-one my-image '2b:d0:2d:b2:57:7a'
Mac address: 2b:d0:2d:b2:57:7a does not match to any vendor

$ docker run -e MY_KEY=$MY_KEY --rm --name my-running-one my-image 'b:d0:2d:b2:57:7a'
No handlers could be found for logger "maclookup-requester"
Error: get_vendor with erro: 


