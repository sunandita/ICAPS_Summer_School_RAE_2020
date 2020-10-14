RAE and UPOM together form a refinement acting-and-planning engine.

We have the following domains in the ./domains folder.

1. domain_chargeableRobot: A chargeable robot collecting different objects

2. domain_springDoor: Robot needs to collect objects in an environment with spring doors and ordinary doors

3. domain_exploreEnv: Robots and UAV move through a partially mapped terrain and collects various data

4. domain_searchAndRescue: UAVs and UGVs carry out search and rescue operations

5. domain_orderFulfillment: Robots pack objects in a warehouse and deliver them to a loading dock

6. domain_test: To modify and play with

HOW TO USE?

To test on any domain, use the following command in terminal

python3 testRAEandUPOM.py [-h] [--v V] [--domain D] [--problem PROBLEMNAME] 

optional arguments:

  -h, --help  	show this help message and exit
  
  --v V      	verbosity of RAE and UPOM's debugging output (0, 1 or 2)
  
  --domain D    domain ID of the test domain ("CR", "SD", "SR", "EE", OF", "test") (see below)
  
  --problem P   problem id for the problem eg. 'problem1', 'problem2', etc. The problem id should correspond to a problem inside the folder 'problems/domain'.
  
  --n_RO numRollouts 	Number of rollouts of UPOM

Domain ID are as follows:

chargeableRobot: 'CR',

springDoor: 'SD',

exploreEnv: 'EE',

searchAndRescue: 'SR'

orderFulfillment: 'OF',

test: 'test'


HOW TO ADD NEW PROBLEMS? 

Please go inside the folder ./problems/<domain> to view examples of problem files. A problem file  specifies the initial state, the tasks arriving at different times and various parameters specific to the domain. Please follow the
following syntax to name a problem file.

problemId_DomainID.py

For example, a problem of SD domain with problemId 'problem1' should be named problem1_SD.py.

DOCKER SETUP STEPS:

Run ./buildDocker.sh only once

Run docker ps -a # to get the container_ID

docker start container_ID

docker attach container_ID 

exit # To exit from docker container 

CONDA SETUP STEPS:

conda env create -f RAE.yml

ON YOUR LOCAL TERMINAL:

To test problem1 of Spring door, use the commands:

cd ./RAE_and_UPOM

python3 testRAEandUPOM.py --domain SD --problem problem1



