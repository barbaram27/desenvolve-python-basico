{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "34063cfb-3b0f-4e67-974b-4b80e8473898",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Emojis disponíveis:\n",
      ":smile: => 😄\n",
      ":heart: => ❤️\n",
      ":thumbsup: => 👍\n",
      ":cry: => 😢\n",
      ":fire: => 🔥\n",
      ":clap: => 👏\n",
      ":rocket: => 🚀\n",
      ":thinking_face: => 🤔\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Digite uma frase usando os códigos acima:  Olá! :smile: Vamos lançar! :rocket:\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Frase com emojis:\n",
      "Olá! 😄 Vamos lançar! 🚀\n"
     ]
    }
   ],
   "source": [
    "import emoji\n",
    "\n",
    "# Lista de emojis disponíveis com códigos no padrão curto\n",
    "emojis_disponiveis = {\n",
    "    \":smile:\": \"😄\",\n",
    "    \":heart:\": \"❤️\",\n",
    "    \":thumbsup:\": \"👍\",\n",
    "    \":cry:\": \"😢\",\n",
    "    \":fire:\": \"🔥\",\n",
    "    \":clap:\": \"👏\",\n",
    "    \":rocket:\": \"🚀\",\n",
    "    \":thinking_face:\": \"🤔\"\n",
    "}\n",
    "\n",
    "# Mostra os emojis disponíveis\n",
    "print(\"Emojis disponíveis:\")\n",
    "for cod, simb in emojis_disponiveis.items():\n",
    "    print(f\"{cod} => {simb}\")\n",
    "\n",
    "# Solicita uma frase codificada\n",
    "frase = input(\"\\nDigite uma frase usando os códigos acima: \")\n",
    "\n",
    "# Converte para emojis reais\n",
    "frase_emojizada = emoji.emojize(frase, language='alias')  # <- ESSENCIAL\n",
    "\n",
    "# Mostra a frase com emojis\n",
    "print(\"\\nFrase com emojis:\")\n",
    "print(frase_emojizada)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f80a2e16-4ae1-420a-b842-52a5e353cf84",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
