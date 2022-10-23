# ptf-2022-hackathon
An educational game to promote DEI through the lense of lived experience of the trans and NB community.  This project is for the 2022 PowerToFly Hackathon.


## Docker Container (for development)
The docker container image is hosted on DockerHub [here](https://hub.docker.com/r/sk8forether/trans-game-dev), which can be obtained with `docker pull sk8forether/trans-game-dev` if you have docker installed.  Then you just have to install [pygame](https://www.pygame.org/wiki/GettingStarted) with `python3 -m pip install -U pygame --user` in the container.

### Full commands to pull and set up the container:
```
docker pull sk8forether/trans-game-dev
docker run sk8forether/trans-game-dev:latest sleep 1000000 &
docker exec -it <container-name> /bin/bash
```

This puts you in the shell of the container which will keep running in the background even if you exit.  So you have to kill the container instance when you're done (making it easier for development).  Then run `python3 -m pip install -U pygame --user` in the container, and you should be all set
the shell drops you in at `/home/dev` (dev is the name of the user) which already has the github repo cloned in, so just `cd ptf-2022-hackathon` and do a `git pull` and you're all set.
