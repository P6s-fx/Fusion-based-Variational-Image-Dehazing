# Fusion Based Variational Image Dehazing 
## Installation and Running the tests
  1. Go to the src folder
  2. run the file "example.py"
  3. sample images are stored in the "Images/" folder
  4. Output images will be stored in the "outputImages/" folder

### user controllable parameters (with their default values):
```
airlightEstimation_windowSze=15
boundaryConstraint_windowSze=3
C0=20
C1=300
regularize_lambda=0.1
sigma=0.5
delta=0.85
showHazeTrasmissionMap=True
```

# Libraries needed:
  1.numpy==1.19.0
  2.opencv-python
  3.scipy

# Theory
The algorithm can be divided into 4 parts:
  - Airlight estimation
  - Calculating boundary constraints
  - Estimate and refine Transmission
  - Perform Dehazing using the estimated Airlight and Transmission
