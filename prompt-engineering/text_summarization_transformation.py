client = OpenAI(api_key="<OPENAI_API_TOKEN>")

marketing_message = "Introducing our latest collection of premium leather handbags. Each bag is meticulously crafted using the finest leather, ensuring durability and elegance. With a variety of designs and colors, our handbags are perfect for any occasion. Shop now and experience the epitome of style and quality."


# Craft a prompt that translates
prompt = f""" 
translate the marketing_message delimitted by triple backtiks into french,spanish and japanese
```{marketing_message}```
"""
 
response = get_response(prompt)

print("English:", marketing_message)
print(response)


# <script.py> output:
#     English: Introducing our latest collection of premium leather handbags. Each bag is meticulously crafted using the finest leather, ensuring durability and elegance. With a variety of designs and colors, our handbags are perfect for any occasion. Shop now and experience the epitome of style and quality.
#     Sure! Here are the translations of the marketing message into French, Spanish, and Japanese:
    
#     **French:**
#     ``` 
#     Découvrez notre dernière collection de sacs à main en cuir haut de gamme. Chaque sac est soigneusement fabriqué à partir du meilleur cuir, garantissant durabilité et élégance. Avec une variété de designs et de couleurs, nos sacs à main sont parfaits pour toutes les occasions. Achetez maintenant et vivez l'apogée du style et de la qualité.
#     ```
    
#     **Spanish:**
#     ```
#     Presentamos nuestra última colección de bolsos de cuero premium. Cada bolso está meticulosamente elaborado con el mejor cuero, asegurando durabilidad y elegancia. Con una variedad de diseños y colores, nuestros bolsos son perfectos para cualquier ocasión. Compra ahora y experimenta la esencia del estilo y la calidad.
#     ```
    
#     **Japanese:**
#     ```
#     最新のプレミアムレザー ハンドバッグ コレクションをご紹介します。各バッグは最高級のレザーを使用して丁寧に作られており、耐久性とエleganceを保証します。さまざまなデザインと色が揃った私たちのハンドバッグは、あらゆる場面にぴったりです。今すぐお買い物をして、スタイルと品質の極みを体験してください。
#     ``` 
    
#     Let me know if you need any further assistance!