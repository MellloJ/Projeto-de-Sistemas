$('#logout').on('click', function() {
    const logoutUrl = $(this).attr('logout-url');
    $.ajax({
        url: logoutUrl,
        type: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        xhrFields: {
            withCredentials: true  // Envia o cookie automaticamente
        },
        success: function() {
            window.location.href = '/';
        },
        error: function(xhr, status, error) {
            alert('Erro ao fazer logout: ' + error);
        }
    });
})