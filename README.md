Flask HelloWolrdFlask Project
Infrastructure RequirementsServer
Flavor      /   OS              /   QTY /   Purpose     /   Elsem1          /   Ubuntu 16.04    /   1   /   Web         /   NoneNetwork
QTY /   Purpose     /   Else1   /   Service     /   NoneApplication Requirementspython3.5virtualenvuwsginginxBootstrap# install prerequisites (ubuntu 16.04)
$ ./misc/bootstrap.sh

Prepare development environment# create virtualenv for development environment
$ make venv_dev

Run application in development environment# enable virtualenv
$ source venv_dev/bin/activate

# run flask app
$ ./src/app.py

Test$ make unittest

Lint$ make lint
