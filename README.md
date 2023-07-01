# acr-branch

Extensao verifica se no merge request a source branch e target branch sao iguais

1. Atributo data contem uma lista de objetos referente a mensagem que deve ser adicionado caso a condicao das branchs nao seja atendida
2. Atributo message, dentro do objeto da lista, se refere a mensagem em si que deve ser comentada

Arquivo config.json

```json
{
  "data": [
    {
      "message": "Branch target e branch source devem ser iguais"
    }
  ]
}
```
