import whisper
import os
import sys

def transcribe_video(video_path):
    # Check if file exists
    if not os.path.exists(video_path):
        print(f"File not found: {video_path}")
        return

    # Load Whisper model
    print("Loading Whisper model...")
    model = whisper.load_model("base")  # Try "medium" or "large" for better accuracy

    print(f"Transcribing: {video_path}")
    result = model.transcribe(video_path)

    # Save transcript to file
    transcript_text = result["text"]
    output_file = os.path.splitext(video_path)[0] + "_transcript.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(transcript_text)

    print(f"Transcription completed and saved to: {output_file}")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe_video.py <video_file_path>")
    else:
        transcribe_video(sys.argv[1])
