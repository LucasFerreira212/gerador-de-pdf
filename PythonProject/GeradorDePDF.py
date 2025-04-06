descricao_projeto = input("Digite a descrição do projeto: ")
dias_previstas = input("Digite a quantidade de dias previstas: ")
valor_diaria = input("Digite o valor do dia trabalhado: ")
prazo = input("Digite o prazo estimado: ")

valor_total = int(dias_previstas) * float(valor_diaria)

from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")
pdf.image("template.png", x=0, y=0)

pdf.text(115, 145, descricao_projeto)
pdf.text(115, 160, dias_previstas)
pdf.text(115, 175, valor_diaria)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))


pdf.output("Orçamento.pdf")

print("Orçamento gerado com sucesso!")
