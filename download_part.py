import subprocess



'''

➙    --rm-cache-dir             :         Delete all filesystem cache files

➙    -f, --format FORMAT        :         Video format code

➙    -x, --extract-audio        :         Convert video files to audio-only files(requires ffmpeg or avconv and ffprobe or avprobe)

➙    --audio-format FORMAT      :         Specify audio format: "best", "aac", "flac", "mp3", "m4a", "opus", "vorbis", or "wav"; "best" by default; No effect without ' -x '

➙.   --no-check-certificate     :         Suppress HTTPS certificate validation

'''



def down_song(video_link,song_title,widgets):

    p = subprocess.run(['youtube-dl','--rm-cache-dir'],capture_output=True,text=True)

    p1 = subprocess.run(['youtube-dl','-f','bestaudio','--no-check-certificate','--extract-audio','--audio-format','mp3',video_link])

    print('[+]song downloaded')

    widgets[0].setText('!!SONG DOWNLOADED!!') # Syntax : Label.setText('<string-you-now-wish-to-get-displayed>') -  this command is used to change the text of any label present in the GUI window
                                              # In the main output of our project , just below the search box , there is a label that says :
                                              # 'please note that songs are stored in the same directory as this program' on the GUI window
                                              # The objective was  ➙ After the song gets downloaded , we want to inform the user the same
                                              #                    ➙ we will do this by changing the above label's content with : "!!SONG DOWNLOADED!!"
                                              #                    ➙ This will help the user to find out whether the song got downloaded or not.
                                              # This objective is achieved by the command : Label.setText('!!SONG DOWNLOADED!!') .  The setText('') command will now replace the string you gave
                                              # with the content you gave within the parenthesis . So , here , we have replaced the label-content with the string : '!!SONG DOWNLOADED!!'
                                              # Since , the label is present in the GUI window ( the output window ) , the change in label-content will be viewable by us.




    widgets[1].setText('')  # Syntax : Label.setText('') - this command is used to change the text of any label present in the GUI window , READ BELOW EXPLANATION.
                            # In the main output of our project , we give the name of song in a search-box (stored in the program as a string) .
                            # The objective was ,  ➙ the song name we gave in the search-box will only be visible to us until the completion of the download,
                            #                      ➙ and then after the song is downloaded , now we want the content we gave in the search-box to disappear ,
                            #                      ➙ so that , now we can input in , a new song name that we wish to download conveniently , without having to
                            #                      ➙ erase the content we earlier gave manually , by using the backspace key of our keyboard to erase all the characters
                            # This command will satisfy the very objective that we had . The setText('') command will now replace the string you gave with the content you gave
                            # within the parenthesis . So , here , we have replaced the content with an empty string using this command .
                            # This is why , as soon as the song downloads , the content you gave in the main output screen will disappear , at the same time giving us
                            # convenience to give a new song name later again.


    widgets[2].setEnabled(True) # Syntax : Button.setEnabled('<True-or-False>')
                                # Basically in the main output of our project , after giving in the song name
                                # We click the download Button , When we click the download button , the button will highlight for a sec to indicate that we have clicked.
                                # After that we wouldn't want the Download button to be still functionable or else if you click it again , it would re-download the same song again
                                # In order to prevent this , in another part of the program-file , as soon as we click the download button we have given : Button.setEnabled(False)
                                # this command is used to disable to button's functionality until the song hs been downloaded .
                                # Now, in this program , At line-15 , at this point, the song has been downloaded so ,
                                # we have given : Button.setEnabled(True) ,  which reinstates the button's functionality back to it.
