from PySide2.QtWidgets import QMainWindow, QApplication, QCompleter, QAbstractItemView
from PySide2.QtCore import Qt, QAbstractItemModel, QModelIndex
from PySide2.QtGui import QStandardItem, QStandardItemModel, QPixmap
from searchui import Ui_MainWindow
import sys
import cards


class DojoClient(QMainWindow):
	def __init__(self):
		super(DojoClient, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.card_catalog = cards.CardCatalog()

		self.init_ui()

	def init_ui(self):
		self.ui.card_search_completer = QCompleter(self.card_catalog.names_list_unique, self)
		self.ui.card_search_completer.setCaseSensitivity(Qt.CaseInsensitive)
		self.ui.search_entry.setCompleter(self.ui.card_search_completer)
		self.ui.search_entry.returnPressed.connect(self.search_for_card)
		self.ui.search_button.clicked.connect(self.search_for_card)

		self.ui.add_card_button.clicked.connect(self._show_selected)

		self.ui.results_tree.setSelectionBehavior(QAbstractItemView.SelectRows)


	def _show_selected(self):
		print(self.ui.results_tree.selectedIndexes())

	# -------- Search Entry and View --------

	def search_for_card(self):
		results = self.fetch_card_search_results()

		self.ui.results_tree.setModel(self.model_search_results(results))
		self.ui.results_tree.setColumnWidth(0, 200)
		self.ui.results_tree.clicked[QModelIndex].connect(self.select_card)

	# try to allow card_dict to accept both card_dicts from the catalog and Card objects' .__dict__ attribute
	def preview_card(self, card_dict):

		pixmap = QPixmap()
		pixmap.loadFromData(self.card_catalog.retrieve_card_image(card_dict).content)
		self.ui.card_preview.setPixmap(pixmap)
		self.ui.card_preview.setScaledContents(True)


	def select_card(self, index):

		self.ui.selected_card_dict = self.fetch_selected_card_dict(index)
		self.preview_card(self.ui.selected_card_dict)
		
	def fetch_selected_card_dict(self, index):
		row_number = index.row()
		name_index = self.ui.results_tree.model()

		name_index = self.ui.results_tree.model().index(row_number,0)
		set_index = self.ui.results_tree.model().index(row_number,1)

		name = self.ui.results_tree.model().itemFromIndex(name_index).text()
		set_name = self.ui.results_tree.model().itemFromIndex(set_index).text()

		return self.card_catalog.lookup_by_name_and_set(name, set_name)

	def fetch_card_search_results(self):
		return self.card_catalog.search_by_name_contains(self.ui.search_entry.text())

	def model_search_results(self, results):
		
		search_model = QStandardItemModel()
		search_model.setHorizontalHeaderLabels(['Name', 'Set'])

		parentItem = search_model.invisibleRootItem()

		for i in range(len(results)):
			model_data = [QStandardItem(results[i]['name']), QStandardItem(results[i]['set_name'])]
			parentItem.appendRow(model_data)
			# parentItem = model_data 

		return search_model

	# -------- End Search Entry and View -------

	# -------- Card Preview --------





app = QApplication(sys.argv)
app_window = DojoClient()

app_window.show()
sys.exit(app.exec_())