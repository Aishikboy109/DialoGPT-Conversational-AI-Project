import speech_recognition as sr


# {
#   "apikey": "IB4LHO5W1xtdxYsSUL6gsR4M6LMr2zc4EiGxcGyjMCyJ",
#   "iam_apikey_description": "Auto-generated for key 826a9b8c-cc9a-4bd7-936f-5f1e0957d90b",
#   "iam_apikey_name": "Service credentials-1",
#   "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
#   "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/5408618e9cae4c98b1d27928645f9292::serviceid:ServiceId-07eb31ef-e0d0-4a77-95ab-c3cbef540b30",
#   "url": "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/ffeaa3d2-ef8a-43ee-985c-05be423b853f"
# }






import speech_recognition as sr
# from ibm_watson import SpeechToTextV1
# import json

# r = sr.Recognizer()
# speech = sr.Microphone()
# speech_to_text = SpeechToTextV1(
#     iam_apikey = "IB4LHO5W1xtdxYsSUL6gsR4M6LMr2zc4EiGxcGyjMCyJ",
#     url = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/ffeaa3d2-ef8a-43ee-985c-05be423b853f"
# )
# with speech as source:
#     print("say something!!…")
#     audio_file = r.adjust_for_ambient_noise(source)
#     audio_file = r.listen(source)
# speech_recognition_results = speech_to_text.recognize(audio=audio_file.get_wav_data(), content_type='audio/wav').get_result()
# print(json.dumps(speech_recognition_results, indent=2))


def get_audio():
# use the audio file as the audio source
	r = sr.Recognizer()

	with sr.Microphone() as source:
	    print("Speak now : ")
	    # r.energy_threshold = 300
	    # r.adjust_for_ambient_noise(source)
	    r.adjust_for_ambient_noise(source, duration=0.2)
	    audio = r.listen(source)  # read the entire audio file

	# USERNAME = "826a9b8c-cc9a-4bd7-936f-5f1e0957d90b"
	# PASSWORD = "IB4LHO5W1xtdxYsSUL6gsR4M6LMr2zc4EiGxcGyjMCyJ"

	try:
	    return r.recognize_google(audio)
	except sr.UnknownValueError:
	    return "Could not understand audio"
	except sr.RequestError as e:
	    return "Error; {0}".format(e)


while True:
	print("Speak now")
	print(get_audio())