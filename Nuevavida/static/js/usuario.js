var habilitar = document.getElementById("btnSave").disabled = true;

function verificarPassword(){
    var pass1 = document.getElementById("password1").value;
    var pass2 = document.getElementById("password2").value;

    if((pass1 == "" || pass1 == null) && (pass2 == "" || pass2 == null)){
        console.log();
    } else {
        if(pass1 == pass2){
            habilitar = document.getElementById("btnSave").disabled = false;
        } else {
            pass1 = document.getElementById("password1").value = "";
            pass2 = document.getElementById("password2").value = "";
            alert("Las contraseñas no coinciden");
        }
    }
}

function verificar(){
    var pass1 = document.getElementById("password1").value;

    if(pass1.length < 8){
        pass1 = document.getElementById("password1").value = "";
        alert("Su contraseña debe tener minimo 8 caracteres");
    }
}