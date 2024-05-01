# Image Dehazing with Boundary Constraint and Contextual Regularization

## Description

This project focuses on the implementation and enhancement of a novel method for single image dehazing. The proposed method combines a boundary constraint with a weighted L1-norm based contextual regularization to estimate the unknown scene transmission, aiming to remove hazes from a single input image efficiently and effectively.

This project is Implementation of Reseach Paper. [Ckeck Out](Documents/Implemented_Research_paper.pdf)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## Features

This Project contains following Features :

- Basic Tkinter UI to get image dehazing results of hazy image.
- PSNR(Peak Signal to Noise Ration) : The calculation of noise removal of hazy image.
- SSIM(Structural Similarity Index) : The Structural calculation of dehaze image in context of Luminance and Contrast.

## Installation

To test the working of the project, follow these installation steps:

1. Clone this repository to your local machine.

```bash
git clone https://github.com/P6s-fx/Image-Dehazing-with-Boundary-Constraint-and-Contextual-Regularization.git
```
2. Install the required Python libraries if you haven't already.
```bash
pip install -r requirements.txt
```

3. Run the application.
```bash
python main.py
```

## Usage
- Launch the application using the installation steps mentioned above.
- Use the user-friendly interface to dehaze Hazy Image.
- Check PSNR and SSIM from the Terminal to analyze the dehazing. 

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
We would like to acknowledge the following libraries and modules that made this project possible:

- Tkinter
- Pillow
- OpenCV
- Numpy

## Contact
If you have questions or want to get in touch with the project maintainer, feel free to contact:
- Param Suthar
- Email: param.corpid@email.com
- Linkedin: [Linkedin/ParamSuthar](https://www.linkedin.com/in/paramsuthar)
- GitHub: [Github/P6s-fx](https://github.com/P6s-fx)
