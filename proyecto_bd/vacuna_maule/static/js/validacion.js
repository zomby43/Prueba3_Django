function validar()
{
    nombre = document.formulario.txt_t_nombre.value;
    appaterno = document.formulario.txt_t_appaterno.value;
    apmaterno = document.formulario.txt_t_apmaterno.value;
    rut = document.formulario.txt_t_rut.value;
    telefono = document.formulario.txt_t_telefono.value;

    if (nombre == "")
    {
        alert("Debe ingresar el nombre");
        document.formulario.txt_t_nombre.focus();
        return false;
    }

    if (appaterno == "")
    {
        alert("Debe ingresar el apellido paterno");
        document.formulario.txt_t_appaterno.focus();
        return false;
    }
    if (apmaterno == "")
    {
        alert("Debe ingresar el apellido materno");
        document.formulario.txt_t_apmaterno.focus();
        return false;
    }
    if (rut == "")
    {
        alert("Debe ingresar el rut");
        document.formulario.txt_t_rut.focus();
        return false;
    }
    if (rut.charAt(8) != "-")
    {
        alert("El guion debe ir antes del digito verificador")
        return false
    }
    if (telefono == "")
    {
        alert("Debe ingresar el telefono");
        document.formulario.txt_t_telefono.focus();
        return false;
    }
    if (telefono.length<9){
        alert("Telefono debe contener 9 caracteres")
        return false
    }

    else {
    document.formulario.action = "/ingresar_trabajador_lista/"
    document.formulario.submit() = true;
    alert("Trabajador ingresado correctamente");
    }
}