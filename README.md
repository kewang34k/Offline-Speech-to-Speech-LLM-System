# Offline Speech-to-Speech LLM System

A complete educational project for building an end-to-end voice assistant pipeline that runs entirely offline in Google Colab.

## Overview

This project demonstrates how to build a fully functional speech-to-speech AI system that:
1. Records or uploads audio (your question)
2. Transcribes speech to text using **OpenAI Whisper**
3. Generates intelligent responses using a local **LLM (TinyLlama)**
4. Synthesizes the answer back to speech using **Microsoft SpeechT5**
5. Plays back the generated audio response

**Key Feature:** Everything runs locally without requiring cloud APIs or external services!

## Project Structure

```
├── README.md                                                    # This file
├── Whisper_Hands_On_Notebook_Dr_Fouad_Bousetouane.ipynb       # Tutorial: Speech-to-Text
├── Hands_On_TTS_with_SpeechT5_Dr_Fouad_Bousetouane.ipynb      # Tutorial: Text-to-Speech
└── Speech_to_Speech_LLM_System_Complete.ipynb                 # Complete voice assistant pipeline
```

## Notebooks

### 1. Speech_to_Speech_LLM_System_Complete.ipynb ⭐ **[MAIN ASSIGNMENT]**

**Complete end-to-end voice assistant implementation**

This is the main deliverable that integrates all components:

**Features:**
- ✅ Audio upload and visualization (waveforms, Mel spectrograms)
- ✅ Whisper speech recognition (multilingual, robust)
- ✅ TinyLlama LLM reasoning (1.1B parameter chat model)
- ✅ SpeechT5 text-to-speech synthesis (natural voice)
- ✅ Complete pipeline: Audio → Text → Reasoning → Audio
- ✅ Bonus: Custom speaker embedding extraction (voice cloning)
- ✅ Bonus: Interactive text-based interface
- ✅ Detailed documentation and reflections

**What You'll Learn:**
- End-to-end audio processing pipeline
- Speech recognition with Transformer models
- LLM inference and prompt engineering
- Text-to-speech synthesis
- Audio visualization techniques

**Perfect for:** Week 6 assignment submission, learning voice AI fundamentals

---

### 2. Whisper_Hands_On_Notebook_Dr_Fouad_Bousetouane.ipynb

**Tutorial: Speech-to-Text with OpenAI Whisper**

Learn how to transcribe audio using Whisper:
- Load and preprocess audio files
- Generate Mel spectrograms
- Perform speech recognition
- Visualize audio features

**Models:** Whisper (tiny, base, small, medium, large)

---

### 3. Hands_On_TTS_with_SpeechT5_Dr_Fouad_Bousetouane.ipynb

**Tutorial: Text-to-Speech with SpeechT5**

Learn how to generate natural speech from text:
- Load SpeechT5 models and vocoder (HifiGan)
- Create speaker embeddings
- Synthesize speech from text
- Control voice characteristics

**Models:** Microsoft SpeechT5 + HifiGan vocoder

---

## Quick Start

### 1. Open in Google Colab

Click on any notebook and upload it to [Google Colab](https://colab.research.google.com/)

### 2. Run the Complete Pipeline

For the full voice assistant experience:

```python
# 1. Upload the Speech_to_Speech_LLM_System_Complete.ipynb
# 2. Run all cells sequentially (Runtime → Run all)
# 3. Upload your audio file when prompted
# 4. Listen to the AI-generated response!
```

### 3. Requirements

All dependencies are installed automatically in the notebooks:
- `openai-whisper` - Speech recognition
- `transformers` - LLM and TTS models
- `torch` - Deep learning framework
- `librosa` - Audio processing
- `soundfile` - Audio I/O
- `datasets` - Speaker embeddings
- `accelerate` - Model loading
- `sentencepiece` - Tokenization

**Hardware:**
- Recommended: GPU (free tier Colab works!)
- Minimum: CPU (slower but functional)
- RAM: 12+ GB recommended

## Technologies Used

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Speech Recognition** | OpenAI Whisper | Audio → Text transcription |
| **Language Model** | TinyLlama-1.1B-Chat | Reasoning and response generation |
| **Text-to-Speech** | Microsoft SpeechT5 | Text → Audio synthesis |
| **Vocoder** | HifiGan | High-quality waveform generation |
| **Audio Processing** | LibROSA | Mel spectrograms, visualization |
| **Deep Learning** | PyTorch | Model inference |
| **Model Hub** | HuggingFace Transformers | Pre-trained models |

## Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   SPEECH-TO-SPEECH PIPELINE                 │
└─────────────────────────────────────────────────────────────┘

1. INPUT AUDIO (Your Question)
   ↓
   [Load at 16 kHz, visualize waveform + Mel spectrogram]
   ↓

2. SPEECH-TO-TEXT (Whisper)
   ↓
   [Transcribe audio → text]
   ↓

3. LANGUAGE MODEL REASONING (TinyLlama)
   ↓
   [Process question → Generate answer]
   ↓

4. TEXT-TO-SPEECH (SpeechT5 + HifiGan)
   ↓
   [Synthesize text → speech audio]
   ↓

5. OUTPUT AUDIO (AI Response)
   [Save as .wav file, play in notebook]
```

## Performance Metrics

| Stage | Latency (GPU) | Latency (CPU) | Quality |
|-------|---------------|---------------|---------|
| Audio Loading | < 1s | < 1s | N/A |
| Whisper STT | 2-5s | 5-15s | ⭐⭐⭐⭐⭐ |
| LLM Reasoning | 3-6s | 10-30s | ⭐⭐⭐⭐ |
| TTS Synthesis | 4-8s | 8-20s | ⭐⭐⭐⭐⭐ |
| **Total Pipeline** | **10-20s** | **25-65s** | **⭐⭐⭐⭐** |

## Assignment Deliverables

For the Week 6 assignment, submit:

1. **The complete notebook:** `Speech_to_Speech_LLM_System_Complete.ipynb`
2. **All required components:**
   - ✅ Audio upload & visualization
   - ✅ Whisper transcription
   - ✅ LLM reasoning
   - ✅ TTS synthesis
   - ✅ Playback and file saving
3. **Reflections:** Markdown cells documenting:
   - What worked
   - What failed
   - Latency observations
   - Quality assessment
4. **Bonus features (optional):**
   - Custom speaker embedding extraction
   - Interactive text interface

## Example Use Cases

### Educational Applications
- Learn speech AI fundamentals
- Understand audio signal processing
- Experiment with Transformer models
- Build voice assistant prototypes

### Research Applications
- Test speech recognition robustness
- Compare TTS voice quality
- Evaluate LLM response quality
- Prototype multilingual voice systems

### Fun Projects
- Build a personal voice assistant
- Create voice-based Q&A systems
- Experiment with voice cloning
- Interactive storytelling

## Troubleshooting

### Out of Memory?
- Use smaller models (Whisper tiny, DistilGPT2)
- Enable model quantization
- Clear GPU cache: `torch.cuda.empty_cache()`

### Slow Inference?
- Ensure GPU is enabled (Runtime → Change runtime type → GPU)
- Reduce `max_new_tokens` for LLM
- Use FP16 precision on GPU

### Poor Audio Quality?
- Check input audio sample rate (should be 16 kHz)
- Try different speaker embeddings
- Ensure clean audio input (minimal background noise)

### Repetitive LLM Responses?
- Increase `repetition_penalty` (1.2 → 1.5)
- Adjust `temperature` (0.7 → 0.8)
- Modify system prompt for specific instructions

## Future Improvements

- [ ] Add real-time streaming mode
- [ ] Implement conversation history/context
- [ ] Support multiple languages
- [ ] Add emotion detection
- [ ] Create Gradio web interface
- [ ] Optimize with ONNX/TensorRT
- [ ] Fine-tune models on custom data

## Credits

**Created by:** Dr. Fouad Bousetouane
**Course:** Advanced AI - Week 6 Assignment
**Topic:** Speech Processing and Voice AI

## License

Educational use only. Models are subject to their respective licenses:
- Whisper: MIT License
- TinyLlama: Apache 2.0
- SpeechT5: MIT License

## References

- [OpenAI Whisper](https://github.com/openai/whisper)
- [TinyLlama](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [Microsoft SpeechT5](https://huggingface.co/microsoft/speecht5_tts)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers)
- [LibROSA Documentation](https://librosa.org/)

---

**Ready to build your voice assistant? Start with `Speech_to_Speech_LLM_System_Complete.ipynb`! 🎙️🤖🔊**