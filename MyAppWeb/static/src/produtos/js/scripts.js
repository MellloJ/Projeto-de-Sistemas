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

    console.log('Dados do filtro:', JSON.stringify(data));

    Unicorn.call('produtos_unicorn', 'filter', JSON.stringify(data));
});
// end

// Botoes de categoria do index
$('.index-categoria-button').on('click', function() {
    var categoria = $(this).data('categoria');
    var data = {
        categoria: categoria
    };

    Unicorn.call('produtos_unicorn', 'filter', JSON.stringify(data));
})

// end

// Modo de edição
let editMode = false;

$('#edit-mode-toggle').on('click', function () {
    editMode = !editMode;
    if (editMode) {
        $(this).removeClass('bg-orange-400').addClass('bg-orange-500');
        $('.produtos-card').addClass('ring-4 ring-orange-300');
    } else{
        $(this).removeClass('bg-orange-500').addClass('bg-orange-400');
        $('.produtos-card').removeClass('ring-4 ring-orange-300');
    }
});


$('.edit-item-btn').on('click', function () {
    if (editMode) {
        const itemId = $(this).data('id');
        editar(itemId);
    }
});

function editar(itemId) {

    const form = $('#editModal');
    const modal = new Modal(document.getElementById('editModal'));

    $.ajax({
        url: `/produtos/api/editar/${itemId}`,
        method: 'GET',
        success: function(data) {
            form.find('#nome').val(data.nome);
            form.find('#descricao').val(data.descricao);
            form.find('#categoria').val(data.categoria);
            form.find('#marca').val(data.marca);
            form.find('#preco_unitario').val(data.preco_unitario);
            form.find('#qtd_estoque').val(data.qtd_estoque);
            form.find('#codigo_barras').val(data.codigo_barras);
        },
        error: function(xhr, status, error) {
            console.error('Erro ao buscar os dados do item:', error);
        }
    });

    modal.show();

    form.find('[data-modal-toggle="editModal"]').off('click').on('click', function () {
        modal.hide();
    });

    form.off('submit').on('submit', function (e) {
        e.preventDefault();

        const formData = {
            nome: form.find('#nome').val(),
            descricao: form.find('#descricao').val(),
            categoria: form.find('#categoria').val(),
            marca: form.find('#marca').val(),
            preco_unitario: form.find('#preco_unitario').val(),
            qtd_estoque: form.find('#qtd_estoque').val(),
            codigo_barras: form.find('#codigo_barras').val()
        };

        // const accessToken = document.cookie
        //     .split('; ')
        //     .find(row => row.startsWith('access_token='))
        //     ?.split('=')[1];

        // if (!accessToken) {
        //     console.error('Token de autenticação não encontrado. Faça login para continuar.');
        //     return;
        // }

        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const accessToken = document.cookie

        console.log('Access Token:', accessToken);
        console.log('CSRF Token:', csrfToken);
       

        $.ajax({
            url: `/produtos/api/editar/${itemId}`,
            method: 'PUT',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            xhrFields: {
                withCredentials: true  // Envia o cookie automaticamente
            },
            data: formData,
            success: function() {
                modal.hide();
                Unicorn.call('produtos_unicorn', 'filter', 'reset');
            },
            error: function(xhr, error) {
            if (xhr.status === 401) {
                console.error('Não autorizado. Verifique o token de autenticação.');
            } else {
                console.error('Erro ao editar o item:', error);
            }
            }
        });
    });
}

// end