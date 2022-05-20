from ui.display import Window
from ui.repeater_gui import RepeaterGui
from events.repeater_events import RepeaterEvents

window = Window('GUI на Python')
repeater_ui = RepeaterGui()
repeater_events = RepeaterEvents(window.get_root())


def logics(f):
    print('logics')


repeater_events.bind(logics)


window.start()
