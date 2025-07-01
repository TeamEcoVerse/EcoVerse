//Function
function startVoice(fieldId) {
  if (!('webkitSpeechRecognition' in window)) {
    alert('Your browser does not support voice input.');
    return;
  }

  const recognition = new webkitSpeechRecognition();
  recognition.lang = 'en-IN';
  recognition.start();

  recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    document.getElementById(fieldId).value = transcript;
  };

  recognition.onerror = function() {
    alert('Voice input failed or was aborted.');
  };
}
