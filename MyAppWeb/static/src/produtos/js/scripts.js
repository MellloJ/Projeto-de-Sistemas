var preco_min = $('#preco-min');
var preco_max = $('#preco-max');

var preco_min_input = $('#preco-min-input');
var preco_max_input = $('#preco-max-input');

var editMode = false;

// addEventListener

document.addEventListener('keydown', function (event) {
    if ((event.ctrlKey || event.metaKey) && event.key === 'e') {
        event.preventDefault();
        toogleEditMode();
    }
});

document.addEventListener('keydown', function (event) {
    if ((event.ctrlKey || event.metaKey) && event.key === 'a') {
        event.preventDefault();
        toogleCreate();
    }
});

// on click

$('.index-categoria-button').on('click', function() {
    var categoria = $(this).data('categoria');
    var data = {
        categoria: categoria
    };

    Unicorn.call('produtos_unicorn', 'filter', JSON.stringify(data));
})

$('#edit-mode-toggle').on('click', function () {
    editMode = !editMode;
    if (editMode) {
        $(this).removeClass('bg-orange-400').addClass('bg-orange-500');
        $('.produtos-card, .categoria-card').addClass('ring-4 ring-orange-300').find('img');
    } else{
        $(this).removeClass('bg-orange-500').addClass('bg-orange-400');
        $('.produtos-card, .categoria-card').removeClass('ring-4 ring-orange-300').find('img');
    }
});

$('.edit-produto-btn').on('click', function () {
    const itemId = $(this).data('id');
    if (editMode) {
        editarProduto(itemId);
    } else {
        visualizarProduto(itemId);
    }
});

$('.edit-categoria-btn').on('click', function () {
    const itemId = $(this).data('id');
    if (editMode) {
        editarCategoria(itemId);
    } else {
        visualizarCategoria(itemId);
    }
});

$('.ordenar-button').on('click', function() {
    const order = $(this).val();
    Unicorn.call('produtos_unicorn', 'ordenar', JSON.stringify({order}));
});

$('#delete-produto-btn').on('click', function () {

    let itemId = $(this).attr('delete-id');
    let modal = new Modal(document.getElementById('editProdutos'));
    let formData = new FormData()

    formData.append('id', itemId);

    $.ajax({
        url: `/produtos/api/editar/produto/${itemId}`,
        method: 'DELETE',
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
                console.error('Erro ao deletar o item:', error);
            }
        }
    });
    modal.hide();   
});

$('#delete-categoria-btn').on('click', function () {

    let itemId = $(this).attr('delete-id');
    let modal = new Modal(document.getElementById('editCategorias'));
    let formData = new FormData()

    formData.append('id', itemId);

    $.ajax({
        url: `/produtos/api/editar/categoria/${itemId}`,
        method: 'DELETE',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        processData: false, // Prevent jQuery from processing the data
        contentType: false, // Prevent jQuery from setting the content type
        data: formData,
        success: function() {
            modal.hide();
            Unicorn.call('categorias_unicorn', 'recarregar');
            resetEditMode();
        },
        error: function(xhr, error) {
            if (xhr.status === 401) {
                console.error('Não autorizado. Verifique o token de autenticação.');
            } else {
                console.error('Erro ao deletar o item:', error);
            }
        }
    });
    modal.hide();   
});

// on change

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

// on submit

$('#filterModal').on('submit', function(e) {
    e.preventDefault();
    var categoria = $(this).find('#categoria').val()
    var preco_min = $(this).find('#preco-min').val();
    var preco_max = $(this).find('#preco-max').val();
    var rating = $(this).find('input[name="rating"]:checked').val();

    var data = {
        categoria: categoria,
        preco_min: preco_min,
        preco_max: preco_max,
        rating: rating
    };

    Unicorn.call('produtos_unicorn', 'filter', JSON.stringify(data));
});

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

    const tempLink = $('<a>')
        .attr('href', url.toString())
        .css('display', 'none');

    $('body').append(tempLink);
    tempLink[0].click();
    tempLink.remove();
});

$("#createProdutos").on('submit', function (e) {
    e.preventDefault();
    const formData = new FormData()

    formData.append('nome', $(this).find('#nome').val());
    formData.append('descricao', $(this).find('#descricao').val());
    formData.append('categoria', $(this).find('#categoria').val());
    formData.append('marca', $(this).find('#marca').val());
    formData.append('preco_unitario', $(this).find('#preco_unitario').val());
    formData.append('qtd_estoque', $(this).find('#qtd_estoque').val());
    formData.append('codigo_barras', $(this).find('#codigo_barras').val());
    formData.append('supermarket', $(this).find('#supermarket').val());

    const imagem = $(this).find('#imagem').prop('files')[0];
    if (imagem) {
        formData.append('imagem', imagem);
    }

    $.ajax({
        url: "/produtos/api/produtos/",
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        processData: false,
        contentType: false,
        data: formData,
        success: function() {
            e.target.reset();
            Unicorn.call('produtos_unicorn', 'recarregar');
            resetEditMode();
        },
        error: function(xhr, error) {
            if (xhr.status === 401) {
                console.error('Não autorizado. Verifique o token de autenticação.');
            } else {
                console.error('Erro ao criar o item:', error);
            }
        }
    });
})

$("#createCategorias").on('submit', function (e) {
    e.preventDefault();
    const formData = new FormData()

    formData.append('nome', $(this).find('#nome').val());
    formData.append('descricao', $(this).find('#descricao').val());
    formData.append('supermarket', $(this).find('#supermarket').val());

    const imagem = $(this).find('#imagem').prop('files')[0];

    if (imagem) {
        formData.append('imagem', imagem);
    }

    $.ajax({
        url: "/produtos/api/categorias/",
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        processData: false,
        contentType: false,
        data: formData,
        success: function() {
            e.target.reset();
            Unicorn.call('categorias_unicorn', 'recarregar');
            resetEditMode();
        },
        error: function(xhr, error) {
            if (xhr.status === 401) {
                console.error('Não autorizado. Verifique o token de autenticação.');
            } else {
                console.error('Erro ao criar o item:', error);
            }
        }
    });
})

// functions

function resetEditMode() {
    editMode = false;
    $('#edit-mode-toggle').removeClass('bg-orange-500')
    $('#edit-mode-toggle').addClass('bg-orange-400');
    $('.produtos-card, .categoria-card').removeClass('ring-4 ring-orange-300').find('img').removeClass('cursor-pointer');
}

function editarProduto(itemId) {

    const form = $('#editProdutos');
    const modal = new Modal(document.getElementById('editProdutos'));

    $.ajax({
        url: `/produtos/api/editar/produto/${itemId}`,
        method: 'GET',
        success: function(data) {
            form.find('#delete-produto-btn').attr('delete-id', itemId);
            form.find('#nome').val(data.nome);
            form.find('#descricao').val(data.descricao);
            form.find('#categoria').val(data.categoria);
            form.find('#marca').val(data.marca);
            form.find('#preco_unitario').val(data.preco_unitario);
            form.find('#qtd_estoque').val(data.qtd_estoque);
            form.find('#codigo_barras').val(data.codigo_barras);
            form.find('#supermarket').val(data.supermarket);

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
        formData.append('supermarket', form.find('#supermarket').val());

        const imagem = form.find('#imagem').prop('files')[0];
        if (imagem) {
            formData.append('imagem', imagem);
        }

        $.ajax({
            url: `/produtos/api/editar/produto/${itemId}`,
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

function editarCategoria(itemId) {

    const form = $('#editCategorias');
    const modal = new Modal(document.getElementById('editCategorias'));

    $.ajax({
        url: `/produtos/api/editar/categoria/${itemId}`,
        method: 'GET',
        success: function(data) {
            form.find('#delete-categoria-btn').attr('delete-id', itemId);
            form.find('#nome').val(data.nome);
            form.find('#descricao').val(data.descricao);
            form.find('#supermarket').val(data.supermarket);
        },
        error: function(xhr, status, error) {
            console.error('Erro ao buscar os dados do item:', error);
        }
    });

    modal.show();

    form.find('[data-modal-toggle="editCategorias"]').off('click').on('click', function () {
        modal.hide();
    });

    form.off('submit').on('submit', function (e) {
        e.preventDefault();

        const formData = new FormData()

        formData.append('id', itemId);
        formData.append('nome', form.find('#nome').val());
        formData.append('descricao', form.find('#descricao').val());
        formData.append('supermarket', form.find('#supermarket').val());

        const imagem = form.find('#imagem').prop('files')[0];
        if (imagem) {
            formData.append('imagem', imagem);
        }

        $.ajax({
            url: `/produtos/api/editar/categoria/${itemId}`,
            method: 'PUT',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            processData: false, // Prevent jQuery from processing the data
            contentType: false, // Prevent jQuery from setting the content type
            data: formData,
            success: function() {
                modal.hide();
                Unicorn.call('categorias_unicorn', 'recarregar');
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

function visualizarCategoria(itemId) {
    const form = $('#viewCategorias');
    const modal = new Modal(document.getElementById('viewCategorias'));

    $.ajax({
        url: `/produtos/api/editar/categoria/${itemId}`,
        method: 'GET',
        success: function(data) {
            form.find('#nome').val(data.nome);
            form.find('#descricao').val(data.descricao);
            form.find('#supermarket').val(data.supermarket);
        },
        error: function(xhr, status, error) {
            console.error('Erro ao buscar os dados do item:', error);
        }
    });

    modal.show();

    form.find('[data-modal-toggle="viewCategorias"]').off('click').on('click', function () {
        modal.hide();
    });
}

function visualizarProduto(itemId) {
    const form = $('#viewProdutos');
    const modal = new Modal(document.getElementById('viewProdutos'));

    $.ajax({
        url: `/produtos/api/editar/produto/${itemId}`,
        method: 'GET',
        success: function(data) {
            form.find('#nome').val(data.nome);
            form.find('#descricao').val(data.descricao);
            form.find('#categoria').val(data.categoria);
            form.find('#marca').val(data.marca);
            form.find('#preco_unitario').val(data.preco_unitario);
            form.find('#qtd_estoque').val(data.qtd_estoque);
            form.find('#codigo_barras').val(data.codigo_barras);
            form.find('#supermarket').val(data.supermarket);
        },
        error: function(xhr, status, error) {
            console.error('Erro ao buscar os dados do item:', error);
        }
    });

    modal.show();

    form.find('[data-modal-toggle="viewProdutos"]').off('click').on('click', function () {
        modal.hide();
    });
}

// function loadProdutosEdit() {
//     $('.edit-produto-btn').off('click').on('click', function () {
//         if (editMode) {
//             const itemId = $(this).data('id');
//             editarProduto(itemId);
//         }
//     });
// }

function toogleEditMode() {
    $('#edit-mode-toggle').trigger('click');
} 

function toogleCreate() {
    $('#novo-modal-button').trigger('click');
}  