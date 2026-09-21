tipo_imovel = input("Digite o tipo do imóvel (comercial, casa ou apartamento): ").strip().lower()
consumo_agua = float(input("Digite o consumo mensal de água em m³: "))

# Verificação das regras de negócio
if tipo_imovel == "comercial":
	print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif tipo_imovel == "apartamento" and consumo_agua < 10:
	print("Consumo econômico – excelente controle de água!")
elif tipo_imovel in ["apartamento", "casa"] and consumo_agua <= 25:
	print("Consumo moderado – dentro do padrão residencial.")
else:
	print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
