Objetivo
Aprender o fluxo de trabalho do Spec-Driven Development (SDD) utilizando a versão moderna do
OpenSpec. Você usará comandos de chat para iniciar e gerenciar uma Change (Mudança), onde a IA
guiará a criação dos artefatos.

Conceitos Chave
• Change (Mudança): A unidade de trabalho no OpenSpec. Uma mudança contém todos os
artefatos necessários (Proposta, Design, Tarefas) para implementar uma feature.
• Artifact-Driven: O fluxo é guiado pela criação sequencial de documentos (artifacts).
• Skill Commands: Comandos especiais de chat (iniciados por /opsx:) que ativam habilidades
específicas da IA.

Passos Detalhados
Legenda de Comandos:
• Chat: Comando enviado no chat da IA (Copilot/Gemini).
• Terminal: Comando digitado no terminal do VS Code.
1. Iniciar uma Nova Mudança (Change)
Em vez de usar comandos de terminal complexos ou configurar prompts manualmente, você usará a
skill /opsx:new.
1. Abra o Chat da IA no VS Code. 2. Envie o comando:
/opsx:new add-subjects
(Ou descreva o que você quer: "Quero criar o gerenciamento de disciplinas")
A IA irá:
1. Criar a pasta openspec/changes/add-subjects.
2. Configurar o fluxo de trabalho (Schema).
3. Mostrar o status da mudança e o próximo passo.
2. Criar os Artefatos (/opsx:continue)

O OpenSpec funciona em etapas. Após iniciar, a IA lhe dirá qual é o próximo artefato a ser criado
(provavelmente o proposal).
Para gerar o artefato, envie no Chat:
/opsx:continue
A IA irá ler o template, o contexto do projeto e gerará o conteúdo do arquivo para você. Revise o
conteúdo gerado e save o arquivo se estiver correto.
Repita o /opsx:continue sempre que a IA indicar que há um próximo passo, até que todos os artefatos
(Proposal, Design, Tasks) estejam prontos.
3. Implementar a Mudança (/opsx:apply)
Quando a lista de tarefas (tasks.md) estiver pronta, você começará a implementação.
Envie no Chat:
/opsx:apply
A IA lerá as tarefas e começará a sugerir o código (Python, XanoScript) ou as alterações necessárias.

Resumo dos Comandos
Comando Função
/opsx:new <nome> Inicia uma nova mudança (pasta em changes/).
/opsx:continue Gera o próximo artefato (ex: proposal, design).
/opsx:apply Começa a executar as tarefas de implementação.

Dica Importante
Se em algum momento a IA parecer perdida, lembre-a: "Você está usando o OpenSpec Skills.
Verifique o status da change atual."
Escopo de Tarefas (CRÍTICO)
O arquivo tasks.md deve conter APENAS as tarefas solicitadas pelo usuário.
• Se o usuário pedir "criar tabela X", NÃO adicione automaticamente: API CRUD, testes, ou
frontend.
• Se o usuário pedir "criar API para Y", NÃO adicione automaticamente: testes ou frontend.
• Adicione tarefas extras SOMENTE se explicitamente solicitado.
Responsabilidade da IA
SUA TAREFA TERMINA NA GERAÇÃO DOS ARQUIVOS.

• Criar/editar arquivos (.xs, specs/spec.md, tasks.md)
• Marcar tasks completas em tasks.md
• Atualizar todos.md
• NÃO tente fazer push, sync ou deploy para Xano
• NÃO procure ou invoque ferramentas push_all_changes_to_xano
O desenvolvedor é responsável por revisar e fazer push manualmente.

> **Instrução:** Cole o conteúdo acima no seu arquivo `AGENTS.md`.

**Passo 3 - Salve o arquivo:**
- Pressione `Ctrl+S` para salvar. **No Terminal**:
```bash
git add AGENTS.md
git commit -m "docs: configura AGENTS.md inicial"

Nota Importante: Este é o AGENTS.md básico para começar. Na Tarefa 10, você expandirá este
arquivo com regras mais avançadas e detalhadas (Segurança, OpenSpec detalhado, Commits, etc.).
Por enquanto, essas 7 regras são suficientes!

Sobre o Arquivo na Raiz: O arquivo AGENTS.md deve ficar na raiz do seu projeto para que você tenha
total controle sobre ele. Ele é o "cérebro" das instruções para seu assistente de IA.

2. Criar a Proposal (Proposta) via Slash Command
Agora utilizaremos o poder da IA integrada ao OpenSpec para criar nossa primeira proposta de forma
automatizada. No Gemini Code Assist, usaremos um Slash Command específico que automatiza a
criação da estrutura.
Como criar a proposta:
1. No Chat: Ative a chave Agent: No chat do Gemini, certifique-se de que a chave
seletora Agent (localizada logo abaixo da caixa de texto do prompt) está ligada. Isso permite
que a IA execute ações como criar pastas e gravar arquivos.
2. Abra o arquivo AGENTS.md (na raiz do seu projeto) no editor do VS Code.
3. No Chat: Abra o chat do Gemini Code Assist (ícone na barra lateral ou Ctrl+I).

4. No Chat: Envie exatamente este prompt (focado no planejamento):
/opsx:new Baseado no @AGENTS.md, defina o esquema da tabela 'subjects' com os campos id
(auto), name (text), teacher (text), hours (int), user_id (FK para a tabela de autenticação do Xano:
user/users)
5. O Gemini irá:
- Criar automaticamente uma nova pasta em `openspec/changes/` (ex: `criar-table-subjects`).
- Gerar o arquivo `proposal.md` usando cabeçalhos obrigatórios (`# Change:`, `## Why:`, etc.).
- Gerar o arquivo `specs/spec.md` (dentro de uma subpasta `specs/`) com o detalhamento técnico
da tabela.
- Gerar o arquivo `tasks.md` com a lista de tarefas técnicas em **Inglês**.

---

### 3. Revisar a Proposal Gerada

Antes de partir para a implementação, é fundamental revisar o que a IA planejou.

1. **Abra a nova pasta** criada dentro de `openspec/changes/`.
2. **Revise o `proposal.md`:** Verifique se ele segue a estrutura de cabeçalhos (`# Change: <id>`,
`## Why:`, etc.) e se a descrição está clara.
3. **Revise o `specs/spec.md`:** Verifique se ele usa os termos `### Requirement:` e `####
Scenario:`, e se os campos da tabela `subjects` estão corretos.
4. **Revise o `tasks.md`:** Veja se as tarefas estão em inglês e descrevem os passos técnicos (ex:
criar arquivo `.xs`).

---

### 4. Implementar a Mudança (Apply)

Agora, com o plano aprovado, utilizaremos o Slash Command de aplicação do OpenSpec.

1. **No Chat:** Use o comando `/opsx:apply` seguido do nome da pasta da sua proposta:
```text

/opsx:apply create-subjects-table
(Dica: Se você não sabe o nome exato, verifique o nome da pasta em openspec/changes/)
2. No Chat: Revise a criação do arquivo:
o O Gemini lerá a proposta e oferecerá para criar o arquivo na pasta correspondente
(ex: tables/).
o Clique em "Accept" para confirmar a criação do arquivo.
o IMPORTANTE: Verifique se o arquivo foi criado na pasta correta seguindo o padrão do
XanoScript.

3. No Terminal: Envie para o Xano (Push):
o No VS Code, abra o arquivo que foi criado (ele deve estar aberto após você clicar em
Accept).
o Abra a Paleta de Comandos: Ctrl+Shift+P
o Digite e selecione: XanoScript: Push Stage Changes to Xano
o Aguarde a conclusão.
4. Valide no Xano:
o Acesse seu dashboard do Xano no navegador.
o Confirme se a tabela subjects foi criada com sucesso.

Se conseguiu criar a tabela no Xano: Parabéns! Você acabou de fazer implementação completa
com IA!

5. Finalizar a Proposta
Agora que a implementação está completa, vamos finalizar o ciclo no OpenSpec:
1. � No Chat: Use o comando para arquivar e finalizar a mudança:
/opsx:archive
2. Marque as tarefas como concluídas:
o No Explorer, abra a pasta da sua proposta em openspec/changes/archive/.
o Abra o arquivo tasks.md.
o Altere [ ] para [x] em todas as tarefas (se a IA não fez isso).
3. Isso irá "consolidar" sua proposta, guardando o que você construiu como a documentação
oficial do projeto.

6. No Terminal: Commitar no Git

# (Recomendado) Crie uma branch para abrir PR (fluxo da Tarefa 05)
git checkout -b feat/openspec-subjects

git add .
git commit -m "feat: implementa primeira tabela via OpenSpec"
git push origin feat/openspec-subjects
(Lembre-se de abrir o Pull Request e fazer o Merge no GitHub, como aprendeu na Tarefa 05).

Entregáveis
1. Screenshot da pasta openspec/changes/archive/ mostrando sua proposta arquivada.
2. Link do repositório GitHub com a proposta arquivada.
Critérios de Avaliação
• Proposta criada usando o Slash Command /opsx:new.
• Arquivos proposal.md, specs/spec.md e tasks.md gerados e revisados seguindo
o @AGENTS.md.
• Tabela subjects criada no Xano via XanoScript.
• Mudança arquivada corretamente (pasta movida para archive/).
• Código enviado para o repositório GitHub.
Dicas para problemas comuns
• A IA não cria todos os arquivos ou ignora os cabeçalhos obrigatórios:
o Certifique-se de que o seu AGENTS.md tem a regra de "Arquivos Obrigatórios".
o Reforce com /opsx:continue.
• Não consigo editar o arquivo AGENTS.md ou não entendo o que adicionar:
o O AGENTS.md deve ficar na raiz do projeto.
• Ao enviar o comando /opsx:new, a IA não cria os arquivos:
o Certifique-se de que a extensão OpenSpec Skills está instalada.
o Verifique se você está usando a IA correta (Copilot/Gemini).
• Erro de validação:
o Verifique se os arquivos proposal.md, specs/spec.md e tasks.md existem e têm
conteúdo válido.
o O proposal.md deve ter os cabeçalhos obrigatórios.

• Erro ao arquivar (archive):
o Tente pedir novamente: "Archive this change".
o Se falhar, faça manualmente movendo a pasta para openspec/changes/archive/.
• O comando de arquivar não fez nada:
o Se falhar, você pode fazer manualmente:
▪ Mova a pasta da proposta (ex: add-subjects-table/) para dentro de archive/.

• A IA criou o arquivo fora das pastas padrão:
o Se isso acontecer, não aceite a sugestão ou apague o arquivo criado.
o Reforce o comando no chat: "Siga as orientações do XanoScript e crie o arquivo na
pasta correta para este tipo de recurso."

• A tabela subjects não foi criada no Xano após fazer Push:
o Certifique-se de que o arquivo .xs foi criado e está aberto no VS Code.
o Verifique se fez XanoScript: Push Stage Changes to Xano (não apenas Save).
o Recarregue o painel do Xano no navegador (F5).
o Se a tabela não aparecer mesmo após Push, pode haver erro de sintaxe - procure por
marcas de erro no VS Code.

• Não consigo sincronizar com o Xano após criar o arquivo .xs:
o Certifique-se de que está autenticado no XanoScript (XanoScript: Login to Xano).
o Verifique se selecionou o workspace correto (XanoScript: Select workspace).
o Tente fazer XanoScript: Pull latest changes primeiro, depois o Push.
• Conflito de Git ao tentar committar a proposta arquivada:
o Você pode ter alterado a proposta enquanto alguém (ou você em outro computador)
também alterou.
o Faça git pull origin main antes de fazer commit.
o Resolva qualquer conflito manualmente.
• A proposta não aparece em openspec/changes/archive/ no GitHub após push:
o Você fez git add . para incluir toda a pasta?
o Git pode não rastrear pastas vazias - certifique-se de que há pelo menos um arquivo na
pasta (ex: .gitkeep).
o Aguarde alguns segundos e recarregue o GitHub.

Dica: O OpenSpec ajuda a manter um "diário de bordo" técnico do seu projeto. No futuro, quando
você usar IAs como o Gemini ou Claude, elas lerão essas proposals para saber exatamente o que
você quer construir.