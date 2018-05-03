import tinysegmenter
statement = 'アリムタ投与中非ステロイド性抗炎症剤（NSAIDs使用'
tokenized_statement = tinysegmenter.tokenize(statement)
print(tokenized_statement)
