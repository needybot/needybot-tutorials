# Needybot Tutorials 
A collection of tutorials showing fun things you can build with Needybot.

## Quick Start
Download the required packages into you catkin workspace and run `catkin_make`

    $ cd ~/catkin_ws     
    $ git clone https://github.com/needybot/needybot-core     
    $ git clone https://github.com/needybot/needybot-speech     
    $ git clone https://github.com/needybot/needybot-tutorials     
    $ catkin_make     

In order to run Needy's speech package you'll want to setup a free Ivona account to generate the voice files. See the [needybot-speech readme](https://github.com/needybot/needybot-speech) for more information.

Once the speech package is setup run Needy's Hello World demo:

    $ roslaunch needybot_hello_world hello.launch    

Needy should fire up, connect with its iPad and start blabbering away.
