function validarFormulario() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    
    var usuario = "joninet"
    var contraseña = "1234"
    
    if (username === usuario && password === contraseña) {
        alert("Inicio de sesión exitoso");
        return true;
    } else if (username === "" && password === ""){
        var errorMsg = document.getElementById('error-msg');
        errorMsg.textContent = "No pueden existir campos vacios";
        return false;
    } else {
        var errorMsg = document.getElementById('error-msg');
        errorMsg.textContent = "Nombre de usuario o contraseña incorrectos";
        return false;
    }
}