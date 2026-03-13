import asyncio
import json

import numpy as np
import sounddevice as sd
import websockets

# Global variable to hold the latest breath intensity
current_intensity = 0.0


def audio_callback(indata, frames, time, status):
    """
    Called by sounddevice for each audio chunk.
    Updates the global current_intensity based on mic input volume.
    """
    global current_intensity

    if status:
        print("Audio status:", status)

    # Compute a simple volume measure (L2 norm of the buffer)
    volume = float(np.linalg.norm(indata))

    # Normalize a bit so values are in a more convenient range (~0–1+)
    # You can tweak this scaling factor based on your mic sensitivity
    scaled = volume * 10.0

    current_intensity = scaled


async def breath_stream(websocket):
    """
    For each connected websocket client, send the current breath intensity
    at a fixed interval.
    """
    try:
        while True:
            payload = {
                "breath": current_intensity
            }
            await websocket.send(json.dumps(payload))
            await asyncio.sleep(0.05)  # 20 updates per second
    except websockets.ConnectionClosed:
        # Client disconnected; just exit the loop
        pass


async def main():
    """
    Start the mic stream and WebSocket server.
    Visit index.html in your browser; it will connect to ws://localhost:8000.
    """
    # Start audio input stream (runs callbacks in a separate thread)
    with sd.InputStream(callback=audio_callback):
        print("Mic input stream started.")

        # Start WebSocket server
        async with websockets.serve(lambda ws: breath_stream(ws), "localhost", 8000):
            print("WebSocket server running on ws://localhost:8000")
            print("Press Ctrl+C to stop.")
            # Run forever
            await asyncio.Future()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nShutting down...")