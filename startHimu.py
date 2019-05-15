from HIMU_MODULES import dataFilter as df
from HIMU_MODULES import dataMng as dm
import speech_recognition as sr


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
  # listen for 5 seconds and create the ambient noise energy level
  r.adjust_for_ambient_noise(source, duration=2)
  print("Connecting..") 
  os.system("clear")  
  print("Say something!")  
  audio = r.listen(source)



#sant = "Hello  there I'm jay from Humbingo bring me 4 piz with extra toping"    
sant = audio
userVoice = dm.makeList(sant)
 

FinalStat = "Ok, Now Just chill we will bring you " + str(df.filtNo(userVoice)) + " " + df.filtFood(userVoice) + " with " + df.filtExtra(userVoice)
print(FinalStat)








