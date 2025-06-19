// scripts.js para gerenciamento (usuários e endereços)
// Inclui DataTables para as tabelas de usuários e endereços

$(document).ready(function() {
    // Garante que o DataTables está disponível antes de usar
    if (typeof $.fn.DataTable === 'undefined') {
        console.error('DataTables não foi carregado corretamente. Verifique se o script do DataTables está incluído antes deste arquivo.');
        return;
    }

    if ($('#usuarios-table').length) {
        $('#usuarios-table').DataTable({
            language: {
                url: 'https://cdn.datatables.net/plug-ins/1.13.4/i18n/pt-BR.json',
                decimal: ",",
                thousands: ".",
                search: "Pesquisar:",
                lengthMenu: "Mostrar _MENU_ registros",
                info: "Mostrando _START_ a _END_ de _TOTAL_ registros",
                infoEmpty: "Mostrando 0 a 0 de 0 registros",
                infoFiltered: "(filtrado de _MAX_ registros no total)",
                zeroRecords: "Nenhum registro encontrado",
                paginate: {
                    first: "Primeiro",
                    last: "Último",
                    next: "Próximo",
                    previous: "Anterior"
                },
            },
            pageLength: 10,
            lengthMenu: [5, 10, 25, 50, 100],
            responsive: true,
            order: [[0, 'asc']],
            searching: true,
            paging: true,
            info: true,
            autoWidth: false,
            ordering: true,
            dom: '<"flex flex-wrap items-center justify-between mb-2"lfr>tip',
        });
    }

    if ($('#enderecos-table').length) {
        $('#enderecos-table').DataTable({
            language: {
                url: 'https://cdn.datatables.net/plug-ins/1.13.4/i18n/pt-BR.json',
                decimal: ",",
                thousands: ".",
                search: "Pesquisar:",
                lengthMenu: "Mostrar _MENU_ registros",
                info: "Mostrando _START_ a _END_ de _TOTAL_ registros",
                infoEmpty: "Mostrando 0 a 0 de 0 registros",
                infoFiltered: "(filtrado de _MAX_ registros no total)",
                zeroRecords: "Nenhum registro encontrado",
                paginate: {
                    first: "Primeiro",
                    last: "Último",
                    next: "Próximo",
                    previous: "Anterior"
                },
            },
            pageLength: 10,
            lengthMenu: [5, 10, 25, 50, 100],
            responsive: true,
            order: [[0, 'asc']],
            searching: true,
            paging: true,
            info: true,
            autoWidth: false,
            ordering: true,
            dom: '<"flex flex-wrap items-center justify-between mb-2"lfr>tip',
        });
    }
});

$(document).on('blur', '#novo-zip_code', function() {
    const cep = $(this).val().replace(/\D/g, '');
    if (cep.length === 8) {
        $.get(`/gerenciamento/api/cep/${cep}/`, function(data) {
            if (data.zip_code) $('#novo-zip_code').val(data.zip_code);
            if (data.street) $('#novo-street').val(data.street);
            if (data.complement) $('#novo-complement').val(data.complement);
            if (data.neighborhood) $('#novo-neighborhood').val(data.neighborhood);
            if (data.city) $('#novo-city').val(data.city);
            if (data.state) $('#novo-state').val(data.state);
        }).fail(function(xhr) {
            // Limpa campos se erro
            $('#novo-street').val('');
            $('#novo-complement').val('');
            $('#novo-neighborhood').val('');
            $('#novo-city').val('');
            $('#novo-state').val('');
        });
    }
});

$(document).on('blur', '#edit-zip_code', function() {
    const cep = $(this).val().replace(/\D/g, '');
    if (cep.length === 8) {
        $.get(`/gerenciamento/api/cep/${cep}/`, function(data) {
            if (data.zip_code) $('#edit-zip_code').val(data.zip_code);
            if (data.street) $('#edit-street').val(data.street);
            if (data.complement) $('#edit-complement').val(data.complement);
            if (data.neighborhood) $('#edit-neighborhood').val(data.neighborhood);
            if (data.city) $('#edit-city').val(data.city);
            if (data.state) $('#edit-state').val(data.state);
        }).fail(function(xhr) {
            // Limpa campos se erro
            $('#edit-street').val('');
            $('#edit-complement').val('');
            $('#edit-neighborhood').val('');
            $('#edit-city').val('');
            $('#edit-state').val('');
        });
    }
});

$(".edit-endereco-btn").on('click', function() {
    const id = $(this).data('id');
    if (!id) {
        Swal.fire('Erro', 'ID do endereço não encontrado.', 'error');
        return;
    }
    const modal = new Modal(document.getElementById('editEnderecos'));

    $.ajax({
        url: `/gerenciamento/api/enderecos/${id}/`,
        method: 'GET',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        success: function(data) {

            console.log('Dados do endereço:', data);

            modal.hide();
            $('#edit-id').val(id);
            $('#edit-zip_code').val(data.zip_code);
            $('#edit-street').val(data.street);
            $('#edit-number').val(data.number);
            $('#edit-complement').val(data.complement);
            $('#edit-neighborhood').val(data.neighborhood);
            $('#edit-city').val(data.city);
            $('#edit-state').val(data.state);
            $('#edit-user-id').val(data.user);
            modal.show();

            console.log('Editando endereço com ID:', id);
            console.log('Editando endereço com ID:', $('#edit-id').val());
        },
        error: function(xhr, error) {
            if (xhr.status === 401) {
                console.error('Não autorizado. Verifique o token de autenticação.');
            } else {
                alert('Erro ao buscar endereço: ' + (xhr.responseJSON?.error || xhr.statusText));
            }
        }
    });
});

$(".delete-endereco-btn").on('click', function() {
    const id = $(this).data('id');
    const modal = new Modal(document.getElementById('editEnderecos'));

    Swal.fire({
        title: 'Tem certeza?',
        text: 'Deseja realmente excluir este endereço?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sim, excluir',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            $.ajax({
                url: `/gerenciamento/api/enderecos/${id}/`,
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                success: function() {
                    modal.hide();
                    location.reload();
                },
                error: function(xhr, error) {
                    if (xhr.status === 401) {
                        console.error('Não autorizado. Verifique o token de autenticação.');
                    } else {
                        Swal.fire('Erro', 'Erro ao excluir endereço: ' + (xhr.responseJSON?.error || xhr.statusText), 'error');
                    }
                }
            });
        }
    });
});

$("#createEnderecos").on('submit', function (e) {
    e.preventDefault();
    const formData = new FormData();

    formData.append('zip_code', $(this).find('#novo-zip_code').val());
    formData.append('street', $(this).find('#novo-street').val());
    formData.append('number', $(this).find('#novo-number').val());
    formData.append('complement', $(this).find('#novo-complement').val());
    formData.append('neighborhood', $(this).find('#novo-neighborhood').val());
    formData.append('city', $(this).find('#novo-city').val());
    formData.append('state', $(this).find('#novo-state').val());
    formData.append('user', $(this).find('#novo-user-id').val());

    $.ajax({
        url: '/gerenciamento/api/enderecos/',
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        processData: false,
        contentType: false,
        data: formData,
        success: function() {
            e.target.reset();
            $(e.target).closest('.modal').hide();
            location.reload();
        },
        error: function(xhr, error) {
            if (xhr.status === 401) {
                console.error('Não autorizado. Verifique o token de autenticação.');
            } else {
                alert('Erro ao criar endereço: ' + (xhr.responseJSON?.error || xhr.statusText));
            }
        }
    });
});

$("#editEnderecos").on('submit', function(e) {
    e.preventDefault();
    const formData = new FormData();

    formData.append('id', $(this).find('#edit-id').val());
    formData.append('zip_code', $(this).find('#edit-zip_code').val());
    formData.append('street', $(this).find('#edit-street').val());
    formData.append('number', $(this).find('#edit-number').val());
    formData.append('complement', $(this).find('#edit-complement').val());
    formData.append('neighborhood', $(this).find('#edit-neighborhood').val());
    formData.append('city', $(this).find('#edit-city').val());
    formData.append('state', $(this).find('#edit-state').val());
    formData.append('user', $(this).find('#edit-user-id').val());

    const id = $(this).find('#edit-id').val();

    Swal.fire({
        title: 'Confirmar edição',
        text: 'Deseja realmente salvar as alterações deste endereço?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: 'Sim, salvar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            $.ajax({
                url: `/gerenciamento/api/enderecos/${id}/`,
                method: 'PUT',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                processData: false,
                contentType: false,
                data: formData,
                success: function() {
                    e.target.reset();
                    $(e.target).closest('.modal').hide();
                    location.reload();
                },
                error: function(xhr, error) {
                    if (xhr.status === 401) {
                        console.error('Não autorizado. Verifique o token de autenticação.');
                    } else if (xhr.status === 404) {
                        Swal.fire('Erro', 'Endereço não encontrado.', 'error');
                    } else {
                        Swal.fire('Erro', 'Erro ao editar endereço: ' + (xhr.responseJSON?.error || xhr.statusText), 'error');
                    }
                }
            });
        }
    });
});

$("#dados-mercado-form").on('submit', function(e) {
    e.preventDefault();

    const data = {
        id: $('#id').val(),
        fantasy_name: $('#fantasy_name').val(),
        cnpj: $('#cnpj').val(),
        email: $('#email').val(),
        phone: $('#phone').val()
    };
    $.ajax({
        url: '/gerenciamento/api/dados-mercado/',
        method: 'PUT',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function() {
            Swal.fire('Sucesso', 'Dados do mercado atualizados com sucesso.', 'success').then(() => {
                location.reload();
            });
        },
        error: function(xhr, error) {
            if (xhr.status === 401) {
                Swal.fire('Erro', 'Não autorizado. Faça login novamente.', 'error');
            } else {
                Swal.fire('Erro', 'Erro ao atualizar dados do mercado: ' + (xhr.responseJSON?.error || xhr.statusText), 'error');
            }
        }
    });
});

