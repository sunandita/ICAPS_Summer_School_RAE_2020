RAE and RAEplan/UPOM together form a refinement acting-and-planning engine with multiple stacks. Each stack is implemented as a Python thread.

We have the following domains in the domains folder.

1. domain_chargeableRobot: A chargeable robot collecting different objects
2. domain_springDoor: Robot needs to collect objects in an environment with spring doors
3. domain_exploreEnv: Robots and UAV move through an area and collects various data
4. domain_searchAndRescue
5. domain_orderFulfillment

HOW TO USE?
To test on any domain, use the following command in terminal

python3 testRAEandRAEplan.py [-h] [--v V] [--domain D] [--problem P] [--plan S] [--c C] [--b breadth]
optional arguments:
  -h, --help  	show this help message and exit
  --v V      	verbosity of RAE and RAEplan's debugging output (0, 1 or 2)
  --domain D    domain code of the test domain (STE, CR, SD, EE, SOD, IP, SF, OF) (see below)
  --problem P   problem id for the problem eg. 'problem1', 'problem2', etc. The problem id should correspond to a
                problem inside the folder 'problems'.
  --plan pl   	Do you want to use planning or not? ('y' or 'n')
  --c C      	Mode of the clock ('Counter' or 'Clock')
  --b breadth 	Number of methods RAEplan should look at (for each task and sub-task) during planning

domain codes are as follows:
domain_chargeableRobot: 'CR',
domain_springDoor: 'SD',
domain_exploreEnv: 'EE',
domain_searchAndRescue: 'SR'
domain_orderFulfillment: 'OF'


HOW TO ADD NEW PROBLEMS? 
A problem file (Please go inside the folder problems/domain to view one) specifies the initial state, the tasks arriving at different times and various parameters specific to the domain. To define a new problem, please follow the
following syntax to name the file.

problemId_domainCode.py

For example, a problem of SD domain with problemId 'problem1' should be named problem1_SD.py.
To test problem1 of Spring door, use the command:

python3 testRAEandRAEplan.py --domain SD --problem problem1

The commands can be executed in two modes: 'Clock' or 'Counter'.
By default, the mode is set to 'Counter'.