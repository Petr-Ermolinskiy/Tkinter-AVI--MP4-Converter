# necessary libraries
from moviepy.editor import VideoFileClip
import os
import glob
import sys
# import bitrate to check the entry bitrate val
from app_settings import bitrate

# dicts for return value through messagebox
error_dict = {'en': 'Error', 'ru': 'Ошибка'}
info_dict = {'en': 'Conversion if finished', 'ru': 'Конец конвертации'}
path_dict = {'en': 'No path is provided in the main field', 'ru': 'В поле ввода не указан путь'}
no_folder_dict = {'en': 'This folder does not exist, or there are no AVI files in it', 'ru': 'Данной папки нет, либо в ней нет AVI файлов'}
bitrate_is_wrong_dict = {'en': 'Bitrate value is not taken from the list', 'ru': 'Значение битрейта взято не из списка'}
good_convert_dict = {'en': 'Conversion of all videos was successful', 'ru': 'Конвертация всех видео прошла успешно'}
bad_convert_dict = {'en': 'Conversion of not all videos was successful.\nFor details, see the file: ', 'ru': 'Конвертация не всех видео прошла успешно.\nДля деталей смотри файл: '}

# dicts for file and folders name
output_file_name_dict = {'en': 'output', 'ru': 'инфо'}
folder_mp4_name_dict = {'en': 'mp4_files', 'ru': 'mp4_видео'}

# main function to convert avi videos to mp4 videos using codec='libx265'
def convert_avi_to_mp4(path, bitrate_val, language):
    # input error checking
    if path == '':
        _error_ = True
        return _error_, error_dict[language], path_dict[language]
    if bitrate_val not in bitrate:
        _error_ = True
        return _error_, error_dict[language], bitrate_is_wrong_dict[language]

    # massive of all avi files
    files = glob.glob(path + '//' + '*.avi')

    # if no avi files than raise error
    if len(files) == 0:
        _error_ = True
        return _error_, error_dict[language], no_folder_dict[language]

    # this txt file is essential for convert. VideoFileClip can not work without it
    output = open(path + '//' + output_file_name_dict[language] + '.txt', 'wt')
    sys.stdout = output
    sys.stderr = output

    # create a subfolder for mp4 files.
    path_folder_mp4 = path + '//' + folder_mp4_name_dict[language]
    os.makedirs(path_folder_mp4, exist_ok=True)

    # massive of file names that have not been converted
    missed_convert_files = False
    # convert each video and save it to the created folder
    for i in files:
        try:
            clip = VideoFileClip(i)
            clip.write_videofile(path_folder_mp4 + '\\' + str(i.split('\\')[-1][:-3]) + 'mp4', codec='libx265',
                                 bitrate=bitrate_val)
        except Exception:
            missed_convert_files = True

    # closing the txt file
    output.close()

    # output message
    _error_ = False
    if missed_convert_files:
        return _error_, info_dict[language], bad_convert_dict[language] + output_file_name_dict[language] + '.txt'
    else:
        return _error_, info_dict[language], good_convert_dict[language]