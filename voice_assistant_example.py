"""
Voice Assistant Pipeline - Example Usage
=========================================

This example demonstrates how to use the voice_assistant_pipeline function
from the Speech-to-Speech LLM System.

Prerequisites:
    - All models must be loaded (Whisper, TinyLlama, SpeechT5)
    - An audio file with your question (.wav or .mp3)
"""

from IPython.display import Audio, display

# =============================================================================
# BASIC USAGE
# =============================================================================

# Simple one-line usage with your audio file
q, a, path = voice_assistant_pipeline("your_question.wav")

# Play the generated response
display(Audio(path, rate=16000))


# =============================================================================
# COMPLETE EXAMPLE WITH ERROR HANDLING
# =============================================================================

def run_voice_assistant_with_feedback(audio_file):
    """
    Run the voice assistant with detailed feedback.

    Args:
        audio_file: Path to your audio question file (.wav or .mp3)

    Returns:
        tuple: (question_text, answer_text, output_audio_path)
    """
    try:
        print("🎙️ Processing your question...")

        # Call the pipeline
        question, answer, output_path = voice_assistant_pipeline(audio_file)

        # Display results
        print("\n" + "="*60)
        print("CONVERSATION")
        print("="*60)
        print(f"👤 You asked: {question}")
        print(f"\n🤖 Assistant: {answer}")
        print("="*60)
        print(f"\n💾 Audio saved to: {output_path}")

        # Play the response
        print("\n🔊 Playing response...")
        display(Audio(output_path, rate=16000, autoplay=True))

        return question, answer, output_path

    except FileNotFoundError:
        print(f"❌ Error: Audio file '{audio_file}' not found.")
        print("   Please check the file path and try again.")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("   Make sure all models are loaded before running the pipeline.")


# =============================================================================
# EXAMPLE 1: Process a Single Question
# =============================================================================

# Replace with your actual audio file
audio_file = "my_question.wav"

# Run the pipeline
question, answer, audio_path = voice_assistant_pipeline(audio_file)

# Play the response
display(Audio(audio_path, rate=16000))


# =============================================================================
# EXAMPLE 2: Process Multiple Questions in a Loop
# =============================================================================

# List of audio files to process
audio_files = [
    "question1.wav",
    "question2.wav",
    "question3.wav"
]

# Process each question
results = []
for i, audio_file in enumerate(audio_files, 1):
    print(f"\n{'='*60}")
    print(f"Question {i}/{len(audio_files)}")
    print(f"{'='*60}")

    q, a, path = voice_assistant_pipeline(audio_file)
    results.append((q, a, path))

    print(f"Q: {q}")
    print(f"A: {a}\n")

# Play all responses
print("\n🎧 Playing all responses:")
for i, (q, a, path) in enumerate(results, 1):
    print(f"\nResponse {i}:")
    display(Audio(path, rate=16000))


# =============================================================================
# EXAMPLE 3: Save and Export Results
# =============================================================================

import json

def process_and_save(audio_file, output_json="results.json"):
    """Process audio and save results to JSON."""

    # Run pipeline
    question, answer, audio_path = voice_assistant_pipeline(audio_file)

    # Prepare results
    results = {
        "input_audio": audio_file,
        "question": question,
        "answer": answer,
        "output_audio": audio_path,
        "sample_rate": 16000
    }

    # Save to JSON
    with open(output_json, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"✅ Results saved to {output_json}")

    # Play audio
    display(Audio(audio_path, rate=16000))

    return results

# Usage
results = process_and_save("my_question.wav", "conversation_results.json")


# =============================================================================
# EXAMPLE 4: Batch Processing with Progress Tracking
# =============================================================================

from tqdm import tqdm  # For progress bar

def batch_process_audio_files(audio_files):
    """
    Process multiple audio files with progress tracking.

    Args:
        audio_files: List of audio file paths

    Returns:
        list: Results for each processed file
    """
    results = []

    print(f"📋 Processing {len(audio_files)} audio files...\n")

    for audio_file in tqdm(audio_files, desc="Processing"):
        try:
            q, a, path = voice_assistant_pipeline(audio_file)
            results.append({
                "file": audio_file,
                "question": q,
                "answer": a,
                "output": path,
                "status": "success"
            })
        except Exception as e:
            results.append({
                "file": audio_file,
                "error": str(e),
                "status": "failed"
            })

    # Print summary
    success_count = sum(1 for r in results if r["status"] == "success")
    print(f"\n✅ Successfully processed: {success_count}/{len(audio_files)}")

    return results

# Usage
files = ["q1.wav", "q2.wav", "q3.wav"]
batch_results = batch_process_audio_files(files)


# =============================================================================
# EXAMPLE 5: Integration with File Upload (Google Colab)
# =============================================================================

from google.colab import files
import os

def upload_and_process():
    """Upload audio file and process it."""

    # Upload file
    print("📁 Please upload your audio file:")
    uploaded = files.upload()

    if not uploaded:
        print("❌ No file uploaded.")
        return

    # Get filename
    audio_file = list(uploaded.keys())[0]
    print(f"✅ Uploaded: {audio_file}")

    # Process it
    q, a, path = voice_assistant_pipeline(audio_file)

    # Show results
    print("\n" + "="*60)
    print(f"👤 Question: {q}")
    print(f"🤖 Answer: {a}")
    print("="*60)

    # Play response
    display(Audio(path, rate=16000, autoplay=True))

    # Offer download
    print(f"\n📥 Download response audio:")
    files.download(path)

# Usage (in Google Colab)
# upload_and_process()


# =============================================================================
# QUICK REFERENCE
# =============================================================================

"""
QUICK USAGE:
-----------

1. Basic usage:
   >>> q, a, path = voice_assistant_pipeline("question.wav")
   >>> display(Audio(path, rate=16000))

2. What it returns:
   - q (str): Your transcribed question
   - a (str): The assistant's text answer
   - path (str): Path to the generated audio file (.wav)

3. Playing the audio:
   - In Jupyter/Colab: Audio(path, rate=16000)
   - With autoplay: Audio(path, rate=16000, autoplay=True)
   - Download in Colab: files.download(path)

4. Supported input formats:
   - .wav files (recommended)
   - .mp3 files
   - Sample rate: 16000 Hz works best

5. Expected latency:
   - ~10-20 seconds total (GPU)
   - ~30-60 seconds total (CPU)
"""
