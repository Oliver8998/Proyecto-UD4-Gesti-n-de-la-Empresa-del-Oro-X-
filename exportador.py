from fpdf import FPDF
class ExportadorPDF:

    def exportarInformeCompleto(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        #informe de clientes
        pdf.cell(200, 10, "informe de clientes", ln=True, align="C")
        with open("clientes.csv", "r") as f:
            for linea in f:
                pdf.cell(200, 10, linea.strip(), ln=True)

        pdf.add_page()
        pdf.cell(200, 10, "informe de tasaciones", ln=True, align="C")
        with open("tasaciones.csv", "r") as f:
            for linea in f:
                pdf.cell(200, 10, linea.strip(), ln=True)

        pdf.add_page()
        pdf.cell(200, 10, "informe de precio del oro", ln=True, align="C")
        with open("precioOro.csv", "r") as f:
            for linea in f:
                pdf.cell(200, 10, linea.strip(), ln=True)

        #insertar grafico del oro
        pdf.add_page()
        pdf.cell(200, 10, "grafico de evolucion del precio del oro", ln=True, align="C")
        pdf.image("graficoPrecioOro.png", x=10, y=30, w=180)

        pdf.output("informeCompleto.pdf")
        print("informe completo exportado a informeCompleto.pdf")
