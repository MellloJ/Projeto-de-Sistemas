
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

var form = $('#filterModal');

form.on('submit', function(e) {
    e.preventDefault();
    var formData = form.serialize();
    console.log(formData);
    $.ajax({
        type: 'GET',
        url: $('#filter_url').val(),
        data: formData,
    });
});