from .get_shiny_info import get_shiny_info
from .build_shiny import build_shiny

def shiny(global_variables):

    shiny_info = get_shiny_info(global_variables)
    build_shiny(global_variables, shiny_info)


