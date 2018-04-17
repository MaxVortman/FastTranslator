from src.ClipboardWatcher import ClipboardWatcher
from src.TranslationWindow import TranslationWindow


tw = TranslationWindow(100, 100)

watcher = ClipboardWatcher(lambda x : True, tw.set_label_text)
watcher.start()
tw.start_loop()
