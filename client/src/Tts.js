import './Tts.css'
import React, { useState } from 'react';
function Tts() {
    const [paragraph, setParagraph] = useState('');
    const [voice, setVoice] = useState('');
    const [audioUrl, setAudioUrl] = useState('');
    const handleSubmit = async(event) => {
        event.preventDefault();
        console.log('Paragraph:', paragraph);
        console.log('Voice', voice);

        const response = await fetch('http://localhost:5001/return_tts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                text: paragraph,
                voice
            })
        })
        .catch(error => console.error('Error:', error));
        console.log(response)
        const audioBlob = await response.blob()
        const audioUrl = URL.createObjectURL(audioBlob);
        setAudioUrl(audioUrl);
        const audioElement = document.getElementById('audioPlayer')
        if(audioElement){
            audioElement.src = audioUrl;
        }
    }
    return (
      <div>
        <h1>TTS Generator</h1>  
        <form onSubmit={handleSubmit}>
          <label htmlFor="text">Enter Paragraph:</label><br />
          <textarea
            id="text"
            name="text"
            rows="4"
            cols="50"
            value={paragraph}
            onChange={(e) => setParagraph(e.target.value)}
          ></textarea><br />    
          <label htmlFor="voice">Voice (optional):</label>
          <input
            type="text"
            id="voice"
            name="voice"
            placeholder="en_us_006"
            value={voice}
            onChange={(e) => setVoice(e.target.value)}
          /><br />  
          <button type="submit">Generate TTS</button>
        </form>
        {audioUrl && (
             <div>
             <h2>Generated TTS</h2>
             <audio controls id ='audioPlayer'>
               <source src={audioUrl} type="audio/mpeg" />
               Your browser does not support the audio element.
             </audio>
           </div>
        )}
      </div>
    );
}


export default Tts;
