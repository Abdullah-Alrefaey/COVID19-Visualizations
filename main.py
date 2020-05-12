import UI as ui
from PyQt5 import QtWidgets, QtCore
import plotly
import plotly.graph_objs as go
from helpers import loadCSVData


class GraphVisualizer(ui.Ui_MainWindow):
    """

    """

    def __init__(self, startWindow: QtWidgets.QMainWindow):
        # Initializer
        super(GraphVisualizer, self).setupUi(startWindow)
        logger.debug("Initializing")
        headers, dataLists, dataTuples = loadCSVData('Data.csv')
        fig = go.FigureWidget()
        fig.add_bar(x=dataLists[1], y=dataLists[2])
        fig.layout.title = 'Salary and Age'
        plotly.offline.plot(fig)
        graph_url = QtCore.QUrl.fromLocalFile(os.path.abspath('temp-plot.html'))
        self.WebEngineView.load(graph_url)
        logger.debug('Loading is Done')

    @staticmethod
    def showMessage(header, message, button, icon):
        """
        Responsible for showing message boxes

        ============= ===================================================================================
        **Arguments**
        header:       Box header title.
        message       the informative message to be shown.
        button:       button type.
        icon:         icon type.
        ============= ===================================================================================
        """
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(header)
        msg.setText(message)
        msg.setIcon(icon)
        msg.setStandardButtons(button)
        logger.debug(f"message shown with {header} {message} ")
        msg.exec_()


if __name__ == '__main__':
    import sys
    import os
    import logging

    # Setup Logger Maintainer
    logging.basicConfig(filename="logs/logfile.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GraphVisualizer(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
