## Breathing Harmonium

Breath‑controlled harmonium: a mic‑driven Python backend with a browser piano that responds to your breathing.

This project turns your microphone into virtual bellows. Python listens to the mic, streams a continuous **breath intensity** value over WebSockets, and a Web Audio–powered front end uses that intensity to shape the volume of a harmonium‑like synth with playable piano keys.

### Features

- **Breath‑driven dynamics**: the harder you breathe into the mic, the louder and more present the sound.
- **WebSocket bridge**: Python + `sounddevice` compute breath intensity and send it in real time to the browser.
- **Web Audio harmonium**: layered, slightly detuned oscillators filtered into a reed‑style tone.
- **On‑screen piano**: clickable white and black keys with clear visual feedback.
- **Computer keyboard mapping**: play notes from your QWERTY keyboard while breath controls volume.

### Controls

- **Breath**: speak or breathe into your microphone to control volume.
- **White keys**
  - Left **Shift** → C
  - `Z` → D
  - `C` → E
  - `V` → F
  - `N` → G
  - `,` (comma) → A
  - `/` → B
- **Black keys (sharps)**
  - `` ` `` (backtick, under Escape) → C#
  - `X` → D#
  - `B` → F#
  - `M` → G#
  - `.` (period) → A#

You can also click any key with the mouse to toggle it on/off.

### Tech stack

- **Backend**: Python, `sounddevice`, `numpy`, `websockets`
- **Frontend**: HTML/CSS, vanilla JS, WebSockets, Web Audio API

### Getting started

1. **Clone the repo**

```bash
git clone https://github.com/Sapan-Byndla/Breathing-Harmonium.git
cd Breathing-Harmonium
```

2. **Install Python dependencies**

```bash
pip install sounddevice numpy websockets
```

3. **Run the Python backend (mic + WebSocket)**

```bash
python Breathing-Harmonium.py
```

You should see:

```text
Mic input stream started.
WebSocket server running on ws://localhost:8000
Press Ctrl+C to stop.
```

4. **Serve the frontend**

In a second terminal, from the same folder:

```bash
python -m http.server 5500
```

Then open in your browser:

```text
http://localhost:5500/index.html
```

5. **Play**

- Allow microphone access in the browser when prompted.
- Press one or more mapped keys (or click on the piano) to start notes.
- Breathe into the mic to swell the sound like real bellows.

### Notes and ideas

- The breath‑to‑volume mapping and synth tone are intentionally simple and easy to tweak.
- Future ideas: scale/chord presets for Indian classical ragas, visualizations of airflow, recording/looping, MIDI output, or integration with hardware breath controllers.


