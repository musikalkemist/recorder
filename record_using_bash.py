import subprocess

def record_using_bash(meeting_code):
    record_command = f"parec -d alsa_output.pci-0000_00_1f.3.analog-stereo.monitor --file-format=wav {meeting_code}.wav"
    print(subprocess.run([record_command], capture_output=True))


def main():
    meeting_code = "aabbcc"
    record_using_bash(meeting_code)

if __name__ == "__main__":
    main()