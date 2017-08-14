function typeChanged(type){
    switch (type.value) {
        case "G":
            $("#id_datetime").addClass("hidden");
            $("#id_compose_post").removeClass("quiz");
            break;
        case "Q":
            $("#id_datetime").removeClass("hidden");
            $("#id_compose_post").addClass("quiz");
            break;
        case "A":
            $("#id_datetime").removeClass("hidden");
            $("#id_compose_post").addClass("quiz");
            break;
    
        default:
            break;
    }
}