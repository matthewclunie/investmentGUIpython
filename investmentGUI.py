"""
Program: labeldemo.py
Author: Matthew 11/10/2021


*** Note: the file breezypythongui.py MUST be in the
same directory as this file for the application to work
"""

from breezypythongui import EasyFrame

class TextAreaDemo(EasyFrame):
	"""An investment calculator that demonstrates the use of a multi-line text area widget."""

	def __init__(self):
		"""Sets up the window and the label."""
		EasyFrame.__init__(self, title = "Investment Calculator")
		self.addLabel(text = "Initial Amount", row = 0, column = 0)
		self.addLabel(text = "Number of Years", row = 1, column = 0)
		self.addLabel(text = "Interest rate in %", row = 2, column = 0)
		self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
		self.period = self.addIntegerField(value = 0, row = 1, column = 1)
		self.rate = self.addIntegerField(value = 0, row = 2, column = 1)
		self.outputArea = self.addTextArea(text = "", row = 4, column = 0, columnspan = 2, width = 50, height = 15)
		self.button = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute) 

		#Change that button color!
		self.button["background"] = "PaleVioletRed"

	#Event handling method
	def compute(self):
		"""Computes the investment schedule based on the inputs and outputs the full report"""
		
		#Obtain and validate the inputs
		startBalance = self.amount.getNumber()
		years = self.period.getNumber()
		rate = self.rate.getNumber()

		#If any of the inputs are a zero, just exit the function
		if startBalance == 0 or rate == 0 or years == 0:
			self.outputArea["state"] = "normal"
			self.outputArea.setText("Please make sure that no inputs \ncontain a zero!")
			return 

		#Calculation phase
		#Convert the rate to a decimal number
		rate = rate / 100

		#Initialize the accumulator for the interest
		totalInterest = 0.0

		#Display the header for the table in tabular notation
		result = "%4s%18s%10s%16s\n" % ("Year", "Starting Balance","Interest", "Ending Balance")

		#Compute and append the results for each year
		for year in range(1, years + 1):
			interest = startBalance * rate
			endBalance = startBalance + interest
			result += "%4d%18.2f%10.2f%16.2f\n" % (years, startBalance, interest, endBalance)
			startBalance = endBalance
			totalInterest += interest

		#Append the totals to the result string for the entire report
		result += "Ending balance: $%0.2f\n" % endBalance
		result += "Total interest earned: $%0.2f\n" % totalInterest

		#Output the result while preserving read-only status
		self.outputArea["state"] = "normal"
		self.outputArea.setText(result)
		self.outputArea["state"] = "disabled"

#Definition of the main() function for program entry
def main(): 
	"""Instantiates and pops up the window."""
	TextAreaDemo().mainloop()

#Global call to trigger the main function
if __name__ == "__main__":
	main()
