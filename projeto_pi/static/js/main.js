$(function() {
    $("#datepicker1").datepicker();

    $("#datepicker2").datepicker();

    $("#datepicker3").datepicker();

    $("#datepicker4").datepicker();

    $("#speed").selectmenu();
    
    $("#files").selectmenu();

    $("app1").selectmenu();
    
    $( "#number" )
        .selectmenu()
        .selectmenu("menuWidget")
        .addClass("overflow");
    
    $("#salutation").selectmenu();

});
function listar_aviso() {
     $("#tblAgendamentos tr:last").after("<tr>" +
        "<td>" + data + "</td>" +
        "<td>" + hora + "</td>" +
        "<td>" + pauta + "</td>" +
        "</tr>");
}
function incluir_aviso() {
    console.log('gravar_aviso()');
    //const data = $('#datepicker2').val();
    //const hora = $('#appt1').val();
    const ts_agenda =$('#datepicker2' + '#appt1').val();
    const pauta = $('#pauta_agenda3').text();
    // TODO: adicionar campo para pauta

    $("#tblAgendamentos tr:last").after("<tr>" +
        "<td>" + data + "</td>" +
        "<td>" + hora + "</td>" +
        "<td>" + pauta + "</td>" +
        "</tr>");
}

function editar_aviso() {
    $("#divEditarAviso").toggle();
}

function editar_ferias() {
    $("#divEditar_Ferias").toggle();
}

function listar_np_ferias() {
    console.log('tblFeriasAagendadas()');

    $("#divListarFerias").toggle();
}

function solicitar_ferias() {
    console.log('solicitar_ferias()');


    $("#divSolicitar_Ferias").toggle();
}
function editar_ferias() {
    $("#divEditar_Ferias").toggle();
}

function excluir_ferias() {
    $("#divExcluir_Ferias").toggle();
}

function gravar_ferias() {
    console.log('gravar_ferias()');

    const data_inicio = moment($('#datepicker4').val());
    const intervalo_ferias = parseInt($("#intervalo_ferias2").val());

    if (isNaN(intervalo_ferias)) {
        alert('Selecione qual será o período de férias');
        return false;
    }
    const data_fim = data_inicio.add(intervalo_ferias, 'days');

    return confirm("Férias agendadas de " + data_inicio.format('DD/MM/YYYY') + " até " + data_fim.format('DD/MM/YYYY') + ", confirma?")
}
