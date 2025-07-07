from django_components import component

@component.register("formModal")
class FormModal(component.Component):
    template_name = "components/formModal.html"

    def get_context_data(self, formModal):
        return {
            "form": formModal,
        }
