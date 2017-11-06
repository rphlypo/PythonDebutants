#!/bin/bash

echo Starting the jupyter server on port 8842
gnome-terminal -x jupyter notebook --port 8842 ./notebook &&
echo Starting the presentation
grunt --gruntfile ./reveal.js/Gruntfile.js serve

exit 0
