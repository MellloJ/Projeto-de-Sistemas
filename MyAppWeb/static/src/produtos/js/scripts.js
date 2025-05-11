// Troca o valor do campo de input para o campo de range

var preco_min = $('#preco-min');
var preco_max = $('#preco-max');

var preco_min_input = $('#preco-min-input');
var preco_max_input = $('#preco-max-input');

preco_min.on('change', function() {
    preco_min_input.val($(this).val());

    preco_max.attr('min', $(this).val());
    preco_max_input.attr('min', $(this).val());

    if (parseFloat($(this).val()) >= parseFloat(preco_max.val())) {
        preco_max.val($(this).val()).trigger('change');
    }
});

preco_min_input.on('change', function() {
    preco_min.val($(this).val());
    
    preco_max.attr('min', $(this).val());
    preco_max_input.attr('min', $(this).val());


    if (parseFloat($(this).val()) >= parseFloat(preco_max.val())) {
        preco_max.val($(this).val()).trigger('change');
    }
});


preco_max.on('change', function() {
    preco_max_input.val($(this).val());
});

preco_max_input.on('change', function() {
    preco_max.val($(this).val());
});

// end

// Filtro da tela de produtos
var form = $('#filterModal');

form.on('submit', function(e) {
    e.preventDefault();

    var categoria = $('#categoria').val();
    var preco_min = $('#preco-min').val();
    var preco_max = $('#preco-max').val();
    var rating = $('input[name="rating"]:checked').val();

    var data = {
        categoria: categoria,
        preco_min: preco_min,
        preco_max: preco_max,
        rating: rating
    };

    Unicorn.call('produtos_unicorn', 'filter', JSON.stringify(data));
});
// end

('.index-categoria-button').on('click', function() {
    var categoria = $(this).data('categoria');
    var data = {
        categoria: categoria
    };

    Unicorn.call('produtos_unicorn', 'filter', JSON.stringify(data));
})