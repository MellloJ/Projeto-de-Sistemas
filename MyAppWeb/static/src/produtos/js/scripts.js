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
        $('.produtos-card, .categoria-card').addClass('ring-4 ring-orange-300').find('img').addClass('cursor-pointer');
    } else{
        $(this).removeClass('bg-orange-500').addClass('bg-orange-400');
        $('.produtos-card, .categoria-card').removeClass('ring-4 ring-orange-300').find('img').removeClass('cursor-pointer');
    }
});

function resetEditMode() {
    editMode = false;
    $('#edit-mode-toggle').removeClass('bg-orange-500')
    $('#edit-mode-toggle').addClass('bg-orange-400');
    $('.produtos-card').removeClass('ring-4 ring-orange-300').find('img').removeClass('cursor-pointer');
}

$('.edit-item-btn').on('click', function () {
    if (editMode) {
        const itemId = $(this).data('id');
        editar(itemId);
    }
});

function editar(itemId) {

    const form = $('#editProdutos');
    const modal = new Modal(document.getElementById('editProdutos'));

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

    form.find('[data-modal-toggle="editProdutos"]').off('click').on('click', function () {
        modal.hide();
    });

    form.off('submit').on('submit', function (e) {
        e.preventDefault();

        const formData = new FormData()

        formData.append('id', itemId);
        formData.append('nome', form.find('#nome').val());
        formData.append('descricao', form.find('#descricao').val());
        formData.append('categoria', form.find('#categoria').val());
        formData.append('marca', form.find('#marca').val());
        formData.append('preco_unitario', form.find('#preco_unitario').val());
        formData.append('qtd_estoque', form.find('#qtd_estoque').val());
        formData.append('codigo_barras', form.find('#codigo_barras').val());

        const imagem = form.find('#imagem').prop('files')[0];
        if (imagem) {
            formData.append('imagem', imagem);
        }

        $.ajax({
            url: `/produtos/api/editar/${itemId}`,
            method: 'PUT',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            processData: false, // Prevent jQuery from processing the data
            contentType: false, // Prevent jQuery from setting the content type
            data: formData,
            success: function() {
                modal.hide();
                Unicorn.call('produtos_unicorn', 'recarregar');
                resetEditMode();
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

function loadProdutosView() {
    $('.vizualizar-produtos').off('click').on('click', function () {
        const form = $('#viewProdutos');
        const modal = new Modal(document.getElementById('viewProdutos'));
        const itemId = $(this).data('id');

        console.log('ID do item:', itemId);

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

        form.find('[data-modal-toggle="viewProdutos"]').off('click').on('click', function () {
            modal.hide();
        });
    });
}

function loadProdutosEdit() {
    $('.edit-item-btn').off('click').on('click', function () {
    if (editMode) {
        const itemId = $(this).data('id');
        editar(itemId);
    }
});
}

// barra de pesquisa
$('#index-pesquisa, #navbar-pesquisa, #sidebar-pesquisa').on('submit', function (e) {
    e.preventDefault();

    const action = $('#url-produtos').val();
    const pesquisa = $(this).find('input[type="text"]').val().trim();

    const url = new URL(action, window.location.origin);

    if (pesquisa) {
        url.searchParams.set('p', pesquisa);
    } else {
        url.searchParams.delete('p'); 
    }

    console.log('Ação final do formulário:', url.toString());

    const tempLink = $('<a>')
        .attr('href', url.toString())
        .css('display', 'none');

    $('body').append(tempLink);
    tempLink[0].click();
    tempLink.remove();
});
// end