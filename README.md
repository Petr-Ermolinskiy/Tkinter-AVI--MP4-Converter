
# Simple Tkinter AVI→MP4 convertor

It is a simple application based on Tkinter and Moviepy to convert AVI video to MP4 video. 




## Installation

If you are using git, you can clone the project and set up a virtual environment using Python 3.11.6 (only this version was tested) in PyCharm or any other workspace:
```bash
git clone https://github.com/Petr-Ermolinskiy/Tkinter_AVI_to_MP4_Converter.git
```
Otherwise you can download the files manually. Then you can open a terminal or command prompt and navigate to the directory where you want to create the virtual environment, i.e., the directory where you have placed the files from this repository. You can use `cd your/path/to/the/directory`.

Run the following command to create a new virtual environment named `venv` (make sure that you have the Python 3.11.6 installed):
```bash
python3.11 -m venv venv
```

Activate the virtual environment. On Windows, you can do this by running:
```bash
venv\Scripts\activate
```
On macOS and Linux, you can do this by running:
```bash
source venv/bin/activate
```

Finally, you can install all the necessary packages:

```bash
pip install -r requirements.txt
```
Run the script:
```bash
python main.py
```

Please __note__ that this application supports both Russian and English languages. To change the language, you can simply click on the title of the main screen, i.e., 'Конвертация видео из AVI в MP4' or 'Convert video from AVI to MP4'.




## Creating an exe file

To create an exe file in Windows, you need to execute the following command in the terminal or command prompt:

```bash
pyinstaller --onefile --windowed --add-data "logo.ico;." --icon=logo.ico main.py
```
I strongly recommend that you use [UPX](https://upx.github.io/) to reduce the size of the executable. In this case you can run the following command:
```bash
pyinstaller --onefile --windowed --add-data "logo.ico;." --icon=logo.ico --upx-dir=Path\to\the\upx-4.2.2-win64 main.py
```
The final size of the exe file will be about 38 MB.

## Usage

Just add the path to the folder with AVI files in the empty field, specify the video bitrate and click the button. 
