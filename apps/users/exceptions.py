from django.template.defaultfilters import join


class RecordSaveError(Exception):

    def __init__(self, model, err_msg):
        self.message = "Failed to record " + model.to_s + " data because: " + join(', ', err_msg)
        super().__init__(self.message)

class RecordNotFoundError(Exception):

    def __init__(self, model):
        self.message = model.to_s + " not found"
        super().__init__(self.message)