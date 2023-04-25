/* todos los scripts  */
// 1) Función para ael puso del texto (loginpage)

$(document).ready(function(){
    (function pulse(){
        $('.text-pulse').fadeOut(1000).fadeIn(1000,pulse);
    })();
});

// 2) Función para ocultar y enseñar la contraseña

function myFunction(){
    var p= document.getElementById("password");
    if (p.type === "password"){
        p.type = "text";
    }else{
        p.type ="password"
    }
}

