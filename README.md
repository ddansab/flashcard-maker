## How To setup
- Click the `<> Code` dropdown above, and select `Download Zip`
- Extract the zip wherever you want on your computer. You can even leave it in Downloads if you want.

- Open `terminal`
- Check your Python version:
    - type `python3 --version` into the terminal
    - if prompts to install Python3, go ahead and install
- Once Python3 is installed, copy/paste the 4 following 4 lines in order (one at a time, just to be safe):
    <!-- install pip -->
    - `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
    - `python3 get-pip.py`
    <!-- install dependencies -->
    - `pip3 install googletrans==3.1.0a0`

## How to Use
- Paste or input your new characters into the `starter_file.txt` file 
    - separate new words/phrases onto lines
- Navigate to the `/flashcard_maker` directory within your terminal
    - type `cd`, space `/path/to/folder` OR:
    - type `cd`, space, then drag the folder from your filefinder into your terminal
- Once inside the correct directory, just type `python3 flashcard_maker.py`
- Follow the prompts
- ...
- ...
- Profit

I have some characters already in the starter file just to test functionality on your machine. You can change the `starter_file.txt` file as many times as you want, but **ONLY CHANGE THE STARTER FILE**
