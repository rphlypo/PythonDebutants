#!/bin/bash

echo Starting the jupyter server on port 8842
gnome-terminal -x jupyter notebook --port 8842 ./notebook &&
echo Starting the presentation on port 8000
gnome-terminal -x npm start --prefix ./reveal.js &&
echo Be patient ... serving data to your web-browser
exit 0
