from abc import ABC, abstractmethod
from math import ceil

class Relatorio(ABC):

    def iniciar_processo(self):
        print(f"[Sistema Central] Exportação iniciada: {type(self).__name__}")

        @abstractmethod
        def exportar(self, titulo, dados):
            pass

class RelatorioPDF(Relatorio):
    LINHAS_POR_PAGINA = 25

    def exportar(self, titulo, dados):
        paginas = max(1, ceil(len(dados)/ self.LINHAS_POR_PAGINA))
        arquivo = f"{titulo.lower().replace(' ', '-')}.pdf"
        print(f"PDF {arquivo} gerado: {len(dados)} linhas em {paginas} pagina(s).")
        return arquivo
class RelatorioExcel(Relatorio):
    def exportar(self, titulo, dados):
        if len(dados) == 0:
            print("Excel: exportação cancelada! Não há dados para gerar a planilha.")
            return None
        total = sum(valor for _, valor in dados)
        arquivo = f"{titulo.lower().replace(' ', '-')}.xlsx"
        print(f"Excel '{arquivo}' gerado: {len(dados)} linhas + linha de total = R$ {total:.2f}.")
        return arquivo


class RelatorioHTML(Relatorio):
    def exportar(self, titulo, dados):
        linhas = "".join(f"<tr><td>{item}</td><td>{valor:.2f}</td></tr>" for item, valor in dados)
        html = f"<h1>{titulo}</h1><table>{linhas}</table>"
        arquivo = f"{titulo.lower().replace(' ', '_')}.html"
        print(f"HTML '{arquivo}' gerado com {len(dados)} linhas de tabela ({len(html)} caracteres).")
        return arquivo



DADOS_PADRAO = [(f"Produto {i}", i * 10.5) for i in range(1, 31)]  # 30 linhas


def processar_lote(lista_de_objetos, titulo="Relatorio Padrao", dados=None):

    if dados is None:
        dados = DADOS_PADRAO
    arquivos = []
    for item in lista_de_objetos:
        item.iniciar_processo()
        arquivo = item.exportar(titulo, dados)
        if arquivo is not None:
            arquivos.append(arquivo)
        print("-" * 30)
    return arquivos





pdf = RelatorioPDF()
excel = RelatorioExcel()
html = RelatorioHTML()


lote = [pdf, excel, html, pdf]

dados_vendas = [(f"Produto {i}", i * 10.5) for i in range(1, 61)]  # 60 linhas


print("\n--- INICIANDO PROCESSAMENTO EM LOTE (loop direto) ---")
for item in lote:
    item.iniciar_processo()

    item.exportar("Vendas Mensais", dados_vendas)
    print("-" * 30)


print("\n--- PROCESSAR_LOTE(lote) ---")
arquivos = processar_lote(lote)
print(f"Arquivos gerados: {arquivos}")


print("\n--- PROCESSAR_LOTE(lote, dados vazios) ---")
arquivos = processar_lote(lote, "Relatorio Vazio", [])
print(f"Arquivos gerados: {arquivos}")