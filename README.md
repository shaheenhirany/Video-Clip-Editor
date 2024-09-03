# Video Slicer and Merger

This Python script uses the `moviepy` library to extract specific slices from a video based on user input and merge them into a single output video file. The script is interactive and allows you to define multiple slices by specifying start and end times.

## Features

- Load a video file from your local directory.
- Interactively define multiple slices by specifying start and end times.
- Combine the extracted slices into a single video.
- Export the final video as an MP4 file.

## Requirements

- Python 3.x
- `moviepy` library

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Shaheenhirany/videoclip-slicer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd videoclip-slicer
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

    Alternatively, if `moviepy` is the only requirement:

    ```bash
    pip install moviepy
    ```

## Usage

1. Place your input video file in the project directory and name it `input_video.mp4`.

2. Run the script `video.py`:

    ```bash
    python video.py
    ```

3. The script will prompt you to enter the number of slices you want to create. For each slice, you will be asked to provide the start and end times in the format `HH:MM:SS`.

4. The script will validate the times and extract the slices from the video. If the provided times are valid, the slices will be concatenated into a single video.

5. The output video will be saved as `output_video.mp4` in the project directory.

6. The script will print a message indicating the completion of the video processing.

## Customization

- **Video File**: Ensure the input video file is named `input_video.mp4` or update the script to use a different file name.
- **Slice Times**: Enter valid times within the video's duration when prompted.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Contact

If you have any questions, feel free to reach out to the project maintainer at shaheen.nhirani@gmail.com.

---

*Powered by Shaheen Hirani & Ali Karim*
