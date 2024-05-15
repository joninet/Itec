let listaAlumnos = [];

function obtenerLocalStorage(nombre){
    const mostrarJSON = localStorage.getItem(nombre);
    return nombre ? JSON.parse(mostrarJSON) : [];
}

function registroNotas() {
    const nombreAlumno = document.getElementById('nombre').value;
    const notaAlumno = document.getElementById('nota').value;

    const alumno = {
        nombre: nombreAlumno,
        nota: notaAlumno
    };
    if (listaAlumnos.length == 6){
        alert("Ya has ingresado el máximo de alumnos permitidos.");
        return false;
    }else if (parseFloat(alumno.nota) > 10){
        alert("la nota debe ser menor que 10");
        return false;
    }else {
        listaAlumnos.push(alumno);
        localStorage.setItem('listaAlumnos', JSON.stringify(listaAlumnos));

        alert("Ingreso correcto");

        document.getElementById('nombre').value = ''; 
        document.getElementById('nota').value = ''; 
        return false;

    }
}

function mostrarPromedios() {
    const mostrarJSON = localStorage.getItem('listaAlumnos');
    const listaAlumnos = JSON.parse(mostrarJSON);

    let notas = 0 ;
    for (let i = 0; i < listaAlumnos.length; i++) {
        notas += parseFloat(listaAlumnos[i].nota);
    }
    promedioAlumnos = notas / 6;

    document.getElementById('mostrar-promedios').innerHTML = "El promedio general es: " + promedioAlumnos;
    return false;
}

function mostrarNotaAlta(){
    const mostrarJSON = localStorage.getItem('listaAlumnos');
    const listaAlumnos = JSON.parse(mostrarJSON);
    
    let notaAlta = 0;
    let nombreAlumno = ""
    for (let i = 0; i <  listaAlumnos.length; i++){
        let notaParse = parseFloat(listaAlumnos[i].nota);
        if(notaParse > notaAlta) {
            notaAlta = notaParse
            nombreAlumno = listaAlumnos[i].nombre
        }
    }
    document.getElementById('mostrar-notaAlta').innerHTML = "La nota mas alta es: " + notaAlta + ", alumno: " + nombreAlumno;
    return false;
}

function mostrarNotaBaja(){
    const mostrarJSON = localStorage.getItem('listaAlumnos');
    const listaAlumnos = JSON.parse(mostrarJSON);
    
    let notaBaja = 10;
    let nombreAlumno = ""
    for (let i = 0; i <  listaAlumnos.length; i++){
        let notaParse = parseFloat(listaAlumnos[i].nota);
        if(notaParse < notaBaja) {
            notaBaja = notaParse
            nombreAlumno = listaAlumnos[i].nombre
        }
    }
    document.getElementById('mostrar-notaBaja').innerHTML = "La nota mas baja es: " + notaBaja + ", alumno: " + nombreAlumno;
    return false;
}
function mostrarAprobados(){
    const mostrarJSON = localStorage.getItem('listaAlumnos');
    const listaAlumnos = JSON.parse(mostrarJSON);

    let listaAprobados = "<ul>"
    for (let i = 0; i < listaAlumnos.length; i++) {
        let notaParse = parseFloat(listaAlumnos[i].nota);
        if (notaParse >= 5){
            listaAprobados += "<li>" + listaAlumnos[i].nombre + "</li>";
        }
    }
    listaAprobados += "</ul>"
    document.getElementById('mostrar-aprobados').innerHTML = "Lista de Aprobados: " + listaAprobados;
    return false;
}
function mostrarDesaprobados(){
    const mostrarJSON = localStorage.getItem('listaAlumnos');
    const listaAlumnos = JSON.parse(mostrarJSON);

    let listaDesaprobados = "<ul>"
    for (let i = 0; i < listaAlumnos.length; i++) {
        let notaParse = parseFloat(listaAlumnos[i].nota);
        if (notaParse < 5){
            listaDesaprobados += "<li>" + listaAlumnos[i].nombre + "</li>";
        }
    }
    listaDesaprobados+= "</ul>"
    document.getElementById('mostrar-desaprobados').innerHTML = "Lista de Desaprobados: " + listaDesaprobados;
    return false;
}