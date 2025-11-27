from fpdf import FPDF
from log.log import Log

log = Log()

class ExportadorPDF:
    def exportarInformeCompleto(self):
        try:
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

            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, "Precio del oro", ln=True)
            pdf.set_font("Arial", "", 10)
            with open("precioOro.csv", "r") as f:
                for linea in f:
                    pdf.cell(0, 8, linea.strip(), ln=True)

            #si los gráficos ya existen se añaden
            try:
                pdf.add_page()
                pdf.set_font("Arial", "B", 12)
                pdf.cell(0, 10, "Grafico: Cantidad de oro vendido por cliente", ln=True)
                pdf.image("graficoOroPorCliente.png", x=10, y=30, w=180)
            except Exception:
                log.warning("No se encontró graficoOroPorCliente.png, se omitirá en el PDF")

            try:
                pdf.add_page()
                pdf.set_font("Arial", "B", 12)
                pdf.cell(0, 10, "Grafico: Total de ventas por mes", ln=True)
                pdf.image("graficoVentasPorMes.png", x=10, y=30, w=180)
            except Exception:
                log.warning("No se encontró graficoVentasPorMes.png, se omitirá en el PDF")

            pdf.output("informeCompleto.pdf")
            log.info("Informe completo generado en informeCompleto.pdf")

        except Exception as e:
            log.error(f"Error al generar informe completo en PDF: {e}")
