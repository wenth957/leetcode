import os
import pdfkit
from PyPDF2 import PdfFileMerger


class Pdf:

    def __init__(self, config, is_pdf=False, is_merge=False):
        self.config = config
        self.is_pdf = is_pdf
        self.is_merge = is_merge

    def get_files(self, dir_path):
        names = os.listdir(dir_path)
        return names

    def html2pdf(self, input_path, pdf_path, verbose=False):
        filenames = self.get_files(input_path)
        for filename in filenames:
            in_path = os.path.join(input_path, filename)
            file_name, _ = os.path.splitext(filename)
            file_path = pdf_path + "\\" + file_name + '.pdf'
            out_path = os.path.join(file_path)
            print('____________转换html为pdf文件_______________', '\n', out_path)
            pdfkit.from_file(
                input=in_path, output_path=out_path,
                configuration=self.config['configuration'],
                options=self.config['options'], verbose=verbose)

    def mergepdf(self, pdf_path, target_path):
        file_merger = PdfFileMerger()
        pdfnames = self.get_files(pdf_path)
        length = len(pdfnames)
        for idx, pdfname in enumerate(pdfnames):
            pdf_name = os.path.join(pdf_path, pdfname)
            print(f"{pdf_name}   被合并")
            remain = length - idx - 1
            print(f"还剩{remain}个文件需要合并")
            file_merger.append(pdf_name)
        file_merger.write(target_path)
        print("——————合并完成——————" * 5)  # 合并pdf文件


if __name__ == '__main__':
    input_path = r'E:\vs_code_python\days_100\reptile\geek_crawler\algs'
    pdf_path = r"E:\vs_code_python\days_100\reptile\geek_crawler\algs\pdf"
    merge_path = pdf_path + r'\merge.pdf'
    wkthmptopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config_pdf = pdfkit.configuration(wkhtmltopdf=wkthmptopdf)
    options = {
        "encoding": "UTF-8",
        "custom-header": [('Accept-Encoding', 'gzip')],
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        # 'encoding': "UTF-8",
        'no-outline': False
    }

    config = {'configuration': config_pdf, 'options': options}

    # pdf = Pdf(config, is_pdf=True, is_merge=True)
    pdf = Pdf(config, is_merge=True)

    if pdf.is_pdf is True and pdf.is_merge is True:
        pdf.html2pdf(input_path, pdf_path)
        pdf.mergepdf(pdf_path, merge_path)
    elif pdf.is_pdf is True:
        pdf.html2pdf(input_path, pdf_path)
    else:
        pdf.mergepdf(pdf_path, merge_path)
