# Fusion Based Variational Image Dehazing 

## Understand the best hyperparameters for your use case: :eyes:
Please use this web-app to upload your image and understand what parameters work best for your use case:<br>
https://utkarsh-deshmukh-streamlit-image-dehaze-run-haze-removal-vo1yua.streamlit.app/
<br> Hope it helps you use the library more efficiently :champagne:

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
This code is an implementation of the paper "Efficient Image Dehazing with Boundary Constraint and Contextual Regularization"
The algorithm can be divided into 4 parts:
  - Airlight estimation
  - Calculating boundary constraints
  - Estimate and refine Transmission
  - Perform Dehazing using the estimated Airlight and Transmission
  
# License
  - This project is licensed under the BSD 2 License - see the LICENSE.md file for details
  
# Acknowledgements

  - The author would like to thank "Gaofeng MENG" and his implementation of his algorithm: https://github.com/gfmeng/imagedehaze

  - The author would like to thank Gaofeng MENG, Ying WANG, Jiangyong DUAN, Shiming XIANG, Chunhong PAN for their paper "Efficient Image Dehazing with Boundary Constraint and Contextual Regularization"
  
  - The author would like to thank Alexandre Boucaud. The function psf2otf was obtained from his repository. (https://github.com/aboucaud/pypher/blob/master/pypher/pypher.py)
  
  - The Author would like to thank Dr. Suresh Merugu for his matlab implementation of the codes. This repository is the python implementation of the matlab codes.
 
 Merugu, Suresh. (2014). Re: How to detect fog in an image and then enhance the image to remove fog?. Retrieved from: https://www.researchgate.net/post/How_to_detect_fog_in_an_image_and_then_enhance_the_image_to_remove_fog/53ae3f10d2fd64c3648b45a9/citation/download. 


# Citation
@INPROCEEDINGS{6751186, 
  author={G. Meng and Y. Wang and J. Duan and S. Xiang and C. Pan}, 
  booktitle={IEEE International Conference on Computer Vision}, 
  title={Efficient Image Dehazing with Boundary Constraint and Contextual Regularization}, 
  year={2013}, 
  volume={}, 
  number={}, 
  pages={617-624}, 
  month={Dec},}
