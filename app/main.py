from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .chain_converter import convert_chain

app = FastAPI()

_DUMMY_TEMPL = (
    '<body style="margin: auto;">'
        '<div style="display: flex; min-height: 100vh; justify-content: center; align-items: center; font-size: 20px">'
            '<p style="text-align: center;">'
                '<strong>{0}</strong>'
                '<br><br>'
                '{1}'
            '</p>'
        '</div>'
    '</body>'
)

@app.get('/', response_class=HTMLResponse)
def read_root():
    return _DUMMY_TEMPL.format('Instruction',
                               'Use search bar. Input spent currency value,'
                               ' then gradually input 3-letter currency codes,'
                               ' starting from the original. Split codes chain with dashes')

@app.get('/{orig_spent}/{chain}', response_class=HTMLResponse)
def chain_rule(orig_spent: float, chain: str):
    total, rate = convert_chain(orig_spent, chain).values()
    return _DUMMY_TEMPL.format(total, rate)