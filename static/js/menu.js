function toggleDropdown(dropdownId) {
    var dropdown = document.getElementById(dropdownId);
    if (dropdown.style.display === 'block') {
        dropdown.style.display = 'none';
    } else {
        var dropdowns = document.getElementsByClassName('dropdown__content');
        for (var i = 0; i < dropdowns.length; i++) {
            dropdowns[i].style.display = 'none';
        }
        dropdown.style.display = 'block';
    }
}

window.onclick = function(event) {
    if (!event.target.matches('.dropdown__button')) {
        var dropdowns = document.getElementsByClassName('dropdown__content');
        for (var i = 0; i < dropdowns.length; i++) {
            dropdowns[i].style.display = 'none';
        }
    }
}

function confirmLogout() {
    var confirmLogout = confirm("¿Desea cerrar la sesión?");
    if (confirmLogout) {
        document.forms[0].submit();
    }
}