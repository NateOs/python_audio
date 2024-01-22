""" record system audio output"""

import pyaudio
import wave


def record_system_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output_sys.wav"

    p = pyaudio.PyAudio()

    # Open the default input device (usually the microphone)
    stream_in = p.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=RATE,
                       input=True,
                       frames_per_buffer=CHUNK)

    # Open the default output device (loopback)
    stream_out = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True,
                        frames_per_buffer=CHUNK)

    print("* recording system audio output")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        try:
            data = stream_in.read(CHUNK)
            frames.append(data)
            stream_out.write(data)
        except IOError as ex:
            if ex[1] != pyaudio.paInputOverflowed:
                raise

    print("* done recording")

    stream_in.stop_stream()
    stream_in.close()

    stream_out.stop_stream()
    stream_out.close()

    p.terminate()

    # Save the recorded audio to a WAV file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def record_agent_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    # Open the default input device (usually the microphone)
    stream_in = p.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=RATE,
                       input=True,
                       frames_per_buffer=CHUNK)

    # Open the default output device (loopback)
    stream_out = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True,
                        frames_per_buffer=CHUNK)

    print("* recording agent audio output")

    frames = []

""" create function to trigger both recordings, speaker and agent channels probably async """
""" use python library to overlap resulting channels and store to file """


def record_audio():
    record_agent_audio()
    record_system_audio()

record_audio()