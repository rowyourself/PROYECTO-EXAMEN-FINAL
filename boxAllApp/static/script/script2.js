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


// Validaciones de formularioasdxd

    // Función para validar el número de teléfono según el formato chileno
function validarTelefono(telefono) {
        // Formato chileno: 9 dígitos comenzando con 9
        var regex = /^[9]\d{8}$/;
        return regex.test(telefono);
    }

    // Función para validar la fecha de nacimiento (mayores de edad)
function validarFechaNacimiento(fechaNacimiento) {
        var hoy = new Date();
        var fechaNac = new Date(fechaNacimiento);
        var edad = hoy.getFullYear() - fechaNac.getFullYear();
        var mes = hoy.getMonth() - fechaNac.getMonth();

        if (mes < 0 || (mes === 0 && hoy.getDate() < fechaNac.getDate())) {
            edad--;
        }

        return edad >= 18;
    }

    // Función para validar el formulario antes de enviarlo
document.getElementById('registroForm').addEventListener('submit', function(event) {
        var telefono = document.getElementById('id_telefono').value;
        var fechaNacimiento = document.getElementById('id_fecha_nacimiento').value;

        if (!validarTelefono(telefono)) {
            alert('Por favor, ingresa un número de teléfono válido (formato chileno)');
            event.preventDefault(); // Evita que el formulario se envíe
            return;
        }

        if (!validarFechaNacimiento(fechaNacimiento)) {
            alert('Debes ser mayor de 18 años para registrarte');
            event.preventDefault(); // Evita que el formulario se envíe
            return;
        }

        // Aquí puedes agregar más validaciones si es necesario

        // Si todas las validaciones son exitosas, el formulario se enviará normalmente
    });

    
 