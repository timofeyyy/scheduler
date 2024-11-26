import launcher
import data_reader
import json

# launcher.start()
reader = data_reader.Reader()
reader.fetch()
reader.print()
