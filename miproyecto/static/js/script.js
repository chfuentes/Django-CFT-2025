// static/js/script.js

// ============================================
// CONFIGURACIÓN DE PARTICLES.JS
// ============================================
particlesJS("particles-js", {
    "particles": {
        "number": {
            "value": 80,
            "density": {
                "enable": true,
                "value_area": 800
            }
        },
        "color": {
            "value": "#ffffff"
        },
        "shape": {
            "type": "circle"
        },
        "opacity": {
            "value": 0.5,
            "random": false
        },
        "size": {
            "value": 3,
            "random": true
        },
        "line_linked": {
            "enable": true,
            "distance": 150,
            "color": "#ffffff",
            "opacity": 0.4,
            "width": 1
        },
        "move": {
            "enable": true,
            "speed": 2,
            "direction": "none",
            "random": false,
            "straight": false,
            "out_mode": "out",
            "bounce": false
        }
    },
    "interactivity": {
        "detect_on": "canvas",
        "events": {
            "onhover": {
                "enable": true,
                "mode": "repulse"
            },
            "onclick": {
                "enable": true,
                "mode": "push"
            },
            "resize": true
        },
        "modes": {
            "repulse": {
                "distance": 200,
                "duration": 0.4
            },
            "push": {
                "particles_nb": 4
            }
        }
    },
    "retina_detect": true
});

// ============================================
// FUNCIONES PARA MENSAJES (SWEETALERT2)
// ============================================
/**
 * Muestra un mensaje simple con SweetAlert2
 * @param {string} texto - El mensaje a mostrar
 */
function mensaje(texto) {
    Swal.fire({
        text: texto,
        icon: 'info',
        confirmButtonColor: '#667eea',
        confirmButtonText: 'Entendido'
    });
}

/**
 * Muestra un mensaje de éxito
 * @param {string} texto - El mensaje a mostrar
 */
function mensajeExito(texto) {
    Swal.fire({
        title: '¡Éxito!',
        text: texto,
        icon: 'success',
        confirmButtonColor: '#667eea',
        timer: 3000
    });
}

/**
 * Muestra un mensaje de error
 * @param {string} texto - El mensaje a mostrar
 */
function mensajeError(texto) {
    Swal.fire({
        title: 'Error',
        text: texto,
        icon: 'error',
        confirmButtonColor: '#667eea'
    });
}

// ============================================
// PROCESAR MENSAJES DE DJANGO
// ============================================
document.addEventListener('DOMContentLoaded', function() {
    // Buscar el contenedor de mensajes
    const messagesContainer = document.getElementById('django-messages');
    
    if (messagesContainer) {
        try {
            // Obtener los mensajes del atributo data
            const messages = JSON.parse(messagesContainer.getAttribute('data-messages'));
            
            // Mostrar cada mensaje
            messages.forEach(function(msg) {
                mensaje(msg);
            });
            
            // Remover el contenedor después de mostrar
            messagesContainer.remove();
        } catch (error) {
            console.error('Error procesando mensajes:', error);
        }
    }
});

// ============================================
// VISTA PREVIA DE IMAGEN EN FORMULARIOS
// ============================================
document.addEventListener('DOMContentLoaded', function() {
    // Buscar todos los inputs de tipo file
    const fileInputs = document.querySelectorAll('input[type="file"]');
    
    fileInputs.forEach(function(input) {
        input.addEventListener('change', function(e) {
            const file = e.target.files[0];
            
            if (file && file.type.startsWith('image/')) {
                const reader = new FileReader();
                
                reader.onload = function(e) {
                    // Buscar o crear contenedor de vista previa
                    let preview = input.parentElement.querySelector('.image-preview');
                    
                    if (!preview) {
                        preview = document.createElement('div');
                        preview.className = 'image-preview';
                        input.parentElement.appendChild(preview);
                    }
                    
                    // Mostrar imagen
                    preview.innerHTML = `
                        <img src="${e.target.result}" alt="Vista previa">
                        <button type="button" class="preview-remove" onclick="this.parentElement.remove(); document.querySelector('input[type=file]').value = '';">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                                <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z"/>
                            </svg>
                        </button>
                    `;
                };
                
                reader.readAsDataURL(file);
            }
        });
    });
});
