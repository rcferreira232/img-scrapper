# Gerador de Dataset de Imagens

Este script realiza a coleta automática de imagens utilizando a biblioteca **icrawler**. As imagens são organizadas em duas categorias: **backgrounds** e **objects**.

Após o download, o script executa um pós-processamento básico nas imagens de fundo, incluindo:

- Conversão para o formato RGB;
- Redimensionamento para 640x640 pixels;
- Remoção de arquivos corrompidos ou incompatíveis.

O objetivo é gerar um conjunto de imagens padronizado para utilização em projetos de visão computacional, treinamento de modelos e experimentos de processamento de imagens.
