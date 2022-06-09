# use docker

```
# Run container with a shared examples/ directory
# Note that `--rm` will make the container be deleted if you exit it
# (if you want to persist data from the container, use docker volumes)
# (we need to increase maximum stack size, so we use ulimit for that)
$ docker run --rm -it --ulimit stack=100000000:100000000 trailofbits/manticore bash

```

