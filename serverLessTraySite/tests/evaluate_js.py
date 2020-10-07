"""
Sends and executes js code on the client side
"""

import webview
from time import sleep

def evaluate_js(window):
    intro_message = "the best"
    js_code = r"""
        var h1 = document.createElement('h1')
        var text = document.createTextNode('{}')
        h1.appendChild(text)
        document.body.appendChild(h1)

        document.body.style.backgroundColor = '#212121'
        document.body.style.color = '#f2f2f2'

        // Return user agent
        'User agent:\n' + navigator.userAgent;
        """.format("hello")
    result = window.evaluate_js(js_code)

    sleep(1)

    js_code = r"""
        document.body.style.backgroundColor = 'red';
    """
    window.evaluate_js(js_code)


if __name__ == '__main__':
    window = webview.create_window('Run custom JavaScript')
    webview.start()