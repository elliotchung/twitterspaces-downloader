video_files = [f"{i}_a.aac" for i in range(1500, 2189)]
input_string = "|".join(video_files)
final_command = f'ffmpeg -i "concat:{input_string}" -c copy output4.ts'
print(final_command)