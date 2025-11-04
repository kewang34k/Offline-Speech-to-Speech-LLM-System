"""
Simple Voice Assistant Example
================================

Minimal example showing how to use the voice_assistant_pipeline.
"""

from IPython.display import Audio, display

# =============================================================================
# MINIMAL EXAMPLE
# =============================================================================

# Step 1: Call the pipeline with your audio file
question, answer, audio_path = voice_assistant_pipeline("your_question.wav")

# Step 2: Play the generated response
display(Audio(audio_path, rate=16000))


# =============================================================================
# WITH CONSOLE OUTPUT
# =============================================================================

# Process your audio
q, a, path = voice_assistant_pipeline("your_question.wav")

# See what was transcribed and answered
print(f"You asked: {q}")
print(f"Assistant: {a}")

# Play the audio response
display(Audio(path, rate=16000))


# =============================================================================
# ONE-LINER (after pipeline is defined)
# =============================================================================

display(Audio(voice_assistant_pipeline("your_question.wav")[2], rate=16000))
