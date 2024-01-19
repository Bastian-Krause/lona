from lona_picocss import install_picocss

from schmona import App

app = App(__file__)

install_picocss(app, debug=True)

app.run()