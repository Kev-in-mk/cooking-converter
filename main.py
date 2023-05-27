from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextFieldRect
from kivy.uix.textinput import TextInput
# from kivy.clock import Clock
import pandas as pd
import re
df = pd.read_csv('unit_conversion.csv')
non_liquid = pd.read_csv('non_liquid.csv')
# print(df.iloc[0])
# print(df.index)
# print(non_liquid)
# for i in df.index:
# 	print(df.iloc[i])

Window.size = (480, 720)
Builder.load_file('cups.kv')

# Clock.max_iteration = 100


class MainWindow(Screen):
	liquid_and_volume = StringProperty('Liquid\nand\nVolume measures')


class SecondWindow(Screen):
	imperial_unit = StringProperty('Imperial Unit')
	metric_unit = StringProperty('Metric Unit')
	input_amount = NumericProperty(1)
	result = StringProperty('')
	# mode = NumericProperty(2)

	def __init__(self, **kwargs):
		self.mode = 0
		# self.modes = (0, 1, 2, 3)
		self.imperial_unit = df.imperial[self.mode]
		self.metric_unit = df.metric[self.mode]
		super().__init__(**kwargs)

	def conversion(self):
		try:
			if float(self.ids.input_amount.text) <= 1:
				self.imperial_unit = f'{self.ids.input_amount.text} {df.imperial[self.mode]}'
			else:
				self.imperial_unit = f'{self.ids.input_amount.text} {df.imperial[self.mode]}s'
			self.result = f'{float(self.ids.input_amount.text) * df.imperial_to_metric[self.mode]:.2f}'
			print(float(self.ids.input_amount.text) * df.imperial_to_metric[self.mode])
		except ValueError as e:
			self.result = 'Please enter a number to convert'

	def change_units(self):
		# print(len(self.modes) - 1)
		if self.mode == 3:
			self.mode = 0
		else:
			self.mode += 1
		self.imperial_unit = df.imperial[self.mode]
		self.metric_unit = df.metric[self.mode]
		print(self.mode)


class ThirdWindow(Screen):
	imperial_unit = StringProperty('Imperial Unit')
	metric_unit = StringProperty('Metric Unit')
	input_amount = NumericProperty(1)
	result = StringProperty('')

	# mode = NumericProperty(2)
	def __init__(self, **kwargs):
		self.mode = 4
		# self.modes = (4, 5, 6, 7, 8)
		self.imperial_unit = df.imperial[self.mode]
		self.metric_unit = df.metric[self.mode]

		super().__init__(**kwargs)

	def conversion(self):
		try:
			# if float(self.ids.input_amount.text) == 1:
			self.result = f'{float(self.ids.input_amount.text) * df.imperial_to_metric[self.mode]}'
			print(float(self.ids.input_amount.text) * df.imperial_to_metric[self.mode])
		except ValueError as e:
			self.result = 'Please enter a number to convert'
	def change_units(self):
		# print(len(self.modes) - 1)
		if self.mode == len(df.imperial) - 1:
			self.mode = 4
		else:
			self.mode += 1
		self.imperial_unit = df.imperial[self.mode]
		self.metric_unit = df.metric[self.mode]
		print(self.mode)


class FourthWindow(Screen):
	fahrenheit = StringProperty('Fahrenheit')
	celsius = StringProperty('Celsius')
	result = StringProperty('')
	mode = NumericProperty(0)
	# mode = NumericProperty(2)

	def __init__(self, **kwargs):
		self.modes = ['c_to_f', 'f_to_c']
		self.mode = '0'
		# self.fahrenheit = non_liquid.ingredient[self.mode]
		super().__init__(**kwargs)

	def conversion(self):
		try:
			if self.mode == 0:
				# self.fahrenheit = f'{self.ids.input_amount.text}\xb0 Fahrenheit'
				self.result = f'{(float(self.ids.input_amount.text) - 32) * 5/9:.2f}\xb0C'
			else:
				self.result = f'{(float(self.ids.input_amount.text) * 9 / 5) + 32:.2f}\xb0F'
		except ValueError as e:
			self.result = 'Please enter a number to convert'

	def change_units(self):
		try:
			if self.mode == 0:
				self.fahrenheit, self.celsius = self.celsius, self.fahrenheit
				# self.result = f'{(float(self.ids.input_amount.text) * 9/5) + 32:.2f}\xb0C'
				# self.fahrenheit = f'{self.ids.input_amount.text}\xb0 Fahrenheit'

				self.mode += 1

			else:
				if self.mode == 1:
					self.celsius, self.fahrenheit = self.fahrenheit, self.celsius
				self.mode -= 1
		except ValueError as e:
			self.result = f'Please enter a number to convert'
		# self.metric_unit = df.metric[self.mode]
		print(self.mode)


class FifthWindow(Screen):
	ingredient = StringProperty('Ingredient')
	# metric_unit = StringProperty('Metric Unit')
	# input_amount = NumericProperty(1)
	result = StringProperty('')

	# mode = NumericProperty(2)
	def __init__(self, **kwargs):
		self.mode = 0
		self.ingredient = non_liquid.ingredient[self.mode]
		super().__init__(**kwargs)

	def conversion(self):
		try:
			if float(self.ids.input_amount.text) == 1:
				self.result = f'{self.ids.input_amount.text} cup {float(self.ids.input_amount.text) * non_liquid.weight[self.mode]} grams'
			else:
				self.result = f'{self.ids.input_amount.text} cups {float(self.ids.input_amount.text) * non_liquid.weight[self.mode]} grams'
		except ValueError as e:
			self.result = 'Please enter a number to convert'

	def change_units(self):
		# print(len(self.modes) - 1)
		try:
			if self.mode == len(non_liquid.ingredient) - 1:
				self.mode = 0
			else:
				self.mode += 1
			self.ingredient = non_liquid.ingredient[self.mode]
			if float(self.ids.input_amount.text) == 1:
				self.result = f'{self.ids.input_amount.text} cup {float(self.ids.input_amount.text) * non_liquid.weight[self.mode]} grams'
			else:
				self.result = f'{self.ids.input_amount.text} cups {float(self.ids.input_amount.text) * non_liquid.weight[self.mode]} grams'

		except ValueError as e:
			self.result = f'Please enter a number to convert'
		# self.metric_unit = df.metric[self.mode]
		print(self.mode)


class Container(ScreenManager):
	pass


class CupsToGrams(MDApp):
	def build(self):
		self.title = 'Cups to grams'
		self.theme_cls.theme_style = 'Dark'
		self.theme_cls.primary_palette = 'Amber'
		# self.theme_cls.primary_accent = 'DeepPurple'
		# self.theme_cls.disabled_hint_text_color = 'Teal'
		self.root = Factory.Container()


if __name__ == '__main__':
	CupsToGrams().run()

