function validarPlan(){
    var plan = document.getElementById("idUsuario").selectedOptions[0].innerText;
    plan = plan.split(":")[1];
    if(plan == "Individual"){
        alert("No puede agregar beneficiarios a un plan Individual");
        document.getElementById("idUsuario").value = 0;
    }
}