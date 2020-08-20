import pyttsx3
import os

pyttsx3.speak("Welcome to my program")

while(True):
                    print("Chat with me with your requirements:",end=" ")
                    p=input()
                    if(("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) ) and ("chrome" in p):
                            pyttsx3.speak("Opening chrome ")
                            os.system("start chrome")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and (("notepad" in p) or ("text editor" in p)):
                            pyttsx3.speak("Opening notepad")
                            os.system("notepad")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and (("notepad" in p) and (("++" in p) or ("plus plus" in p))):
                            pyttsx3.speak("Opening notepad plus plus")
                            os.system("notepad++")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and ("brackets" in p):
                            pyttsx3.speak("Opening brackets")
                            os.system("brackets")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("create" in p)) and (("excel" in p) or ("sheets" in p) or ("database" in p)):
                            pyttsx3.speak("Opening excel sheets")
                            os.system("excel")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and (("power point" in p) or ("presentation" in p)):
                            pyttsx3.speak("Opening power point")
                            os.system("powerpnt")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and (("virtual box" in p) or ("redhat" in p)):
                            pyttsx3.speak("Opening virtual box")
                            os.system("VirtualBox")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and ("word" in p):
                            pyttsx3.speak("Opening microsoft word")
                            os.system("winword")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and ("onenote" in p):
                            pyttsx3.speak("Opening onenote")
                            os.system("onenote")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and (("pycharm" in p) or (("python" in p) and ("ide" in p))):
                            pyttsx3.speak("Opening pycharm")
                            os.system("pycharm64")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and ((("idle" in p) and ("python" in p)) or ("python shell" in p)):
                            pyttsx3.speak("opening python shell")
                            os.system("pythonw")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("play" in p) or ("start" in p)) and ("game" in p):
                            pyttsx3.speak("Opening games")
                            os.system("GameConsole-wt")           
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and (("internet" in p)  or ("search engine" in p)):
                            pyttsx3.speak("Opening ")
                            os.system("iexplore")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("create" in p)) and (("paint" in p) or ("drawing" in p)):
                            pyttsx3.speak("Opening paint")
                            os.system("mspaint")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("play" in p) or ("listen" in p)) and (("media player" in p) or ("music" in p) or ("songs" in p) ):
                            pyttsx3.speak("Opening media player")
                            os.system("wmplayer")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) ) and ("deluge" in p):
                            pyttsx3.speak("Opening deluge")
                            os.system("deluge")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) ) and ("home makeover" in p):
                            pyttsx3.speak("Opening home makeover game")
                            os.system("HomeMakeover-WT")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) ) and ("defender" in p):
                            pyttsx3.speak("Opening microsoft defender")
                            os.system("MSASCui")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) ) and (("Sublime" in p) or  ("text editor" in p)):
                            pyttsx3.speak("Opening sublime text editor")
                            os.system("sublime_text")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) ) and ("zoom" in p):
                            pyttsx3.speak("Opening zoom app")
                            os.system("zoom")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) ) and ("word" in p) and ("pad" in p):
                            pyttsx3.speak("wordpad")
                            os.system("wordpad")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) ) and  (("quick" in p) and ("assist" in p)):
                            pyttsx3.speak("Opening quick assist")
                            os.system("quickassist")
                    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) ) and  ("automation manager" in p):
                            pyttsx3.speak("Opening automation manager")
                            os.system("AUTMGR32")
                    elif ("exit" in p) or ("stop" in p):
                            pyttsx3.speak("Thank you")
                            break
                    else :
                            pyttsx3.speak("Sorry not found ")
                            print("Not support")
