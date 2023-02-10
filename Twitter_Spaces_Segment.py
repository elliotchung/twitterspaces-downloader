video_files = [f"{i}_a.aac" for i in range(0, 501)]
input_string = "|".join(video_files)
final_command = f'ffmpeg -i "concat:{input_string}" -c copy output.aac'
print(final_command)
