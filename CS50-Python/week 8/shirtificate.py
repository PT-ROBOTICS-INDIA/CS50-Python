from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Setting font for the top title
        self.set_font("helvetica", "B", 45)
        self.cell(0, 50, "CS50 Shirtificate", align="C")
        self.ln(20)

def main():
    name = input("Name: ")
    create_shirt(name)

def create_shirt(user_name):
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Place the shirt image (centered)
    # x=15, y=70, width=180mm
    pdf.image("shirtificate.png", x=15, y=70, w=180)

    # Place the user's name on top of the shirt
    pdf.set_font("helvetica", "B", 25)
    pdf.set_text_color(255, 255, 255) # White text for the shirt

    # Position the text horizontally and vertically on the shirt
    pdf.text(x=45, y=145, txt=f"{user_name} took CS50P")

    # Save the file
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
