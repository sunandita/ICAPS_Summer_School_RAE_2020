#!/bin/bash

DOCKER="$(docker -v)"
DOCKER_OUTPUT=${DOCKER//,/ }
DOCKER_VER="$(cut -d' ' -f3 <<<"$DOCKER_OUTPUT")"
REQUIRED_VER="18.09"

uid=$UID
pwd=$PWD

if [ "$(printf '%s\n' "$REQUIRED_VER" "$DOCKER_VER" | sort -V | head -n1)" = "$REQUIRED_VER" ]
then
	if [ -z "${DOCKER_BUILDKIT}" ] 
	then
		echo "Setting DOCKER_BUILDKIT environment variables.."
		export DOCKER_BUILDKIT=1
	fi
	docker build --network=host -f Dockerfile -t $USER/rae .
	#if [ -z $DISPLAY ]; then export DISPLAY=:0.0; fi
	docker run -v /Users/patras2/ICAPS_Summer_School_RAE_2020/hostdir:/app/ICAPS_Summer_School_RAE_2020/hostdir \
	       	   -e DISPLAY=$IP:0 \
	       	   -v /tmp/.X11-unix:/tmp/.X11-unix \
               -h docker \
               -it $USER/rae:latest
fi
