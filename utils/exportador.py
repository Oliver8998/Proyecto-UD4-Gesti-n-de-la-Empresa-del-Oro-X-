# exportador.py
from fpdf import FPDF

class ExportadorPDF:
    def exportarInformeCompleto(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Informe completo", ln=True)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Usuarios", ln=True)
        pdf.set_font("Arial", "", 10)
        with open("usuarios.csv", "r") as f:
            for linea in f:
                pdf.cell(0, 8, linea.strip(), ln=True)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Tasaciones", ln=True)
        pdf.set_font("Arial", "", 10)
        with open("tasaciones.csv", "r") as f:
            for linea in f:
                pdf.cell(0, 8, linea.strip(), ln=True)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Ventas", ln=True)
        pdf.set_font("Arial", "", 10)
        with open("ventas.csv", "r") as f:
            for linea in f:
                pdf.cell(0, 8, linea.strip(), ln=True)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Estados", ln=True)
        pdf.set_font("Arial", "", 10)
        with open("estados.csv", "r") as f:
            for linea in f:
                pdf.cell(0, 8, linea.strip(), ln=True)

        pdf.add_page()
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Grafico: Oro vendido por cliente", ln=True)
        pdf.image("graficoOroPorCliente.png", x=10, y=30, w=180)

        pdf.add_page()
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Grafico: Ventas por mes", ln=True)
        pdf.image("graficoVentasPorMes.png", x=10, y=30, w=180)

        pdf.output("informeCompleto.pdf")
        print("Informe completo generado en informeCompleto.pdf")
