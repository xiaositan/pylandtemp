from temperature.methods.mono_window import MonoWindow
from temperature.utils import get_lst_compute_fn_input

LST_METHODS = {'mono_window': MonoWindow}

class LST:
    def __init__(self, method, lst_methods=LST_METHODS):

        assert method in lst_methods, ValueError(f"method must be one of {lst_methods}")

        self.lst_methods = lst_methods
        self.method = method

    def __call__(self, emissivity_10, brightness_temperature_10, emissivity_11=None, brightness_temperature_11=None, column_water_vapour=None):

        lst_method_fn = self._get_methods(self.method)

        dict_input = get_lst_compute_fn_input(
                                            emissivity_10,
                                            emissivity_11, 
                                            brightness_temperature_10, 
                                            brightness_temperature_11, 
                                            column_water_vapour
                                            )
        # mask for nan values 

        return lst_method_fn()(dict_input)

    def _get_methods(self, method):
        if method not in self.lst_methods:
            raise NotImplementedError("Requested method not implemented. Choose among available methods: {self.methods}")
        return self.lst_methods[method]


