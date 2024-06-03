let temperature = 19; // Initial temperature value
let humidity = 50; // Initial humidity value

function updateValues() {
    document.getElementById('temperature').textContent = temperature;
    document.getElementById('humidity').textContent = humidity;
}

function controlAnimation() {
    const water = document.getElementById('water');
    if (temperature < 20) {
        water.style.height = '100px'; // Set height to show water stream
    } else {
        water.style.height = '0'; // Hide water stream
    }
}

updateValues();
controlAnimation();

// Simulate changing temperature over time
setInterval(() => {
    const randomChoice = Math.round(Math.random()); // 0 or 1
    temperature = (randomChoice === 0) ? 21 : 19;
    humidity = Math.floor(Math.random() * 101); // Random number between 0 and 100 for humidity

    updateValues();
    controlAnimation();

    // Additional logic to stop animation if temperature exceeds 24 degrees
    if (temperature > 24) {
        document.getElementById('water').style.height = '0'; // Stop water stream
    }
}, 3000);