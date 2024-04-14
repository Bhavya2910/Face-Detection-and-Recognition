# Face Detection and Recognition

This project implements a face detection and recognition system using OpenCV in Python. It detects faces in images or video streams from a webcam and recognizes them based on pre-trained models.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use this project, follow these steps:

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/face-detection-recognition.git
    cd face-detection-recognition
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Download pre-trained models:
    - LBPH Face Recognizer: [trainer.yml](link-to-your-trained-model)
    - Haar Cascade Classifier for Face Detection: [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)

4. Place the downloaded files in the appropriate directories (`trainer/trainer.yml` and `haarcascade_frontalface_default.xml`).

## Usage

To run the face detection and recognition system, execute the main Python script:


Ensure that your webcam is connected and accessible. The system will display the live video stream with detected faces and recognized IDs.

## Features

- Real-time face detection and recognition using OpenCV.
- Overlay recognized IDs and confidence levels on the video stream.
- Adjustable parameters for face detection (scale factor, minimum neighbors, etc.).

## Dependencies

- Python 3.x
- OpenCV
- NumPy

## Contributing

Contributions to this project are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/feature-name`).
3. Make changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/feature-name`).
5. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).
