from urllib import response
import pyodide
from pyodide.http import pyfetch
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")
sns.set(font_scale=0.8)


async def on_click(e):
    btn = document.getElementById('btn-load')
    data = await make_request('table','GET')
    data_frame = pd.DataFrame(data)
    fig, axes = plt.subplots()
    fig.set_size_inches(8,8) 
    sns.lineplot(x= data_frame.index, y=data_frame.iloc[:,0])
    plt.tight_layout()
    plt.xticks(rotation = 45)
    pyscript.write('lineplot', fig)
    
async def make_request(url, method, headers=None):
    if not headers:
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json'
        }
    response = await pyfetch(
        url=url,
        method = method,
        headers=headers
    )
    return await response.json()
    
def main():
    button = document.getElementById('btn-load')
    button.addEventListener('click', pyodide.create_proxy(on_click))
main()