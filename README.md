# patient-Simulation
Flask application that generates a patients EKG

JSON Values are returned with Patients Heart Rate, ECG values, and Name (which is passed in). The heart rate is randomly generated at the moment. However, this value will have an impact on the ECG generated.

This is used to simulate medical IOT devices.

## Running with Python

To run on CLI/Testing:

 1. cd to the project directory.
 2. python app.py

In another terminal or browser:

 curl -s localhost:5000/api/getPatientData/<patient name>

 i.e. curl -s localhost:5000/api/getPatientData/David

## Docker

To Build:

 docker build -t patient-simulation .

To Run:

 docker run -p 5000:5000 --rm -it patient-simulation

You can now go to localhost:5000/api/getPatientData/<patient name>
 
To Save to a tar file so you can import into other dockers (manually):
 
 save -o ./patient-simulation.tar patient-simulation
 
 To load the tar file:
 
 docker load -i stockz.tar 
