function openTab(evt, tabName) {
    var i, tabContent, tabButtons;

    // Ocultar todas las pestañas
    tabContent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabContent.length; i++) {
        tabContent[i].style.display = "none";
    }

    // Eliminar la clase "active" de todos los botones de pestañas
    tabButtons = document.getElementsByClassName("tab-button");
    for (i = 0; i < tabButtons.length; i++) {
        tabButtons[i].className = tabButtons[i].className.replace(" active", "");
    }

    // Mostrar la pestaña actual y añadir una clase "active" al botón que abrió la pestaña
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Mostrar la primera pestaña por defecto
document.addEventListener("DOMContentLoaded", function() {
    document.getElementsByClassName("tab-button")[0].click();
});


let direccionCount = 0;

function agregarDireccion() {
    direccionCount++;

    // Creamos un nuevo conjunto de campos de dirección
    const direccionHTML = `
        <div class="direccion">
            <label for="direccion${direccionCount}">Dirección ${direccionCount}:</label>
            <input type="text" id="direccion${direccionCount}" name="direccion${direccionCount}" required><br>
        </div>
    `;

    // Agregamos el HTML al contenedor de direcciones
    document.getElementById('direcciones-container').insertAdjacentHTML('beforeend', direccionHTML);
}


$('[id^="agregar-direccion-"]').click(function() {
    console.log("Se ejecutó el evento de clic");
    var idPaciente = $(this).attr('id').split('-')[2];
    $('#id-paciente').val(idPaciente);
    document.getElementById('agregarDireccionModal').style.display = 'block';
  });

// Función para cerrar el modal
function cerrarModal() {
    document.getElementById('modal-direccion').style.display = 'none';
}



// PADRES FORMULARIO
// Funciones para manejar el modal de ver direcciones
function abrirModalVerDirecciones() {
    document.getElementById('modal-direccion').style.display = 'block';
}

function CerrarModalVerDirecciones() {
    document.getElementById('modal-direccion').style.display = 'none';
}

function mostrarDirecciones() {
    document.querySelector('.modal-content').style.display = 'block';
  }

   // Función para abrir el modal
   function abrirModalEmbarazo() {
    document.getElementById('modal-embarazo-registro').style.display = 'block';
}

// Función para cerrar el modal
function cerrarModal() {
    document.getElementById('modal-embarazo-registro').style.display = 'none';
}

function confirmarEliminacion() {
    if (confirm("¿Estás seguro de eliminar este registro?")) {
      return true; // Envía el formulario
    } else {
      return false; // No envía el formulario
    }
  }

 // Seleccionar fila
$('.seleccionar-fila').on('change', function() {
    var idPaciente = $(this).val();
    var seleccionado = $(this).is(':checked');
  
    if (seleccionado) {
      // Abrir modal para agregar dirección
      $('#modal-direccion').show();
      // Asignar ID del paciente seleccionado a una variable
      $('#id-paciente-direccion').val(idPaciente);
    }
});
  
  function agregarDireccion() {
  
  }
