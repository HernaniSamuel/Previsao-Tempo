$(document).ready(function() {
    $('form').submit(function(event) {
        event.preventDefault();  // Impede o envio do formulário

        var cidade = $('#pesquisa').val();

        // Verificar se a cidade foi especificada
        if (!cidade) {
            $('#resultado').text('Cidade não especificada');
            return;
        }

        // Enviar a requisição ao servidor
        $.ajax({
            url: '/dados',
            type: 'GET',
            data: { pesquisa: cidade },
            dataType: 'json',
            success: function(response) {
                // Atualizar os elementos HTML com os dados da previsão
                $('#cidade').text(response.cidade);
                $('#estado').text(response.estado);
                $('#pais').text(response.pais);
                $('#hora').text(response.hora);
                $('#temperatura-atual').text(response.temperatura_atual);
                $('#descricao-tempo').text(response.descricao_tempo);
                $('#icone-tempo').attr('src', response.icone_tempo);
                $('#velocidade-vento').text(response.velocidade_vento);
                $('#direcao-vento').text(response.direcao_vento);
                $('#grau-vento').text(response.grau_vento);
                $('#umidade-ar').text(response.umidade_ar);
                $('#precipitacao').text(response.precipitacao);
                $('#temperatura-maxima').text(response.temperatura_maxima);
                $('#temperatura-minima').text(response.temperatura_minima);
                $('#descricao-geral').text(response.descricao_geral);
                $('#precipitacao-esperada').text(response.precipitacao_esperada);
                $('#indice-uv').text(response.indice_uv);
                $('#vento-maximo').text(response.vento_maximo);
                $('#visibilidade-prevista').text(response.visibilidade_prevista);
                $('#fases-lua').text(response.fases_lua);
            },
            error: function(error) {
                alert('Cidade não encontrada');
            }
        });
    });
});
