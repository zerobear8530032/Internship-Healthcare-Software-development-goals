// Add your JavaScript here for interactivity

function logMood(mood) {
    // Function to log the user's mood
    alert('Mood logged: ' + mood);
}

// Example of adding an event listener to the mood wheel
document.querySelector('.mood-wheel').addEventListener('click', function(event) {
    const mood = event.target.getAttribute('data-mood');
    if (mood) {
        logMood(mood);
    }
});
