nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
porcentagem_frequencia = int(input("Digite a quantidade da frequencia:"))

media = (nota1 + nota2) / 2

porcentagem_frequencia_min = (200 * 75) / 100

frequencia_do_aluno = (porcentagem_frequencia * 100) / 200

frequencia_do_aluno = porcentagem_frequencia > porcentagem_frequencia_min

aprovado = frequencia_do_aluno > 75 and media >= 7.0

print(f"A media do aluno foi: {media:.2f}. "f"Ele foi aprovado: {aprovado}")