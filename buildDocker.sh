#Copyright 2020 Debjit Pal
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this 
#software and associated documentation files (the "Software"), to deal in the Software 
#without restriction, including without limitation the rights to use, copy, modify, 
#merge, publish, distribute, sublicense, and/or sell copies of the Software, and 
#to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all 
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
#INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
#PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
#FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
#ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
