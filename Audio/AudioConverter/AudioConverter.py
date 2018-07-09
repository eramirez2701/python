from pydub import AudioSegment
import pathlib

AudioSegment.converter = "C:/ffmpeg/bin/ffmpeg.exe"


def get_filepaths(directory, extension):
    filepaths = []
    for filepath in pathlib.Path(directory).glob('**/*.' + extension):
        filepaths.append(filepath)
    return filepaths


def convert_files(directory, extension, audio_format, audio_codec):
    filepaths = get_filepaths(directory, extension)
    for filepath in filepaths:
        new_filepath = filepath.with_suffix('.mp3')
        print(filepath)
        input_file = AudioSegment.from_file(filepath, "flac")
        input_file.export(new_filepath,
                          format=audio_format,
                          bitrate=audio_codec)
        print("Exported file: " + str(new_filepath))

