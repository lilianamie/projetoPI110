$(function() {
    $("#datepicker1").datepicker();

    $("#datepicker2").datepicker();

    $("#datepicker3").datepicker();

    $("#speed").selectmenu();
    
    $("#files").selectmenu();
    
    $( "#number" )
        .selectmenu()
        .selectmenu("menuWidget")
        .addClass("overflow");
    
    $("#salutation").selectmenu();

});

function incluir_aviso() {
    $("#divIncluirAviso").toggle();    
}

function editar_aviso() {
    $("#divEditarAviso").toggle();    
}

function editar_ferias() {
    $("#divEditar_Ferias").toggle();
}

function listar_ferias() {
    $("#divListar_Ferias").toggle();
}

function solicitar_ferias() {
    $("#divSolicitar_Ferias").toggle();
}

function gravar_aviso() {
    console.log('gravar_aviso()');

    const data = $('#datepicker1').val();
    const hora = $('#appt1').val();
    const pauta = $( 'pauta_agenda3').val();
    // TODO: adicionar campo para pauta

    $("#tblAgendamentos tr:last").after("<tr><td>" + data + "</td><td>" + hora + "</td></tr>" + pauta_agenda3 + "</td></tr>");

   


}