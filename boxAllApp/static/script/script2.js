async function fetchTime() {
    try {
        const response = await fetch('http://worldtimeapi.org/api/ip');
        const data = await response.json();
        return data;
    } catch (error) {
        console.log('Error fetching time data:', error);
        return null;
    }
}

function updateClock() {
    fetchTime().then(data => {
        if (data) {
            const timeString = data.datetime.substr(11, 8);
            document.getElementById('current-time').textContent = `Hora: ${timeString}`;
            document.getElementById('city').textContent = `Ciudad: ${data.timezone.split('/')[1]}`;
        } else {
            document.getElementById('current-time').textContent = 'Error fetching time data';
        }
    });
}

// Actualizar la hora cada segundo
setInterval(updateClock, 1000);

// Mostrar la hora actual al cargar la página
updateClock();