from flask import Flask, jsonify
app = Flask(__name__)

import spotilib

@app.route('/song')
def song():
    info = {
      'artist': spotilib.artist(),
      'song': spotilib.song()
    }
    return jsonify(**info)

@app.route('/next')
def action_next():
    spotilib.next()
    return "OK"

@app.route('/previous')
def previous():
    spotilib.previous()
    return "OK"

@app.route('/pause')
def pause():
    spotilib.pause()
    return "OK"

@app.route('/play')
def play():
    spotilib.play()
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
