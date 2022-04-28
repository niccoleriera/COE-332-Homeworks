# Software Diagram for "Tracking the ISS" Project
The task for the "Tracking the ISS" Project was to sort through different kinds of information about the sightings of the International Space Station (ISS), such as its position and velocity at given times as well as the cities and countries it can be seen in. For this diagram, I wanted to show how exactly the process of accessing these different kinds of information works. In my example, I used the route /countries to show how the user makes a request to the Flask app which returns a list of countries where the ISS was spotted. In order to do this the user first attains the ISS Data from NASA's webpage, this is shown at the very top of the diagram. The user uses the command wget so that the data can be found in their current working directory. After this, the user then pulls the image from Dockerhub, builds it, and runs it. This is shown at the right of the diagram. Finally, the user executes the command curl localhost:5022/countries on the server which returns the list of countries where the ISS was spotted.

## How to Access More of the Project
To see the actual project simply copy and paste the following link into your web browser:
> https://github.com/niccoleriera/tracking-the-ISS-sightings

