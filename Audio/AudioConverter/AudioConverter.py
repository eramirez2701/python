from pydub import AudioSegment
from pydub.utils import mediainfo
import pathlib


def get_filepaths(directory, extension):
    filepaths = []
    for filepath in pathlib.Path(directory).glob('**/*.' + extension):
        filepaths.append(filepath)
    return filepaths


def get_tags(file_path):
    return mediainfo(file_path).get('TAG', {})


def convert_files(directory, input_audioextension, audio_format, audio_codec):
    filepaths = get_filepaths(directory, input_audioextension)
    for fp in filepaths:
        output_extension = '.' + audio_format
        new_filepath = fp.with_suffix(output_extension)
        input_file = AudioSegment.from_file(fp, input_audioextension)
        input_file.export(new_filepath,
                          format=audio_format,
                          bitrate=audio_codec,
                          tags=get_tags(fp))
        print("Exported file: " + str(new_filepath))
