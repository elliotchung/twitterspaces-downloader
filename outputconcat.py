video_files = [f"output{i}.ts" for i in range(1, 5)]
input_string = "|".join(video_files)
final_command = f'ffmpeg -i "concat:{input_string}" -c copy 10feb.aac'
print(final_command)