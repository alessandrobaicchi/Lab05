import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()


    def load_corsi(self):
        corsi = self._model.get_all_corsi()
        # Chiedo al Model la lista dei codici di insegnamento. Poi, cicla su questa
        # lista e la aggiunge alla lista delle opzioni del Dropdown.
        # Questo metodo lo uso nel View.
        for c in corsi:
            self._view.dd_corsi.options.append(
                ft.dropdown.Option(
                    key = c.codins,
                    text = str(c))
                    )


    def handle_cerca_iscritti(self, e):
        # 1) Leggo il corso scelto nel dropdown
        codins = self._view.dd_corsi.value

        if codins is None:
            self._view.create_alert("Seleziona un corso!")
            return

        # 2) Chiedo al Model la lista degli studenti iscritti al corso scelto
        studenti = self._model.get_studenti_by_corso(codins)    # studenti è una lista

        # 3) Pulisco la finestra dei risultati
        self._view.txt_result.controls.clear()

        # 4) Stampo i risultati
        if not len(studenti):
            self._view.txt_result.controls.append(ft.Text(f"Nessun studente iscritto al corso {codins}"))
            self._view.update_page()
            return
        # Altrimenti esiste una lista di studenti iscritti a quel corso.
        self._view.txt_result.controls.append(ft.Text(f"Ecco gli studenti iscritti al corso {codins}:"))
        for s in studenti:
            self._view.txt_result.controls.append(ft.Text(str(s)))
        self._view.update_page()

