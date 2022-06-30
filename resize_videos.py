import os
import ffmpeg

def resize_video(input_folder, video_name, filename_suffix='_resized', size=[1,1]):

    video_full_path = os.path.join(input_folder, video_name)
    filename, extension = os.path.splitext(video_name)
    extension = '.mp4'
    output_folder = 'resized_videos'
    output_file_name = os.path.join(output_folder, filename + filename_suffix + extension)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    

    try:
        probe = ffmpeg.probe(video_full_path)
        vid_size = float(probe['format']['size'])

        i = ffmpeg.input(video_full_path)
        ffmpeg.output(i, output_file_name,
                        **{'c:v': 'libx264', 's': f'{size[0]}x{size[1]}', 'c:a': 'aac'}
                        ).overwrite_output().run()

        if os.path.getsize(output_file_name) <= vid_size:
            return output_file_name
    except FileNotFoundError as e:
        print('You do not have ffmpeg installed!', e)
        print('You can install ffmpeg by reading https://github.com/kkroening/ffmpeg-python/issues/251')
        return False

if __name__ == '__main__':

    input_folder = 'vids_to_resize'
    vids_to_compress = os.listdir(input_folder)
    for i, vid in enumerate(vids_to_compress):
        print(f'Compressing {i+1}/{len(vids_to_compress)}')
        resize_video(input_folder, vid, size=[700, 566])


