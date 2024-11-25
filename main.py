import launcher
import data_reader

# launcher.start()
reader = data_reader.Reader()
reader.fetch()

reader.print()