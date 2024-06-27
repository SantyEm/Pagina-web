// Función para alternar la visibilidad del dropdown
function toggleDropdown(dropdownId) {
    var dropdown = document.getElementById(dropdownId);
    dropdown.classList.toggle("show"); // Toggle añade o quita la clase 'show'
}


// Función para cerrar todos los dropdowns al hacer clic fuera de ellos
window.onclick = function(event) {
    if (!event.target.matches('.dropdown__button')) {
        var dropdowns = document.getElementsByClassName('dropdown__content');
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}



// Función para confirmar el cierre de sesión (si es necesario)
function confirmLogout() {
    var confirmLogout = confirm("¿Desea cerrar la sesión?");
    if (confirmLogout) {
        document.forms[0].submit(); // Envía el formulario de cierre de sesión
    }
}

