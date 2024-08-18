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

  
// Función para abrir el modal
function abrirModalEmbarazo() {
    document.getElementById('modal-embarazo-registro').style.display = 'block';
}

// Función para cerrar el modal
function cerrarModal() {
    document.getElementById('modal-embarazo-registro').style.display = 'none';
}
