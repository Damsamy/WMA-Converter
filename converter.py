from pydub import AudioSegment
import glob


def convert_wma(directory):
    # this function converts wma files and takes the desired folder path as a param

    # this variable defines which file name and extension will be searched
    query = "**/*.wma"

    # here we are creating a list with the path(s) of any wma files found in the folder and subsequent
    wma_songs = glob.glob(query, root_dir=f"{directory}", recursive=True)

    # this 'for loop' takes any wma file paths found and uses pydub and ffmpeg to convert them
    # 'Entry' only contains the relative path within the desired folder, so 'directory' is added to
    # include the full file path
    for entry in wma_songs:
        # Load the wma file using its path
        wma_file = AudioSegment.from_file(f"/{directory}/{entry}", codec="wmav2")
        # creates path for exported song with correct file ending
        location = entry.replace(".wma", ".mp3")
        # Export as mp3
        wma_file.export(f"{directory}/{location}", format="mp3")

