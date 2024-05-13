from moviepy.editor import *

import_path_file = None
export_path_file = None

if import_path_file and export_path_file:
    video = VideoFileClip(import_path_file)
    video.audio.write_audiofile(export_path_file)