from gtts import gTTS

# Testo da convertire
text = "Adotta un marino. Adottalo a distanza. "
text += "Potrai pagarli gli studi musicali, le sue rassegne organistiche."
text += "In cambio lui ti scriverà nelle varie festività per salutarti e chiedere tue notizie. "
text += "Magari ti chiederà anche dei soldi"
text += "Se vuoi adottare un marino chiama il numero 666 - 666 - 6 6 6"
text += "Chiama ora!"
text += "Chiama ora! un Marino ti aspetta"

# Stalva l'audio come file mp3
tts.save("output.mp3")
print("File MP3 generato con successo")