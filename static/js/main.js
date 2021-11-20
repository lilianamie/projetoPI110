$(function() {
    $("#datepicker1").datepicker();

    $("#datepicker2").datepicker();

    $("#datepicker3").datepicker();

    $("#datepicker4").datepicker();

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
    $("#divEditarFerias").toggle();
}

function listar_ferias() {
    $("#divListarFerias").toggle();
}

function solicitar_ferias() {
    $("#divSolicitar_Ferias").toggle();
}
function editar_ferias() {
    $("#divEditar_Ferias").toggle();
}

function excluir_ferias() {
    $("#divExcluir_Ferias").toggle();
}

function gravar_aviso() {
    console.log('gravar_aviso()');

    const data = $('#datepicker2').val();
    const hora = $('#appt1').val();
    const pauta = $('#pauta_agenda3').text();
    // TODO: adicionar campo para pauta

    $("#tblAgendamentos tr:last").after("<tr>" +
        "<td>" + data + "</td>" +
        "<td>" + hora + "</td>" + 
        "<td>" + pauta + "</td>" +
        "</tr>");
}
function gravar_ferias() {
    console.log('gravar_ferias()');

    const data_inicio = $('#datepicker4').val();
    if (intervalo_ferias2 = 30){
        const data_fim = $('#datepicker4' + 30 ).val(moment().format());
    }
    else if (intervalo_ferias2 = 15){
        const data_fim = $('#datepicker4' + 15 ).val(moment().format());
    }
    else if (intervalo_ferias2 = 20){
        const data_fim = $('#datepicker4' + 15 ).val(moment().format());
    }
    else print('Selecione qual será o período de férias')
    

    $("#tblFeriasAagendadas tr:last").after("<tr>" +
        "<td>" +nome_func+ "</td>" +
        "<td>" + data_inicio + "</td>" + 
        "<td>" + data_fim + "</td>" +
        "</tr>");
}
