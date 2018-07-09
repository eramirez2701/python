from pydub import AudioSegment
import pathlib

AudioSegment.converter = "C:/ffmpeg/bin/ffmpeg.exe"


def get_filepaths(directory, extension):
    filepaths = []
    for filepath in pathlib.Path(directory).glob('**/*.' + extension):
        filepaths.append(filepath)
    return filepaths


def convert_files(directory, input_audioextension, audio_format, audio_codec):
    filepaths = get_filepaths(directory, input_audioextension)
    for filepath in filepaths:
        new_filepath = filepath.with_suffix(audio_format)
        print(filepath)
        input_file = AudioSegment.from_file(filepath, input_file)
        input_file.export(new_filepath,
                          format=audio_format,
                          bitrate=audio_codec)
        print("Exported file: " + str(new_filepath))

