// scripts.js para gerenciamento (usuários e endereços)
// Inclui DataTables para as tabelas de usuários e endereços

$(document).ready(function() {
    // DataTable para usuários (já existente)
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
    // DataTable para endereços
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
    // Ações para usuários
    $(document).on('click', '.edit-user-btn', function() {
        const id = $(this).data('id');
        alert('Editar usuário ID: ' + id);
    });
    $(document).on('click', '.delete-user-btn', function() {
        const id = $(this).data('id');
        alert('Deletar usuário ID: ' + id);
    });
    $('#novo-usuario-btn').on('click', function(e) {
        e.preventDefault();
        alert('Abrir modal de novo usuário (implementar)');
    });
    // Ações para endereços
    $(document).on('click', '.edit-endereco-btn', function() {
        const id = $(this).data('id');
        alert('Editar endereço ID: ' + id);
    });
    $(document).on('click', '.delete-endereco-btn', function() {
        const id = $(this).data('id');
        alert('Deletar endereço ID: ' + id);
    });
    $('#novo-endereco-btn').on('click', function(e) {
        e.preventDefault();
        alert('Abrir modal de novo endereço (implementar)');
    });
    
    // Preenchimento automático de endereço pelo CEP no formulário de novo endereço
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

    // Função utilitária para obter o token JWT do localStorage
    function getJWTToken() {
        return localStorage.getItem('access_token');
    }

    // Submit do formulário de novo endereço (CREATE)
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

        const headers = {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        };
        
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

    // Submit do formulário de edição de endereço (EDIT) usando FormData
    $("#editEnderecos").on('submit', function(e) {
        e.preventDefault();
        const formData = new FormData();

        formData.append('zip_code', $(this).find('#editar-zip_code').val());
        formData.append('street', $(this).find('#editar-street').val());
        formData.append('number', $(this).find('#editar-number').val());
        formData.append('complement', $(this).find('#editar-complement').val());
        formData.append('neighborhood', $(this).find('#editar-neighborhood').val());
        formData.append('city', $(this).find('#editar-city').val());
        formData.append('state', $(this).find('#editar-state').val());

        const id = $(this).find('#editar-id').val();
        const headers = {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        };
        const token = getJWTToken();
        if (token) headers['Authorization'] = 'Bearer ' + token;

        $.ajax({
            url: `/gerenciamento/api/enderecos/${id}/`,
            method: 'PUT',
            headers: headers,
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
                    alert('Erro ao editar endereço: ' + (xhr.responseJSON?.error || xhr.statusText));
                }
            }
        });
    });
});

