from flat import Bill, Flatmate, PdfReport, FileShare

bill_input = float(input("Hey user, enter the bill amount: "))
period_input = input("What is the bill period? E.g: February 2023: ")

name_1 = input("What is your name: ")
days_in_house1 = int(input(f"How many days did {name_1} stay in house "))

name_2 = input("What is the name of the other flatmate?: ")
days_in_house2 = int(input(f"How many days did {name_2} stay in house "))

the_bill = Bill(amount=bill_input, period=period_input)
flatmate1 = Flatmate(name=name_1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name_2, days_in_house=days_in_house2)

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)

file_share = FileShare(filepath=pdf_report.filename)
print(file_share.share())
