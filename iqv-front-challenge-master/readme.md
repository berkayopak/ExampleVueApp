# IQVizyon Frontend Challenge

To run the docker image, you'll either need to pull the image from gitlab registry or you can fetch the git repository and build it yourself.

You can fetch or build the 

    docker pull registry.gitlab.com/iqvizyon/iqv-front-challenge:latest

or

    docker build -t registry.gitlab.com/iqvizyon/iqv-front-challenge .

The docker image exposes port 5000, you'll need to bind it. Also you must define the command `web`

    docker run -i -p 5000:5000 registry.gitlab.com/iqvizyon/iqv-front-challenge:latest web
    
**Or simply use the provided docker-compose file.**

    docker-compose up

This will build the image and run it appropriately.

### LICENSE
This software is licensed under GPLv3 by IQVizyon Dijital Dönüşüm AŞ © 2020. To read more, please refer to license file.