from collections import namedtuple

from PyQt4.QtCore import QFile, QDataStream, QIODevice

FileStream = namedtuple('FileStream', 'file stream')  # Keep reference to file.

FILENAME = ''  # whatever

def open_to_stream(filename, mode, stream_version=QDataStream.Qt_4_5):
    file = QFile(filename)
    file.open(mode)

    stream = QDataStream(file)
    stream.setVersion(stream_version)
    return FileStream(file, stream)

fs = open_to_stream(FILENAME, QIODevice.ReadOnly)

dct = fs.stream.readQVariantHash()
