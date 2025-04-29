import pandas as pd
import query, builder


question = "Crie um gráfico ordenando os times com mais pontos"
kind = "colunas"
table = pd.DataFrame.from_dict({
    'Team': ["Arsenal", "Manchester United", "Chelsea"],
    'Points': ["92", "19", "65"],
    'Year': ["2004", "2004", "2004"]
})

answer = query.find_answer(question, table)
chart = builder.create_chart(answer, kind)

print(chart)
