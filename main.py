import os

def synthesize_text(text):
    directory = "D:\\Users\\Joseph\\Documents\\Sharethefreefun\\Developments\\Text-To-Speech\\"
    directory = os.getcwd()+"\\"
    
    from google.oauth2 import service_account
    credentials = service_account.Credentials.from_service_account_file(directory+'(service_acc)plated-shelter-344504-d9a09e301ab7.json')
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient(credentials=credentials)
    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        #language_code="en-US",
        language_code="cmn-CN",
        #name="en-US-Standard-C",
        name="cmn-CN-Wavenet-A",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open(directory+"output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('完成!请查看"output.mp3"')


while True:
    try:
        text = input("文字: ")
        if text == "c":
            break
        synthesize_text(text)
    except Exception as e:
        print(str(e))
        pass
