import os
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from docx import Document
from fpdf import FPDF

def select_file():
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo .docx",
        filetypes=(("Arquivos DOCX", "*.docx"), ("Todos os arquivos", "*.*"))
    )
    if file_path:
        entry_file.delete(0, 'end')
        entry_file.insert(0, file_path)

def select_output_folder():
    folder_path = filedialog.askdirectory(title="Selecione uma pasta de saída")
    if folder_path:
        entry_output.delete(0, 'end')
        entry_output.insert(0, folder_path)

def convert_to_pdf():
    docx_path = entry_file.get()
    output_folder = entry_output.get()

    if not os.path.isfile(docx_path):
        messagebox.showerror("Erro", "Arquivo .docx inválido ou não selecionado.")
        return

    if not os.path.isdir(output_folder):
        messagebox.showerror("Erro", "Pasta de saída inválida ou não selecionada.")
        return

    try:
        document = Document(docx_path)
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for paragraph in document.paragraphs:
            pdf.multi_cell(0, 10, paragraph.text)

        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(docx_path))[0] + ".pdf")
        pdf.output(output_file)
        messagebox.showinfo("Sucesso", f"Arquivo convertido com sucesso: {output_file}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante a conversão: {e}")

# Configuração da interface
root = Tk()
root.title("Conversor DOCX para PDF")

Label(root, text="Arquivo .docx:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_file = Entry(root, width=40)
entry_file.grid(row=0, column=1, padx=10, pady=10)
Button(root, text="Selecionar", command=select_file).grid(row=0, column=2, padx=10, pady=10)

Label(root, text="Pasta de saída:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_output = Entry(root, width=40)
entry_output.grid(row=1, column=1, padx=10, pady=10)
Button(root, text="Selecionar", command=select_output_folder).grid(row=1, column=2, padx=10, pady=10)

Button(root, text="Iniciar Conversão", command=convert_to_pdf).grid(row=2, column=0, columnspan=3, pady=20)

root.mainloop()
