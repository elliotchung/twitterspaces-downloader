# twitterspaces-downloader
fastest way to download twitter spaces recordings
## Requirements:
ffmpeg
Chrome
VScode
Jdownloader2
PowerToys
### Steps:
1. Navigate to the twitter space recording on Chrome
2. Open ddevtools by pressing F12 andd navigate to the network tab
3. Filter the results with 'chunk_'
![image](https://user-images.githubusercontent.com/101564632/218022552-c7430218-b769-4619-9fd7-b42866c22590.png)
4. Wait for the recording to finish and all the chunks are shown in the network tab
5. Follow the instructions here to get all the URLs of the chunks:
https://stackoverflow.com/questions/41200450/multiple-urls-copy-in-sources-network-tab
6. Download all the chunks with your favourite download manager, e.g Jdownloader2
7. Use PowerToys's power rename tool to rename the files to an easier format
![image](https://user-images.githubusercontent.com/101564632/218021383-49e6c862-05cb-4228-a522-d31b251ecc23.png)
8. Use the python code provided to create the cmd command needed to merge the chunks together
