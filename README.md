# acr-branch

Extensao verifica se no merge request a source branch e target branch atendem as configurações desejadas

- data
    - Contem uma lista de objetos
    - type
        - Tipo de verificação
        - SOURCE_TARGET_EQUALITY: Se a branch target e source são iguais
        - TARGET_DENY_LIST: Se a branch target é uma branch que não pode entregar merge request
    - message
        - Mensagem que ira apresentar
        - Permite o bind do parametro ${BRANCH_TARGET}
    - denyList
        - Usado apenas para o TARGET_DENY_LIST por hora
        - Trata-se de uma lista de nome de branches bloqueadas para abrir merge request
    - processorArgs
        - Configuração opcional encaminhada ao processador junto com o comentário
        - `resolutionPolicy.allowedResolvers`: usernames do GitLab autorizados a resolver manualmente a thread

`processorArgs` pode ser definido globalmente na raiz da configuração para valer para todas as regras, ou dentro de uma regra específica para valer apenas para os comentários gerados por ela. A configuração da regra tem precedência sobre a configuração global.

Arquivo config.json

```json
{
  "stage": "static",
  "processorArgs": {
    "resolutionPolicy": {
      "allowedResolvers": ["usuario_x", "usuario_y"]
    }
  },
  "data": [
    {
      "type": "SOURCE_TARGET_EQUALITY",
      "message": "Branch target e branch source devem ser iguais"
    },
    {
      "type": "TARGET_DENY_LIST",
      "denyList": [
      ],
      "message": "Não é permitido abrir merge request direto para a branch `${BRANCH_TARGET}`"
    }
  ]
}
```

Para limitar a resolução a uma regra, coloque o mesmo bloco `processorArgs` dentro do objeto dessa regra. Quando o processador detectar que outro usuário resolveu a thread, ele a reabre e publica um aviso.
