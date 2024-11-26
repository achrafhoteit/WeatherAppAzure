document.getElementById('weather-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const city = document.getElementById('city').value;
    const resultDiv = document.getElementById('weather-result');
    resultDiv.innerHTML = 'Loading...';

    try {
        const response = await fetch(`/api/weather?city=${city}`);
        const data = await response.json();

        if (response.ok) {
            resultDiv.innerHTML = `
                <h2>Weather in ${data.city}</h2>
                <p>Temperature: ${data.temperature}°C</p>
                <p>Humidity: ${data.humidity}%</p>
                <p>Description: ${data.description}</p>
            `;
        } else {
            resultDiv.innerHTML = `<p>${data.error}</p>`;
        }
    } catch (error) {
        resultDiv.innerHTML = '<p>An error occurred. Please try again.</p>';
    }
});
