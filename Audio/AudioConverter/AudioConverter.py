from pydub import AudioSegment
from pydub.utils import mediainfo
import pathlib
import gc

class AudioConverter:
    def __init__(self, input_path, input_audio_extension, output_audio_extension, codec)
        self.input_path = input_path
        self.input_audio_extension = input_audio_extension
        self.output_audio_extension = output_audio_extension
        self.codec = codec


    def get_filepaths(self):
        filepaths = []
        for filepath in pathlib.Path(self.input_path).glob('**/*.' + self.input_audio_extension):
            filepaths.append(filepath)
        return filepaths


    def get_tags(self, filepath):
        return mediainfo(filepath).get('TAG', {})


    def convert_files(self):
        filepaths = self.get_filepaths()
        for fp in filepaths:
            try:
                output_extension = '.' + self.output_audio_extension
                new_filepath = fp.with_suffix(output_extension)
                print('Converting ' + str(fp) + ' to ' + self.codec)
                input_file = AudioSegment.from_file(fp, self.input_audio_extension)
                input_file.export(new_filepath,
                                  format=self.output_audio_extension,
                                  bitrate=self.codec,
                                  tags=self.get_tags(str(fp)))
                print("Exported file: " + str(new_filepath))
                del input_file
                gc.collect()
            except FileNotFoundError:
            except MemoryError:
                continue
