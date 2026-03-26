import csv
import asyncio
import websockets
import json
import webbrowser
import os
import git_cloner as miner
import processor

PORT = 8080 
words_found = []

async def send_to_d3(websocket, words):
    if words:
        await websocket.send(json.dumps(words))

async def main_loop(websocket):
    global words_found
    
    with open('repos.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for fila in reader:
            if not fila: continue
            url = fila[0].strip()
            
            if miner.clone_repo(url):
                
                new_words = processor.process_directory(miner.TEMP_DIR)
                words_found.extend(new_words)
                
                while len(words_found) >= 100:
                    batch = words_found[:100]
                    await send_to_d3(websocket, batch)
                    words_found = words_found[100:]
                    await asyncio.sleep(1)
                
                miner.cleanup()
    
    if words_found:
        await send_to_d3(websocket, words_found)

async def start_server():
    
    async with websockets.serve(main_loop, "0.0.0.0", PORT):
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(start_server())
    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario.")