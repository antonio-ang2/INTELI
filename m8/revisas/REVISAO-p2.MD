# REVISÃO PROGRAMAÇÃO:

# COESÃO

Coesão refere-se à medida em que as responsabilidades de um módulo ou classe são estreitamente relacionadas. Uma classe coesa faz "uma coisa e faz bem". Quando a coesão é alta, o módulo ou a classe tem um propósito bem definido, o que torna o software mais compreensível, fácil de manter e menos propenso a erros.

# ACOPLAMENTO

Acoplamento refere-se ao grau em que um módulo ou classe depende de outros módulos ou classes. O objetivo é ter o menor acoplamento possível, ou seja, cada módulo ou classe deve operar de forma tão independente quanto possível. Um baixo acoplamento facilita a manutenção, o teste e a reutilização do código.

## Inversão de depedência

A Inversão de Dependência é um dos cinco princípios SOLID do design orientado a objetos, e refere-se a uma forma específica de reduzir o acoplamento

entre módulos ou classes de um software. A ideia principal é que módulos de alto nível, que fornecem funcionalidades complexas, não devem depender de módulos de baixo nível, que fornecem operações detalhadas. Em vez disso, ambos devem depender de abstrações.

Para implementar a inversão de dependência, geralmente seguimos dois princípios fundamentais:

- Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.
- Abstrações não devem depender de detalhes. Detalhes devem depender de abstrações.

Isso é frequentemente alcançado através do uso de interfaces (em linguagens que suportam) ou classes abstratas.



# Desing Patterns em Python

A utilização de design patterns é essencial para promover o baixo acoplamento e a alta coesão em sistemas de software. Padrões como Singleton, Factory, Strategy e Dependency Injection são técnicas que incentivam a separação de responsabilidades e a dependência em interfaces ou abstrações, permitindo que componentes interajam sem depender diretamente uns dos outros. Isso leva à redução do acoplamento. Por outro lado, padrões como Composite, Observer e Command incentivam a criação de componentes com funções bem definidas e limitadas, reforçando a coesão. Ao adotar esses padrões, os desenvolvedores podem construir sistemas mais modulares, escaláveis e fáceis de manter.  


## Strategy Pattern

O Strategy Pattern é um padrão de projeto que permite que você defina uma família de algoritmos, encapsule cada um deles e os torne intercambiáveis. Isso significa que você pode alterar o comportamento de uma classe sem alterar seu código, apenas trocando a "estratégia" ou algoritmo que ela usa.

A Inversão de Dependência é um princípio da programação orientada a objetos que sugere que módulos de alto nível não devem depender de módulos de baixo nível, mas ambos devem depender de abstrações. Em outras palavras, em vez de depender de detalhes concretos, seu código deve depender de interfaces ou classes abstratas.

```
strategy

class S3Strategy():
    def upload(self, file):
        # código para upload no S3
        print("Uploading to S3...")

class GCPStrategy():
    def upload(self, file):
        # código para upload no GCP
        print("Uploading to GCP...")

class CloudUploader:
    def __init__(self, service):
        self.service = service

    def upload(self, file):
        if self.service == "S3":
            S3Strategy().upload(file)
        elif self.service == "GCP":
            GCPStrategy().upload(file) ```

```


```
strategy + inversão
from abc import ABC, abstractmethod

class CloudStrategy(ABC):
    @abstractmethod
    def upload(self, file):
        pass

class S3Strategy(CloudStrategy):
    def upload(self, file):
        # código para upload no S3
        print("Uploading to S3...")

class GCPStrategy(CloudStrategy):
    def upload(self, file):
        # código para upload no GCP
        print("Uploading to GCP...")

class CloudUploader:
    def __init__(self, strategy: CloudStrategy):
        self.strategy = strategy

    def upload(self, file):
        self.strategy.upload(file)
 ```


 ## OBSERVER PATTERN

 O Observer Pattern é um padrão de projeto que define uma dependência entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são automaticamente notificados e atualizados. É amplamente usado em sistemas que requerem que um componente mantenha outros componentes informados sobre mudanças.

 Coesão: O uso do Observer Pattern aumenta a coesão, já que as responsabilidades estão mais claramente definidas. No exemplo, a lógica de notificação é claramente separada da lógica de publicação.

Acoplamento: O padrão reduz o acoplamento, pois a classe Blog agora não precisa saber os detalhes de como notificar cada assinante. Ela apenas comunica que um evento ocorreu, e é responsabilidade de cada observador decidir como responder.

O Robot Operating System (ROS) utiliza uma variante do Observer Pattern em sua infraestrutura de comunicação. Em ROS, os "publishers" publicam mensagens em tópicos, e os "subscribers" se inscrevem nesses tópicos para receber as mensagens. A relação entre publishers e subscribers em ROS é semelhante à relação entre observáveis e observadores no Observer Pattern.

Vamos ver um exemplo simplificado de como isso funcionaria em um cenário hipotético, onde um subscriber força sua adição a um publisher quando se inscreve em um tópico:



### Observer pattern no ROS

O Robot Operating System utiliza uma variante do Observer Pattern em sua infraestrutura de comunicação. Em ROS, os "publishers" publicam mensagens em tópicos, e os "subscribers" se inscrevem nesses tópicos para receber as mensagens. A relação entre publisher e subscribers em ROS é semelhante à relação entre observáveis e observadores no Observer Pattern. 




Design patterns são soluções generalizadas para problemas recorrentes no design de software. Eles representam as melhores práticas utilizadas por desenvolvedores ao longo do tempo para resolver problemas específicos. Vou explicar brevemente os padrões Observer e Strategy, junto com exemplos.

### Observer Pattern:

**Descrição:**
O padrão Observer é usado para definir uma dependência de um para muitos entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente.

**Exemplo:**
Considere um sistema onde um objeto (sujeito) mantém uma lista de observadores e os notifica sempre que seu estado muda. Por exemplo, um sistema de monitoramento meteorológico, onde várias exibições (observadores) precisam ser atualizadas quando a temperatura muda.

```python
# Observer Interface
class Observer:
    def update(self, temperature):
        pass

# Concrete Observer
class TemperatureDisplay(Observer):
    def update(self, temperature):
        print(f"Nova temperatura: {temperature} C")

# Subject
class WeatherStation:
    def __init__(self):
        self._temperature = None
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify_observers()

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

# Uso
weather_station = WeatherStation()

display1 = TemperatureDisplay()
display2 = TemperatureDisplay()

weather_station.add_observer(display1)
weather_station.add_observer(display2)

weather_station.set_temperature(25.5)
```

Neste exemplo, `TemperatureDisplay` é um observador que exibe a temperatura sempre que ela é atualizada no `WeatherStation`.

### Strategy Pattern:

**Descrição:**
O padrão Strategy é usado quando temos um conjunto de algoritmos intercambiáveis e queremos que o cliente escolha o algoritmo a ser usado dinamicamente.

**Exemplo:**
Considere um sistema de pagamento onde diferentes estratégias de pagamento podem ser escolhidas (cartão de crédito, PayPal, etc.).

```python
# Strategy Interface
class PaymentStrategy:
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Pagamento de {amount} via cartão de crédito.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Pagamento de {amount} via PayPal.")

# Context
class ShoppingCart:
    def __init__(self, payment_strategy):
        self._items = []
        self._payment_strategy = payment_strategy

    def add_item(self, item):
        self._items.append(item)

    def checkout(self):
        total_amount = sum(item.price for item in self._items)
        self._payment_strategy.pay(total_amount)

# Uso
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

cart1 = ShoppingCart(credit_card_payment)
cart2 = ShoppingCart(paypal_payment)

cart1.add_item(Item("Produto A", 50))
cart2.add_item(Item("Produto B", 30))

cart1.checkout()
cart2.checkout()
```

Neste exemplo, `CreditCardPayment` e `PayPalPayment` são estratégias intercambiáveis que implementam a interface `PaymentStrategy`. O cliente (`ShoppingCart`) pode escolher a estratégia de pagamento desejada dinamicamente.
# REQUISITOS DE SOFTWARE

Requisitos funcionais são especificações detalhadas que descrevem as funções, características e interações que um sistema ou software deve possuir. Eles definem o que o sistema deve fazer em resposta a entradas específicas ou em condições determinadas. Em outras palavras, os requisitos funcionais descrevem as funcionalidades que o sistema deve oferecer para atender às necessidades e expectativas dos usuários e dos stakeholders.

## FUNCIONAIS

1.1. Como Definir Requisitos Funcionais
Entendimento do Negócio: Antes de tudo, é crucial entender o domínio do negócio e os objetivos do projeto. Isso fornece um contexto para a definição dos requisitos.

Reuniões e Workshops: Organize sessões de brainstorming com stakeholders, incluindo gerentes de projeto, desenvolvedores, designers e, claro, representantes dos usuários finais.

Use Casos e Histórias de Usuários: Descreva cenários específicos de como os usuários interagirão com o sistema. Isso ajuda a visualizar as funcionalidades necessárias e a identificar possíveis lacunas.

Prototipagem: Crie protótipos ou mockups do sistema para visualizar como ele funcionará. Isso pode ajudar a identificar requisitos adicionais e a obter feedback antecipado.


O cliente, seja ele um usuário final ou um representante de uma organização cliente, é fundamental na definição de requisitos funcionais. Aqui estão as razões:

Perspectiva do Usuário: O cliente oferece uma perspectiva única, a do usuário. Eles podem fornecer insights sobre o que realmente precisam e esperam do sistema.

Validação: Ao envolver o cliente no processo de definição, é possível validar os requisitos à medida que são desenvolvidos, garantindo que o sistema atenda às suas necessidades.

Priorização: O cliente pode ajudar a priorizar requisitos com base em sua importância e valor para o negócio.

Redução de Riscos: Ao entender e documentar corretamente os requisitos do cliente desde o início, reduz-se o risco de retrabalho, custos adicionais e insatisfação do cliente no final do projeto.

Relacionamento e Confiança: Envolver o cliente no processo fortalece o relacionamento e constrói confiança, pois eles veem que suas opiniões e necessidades são valorizadas.


## NÃO FUNCIONAIS

um software também tem requisitos que não estão diretamente relacionados à sua função principal, mas são essenciais para atender às necessidades do usuário final.

Definição: Os requisitos não funcionais descrevem as capacidades operacionais do sistema e tentam melhorar sua funcionalidade. Eles abordam aspectos como velocidade, segurança, confiabilidade e integridade dos dados.

Diferença com Requisitos Funcionais: Enquanto os requisitos funcionais definem o que um produto deve fazer (por exemplo, um mensageiro deve permitir a edição de mensagens), os requisitos não funcionais especificam os atributos de qualidade do sistema.

Tipos de Requisitos Não Funcionais:

- Performance e Escalabilidade: Refere-se à rapidez com que o sistema retorna resultados e como essa performance muda com cargas de trabalho maiores.
- Portabilidade e Compatibilidade: Aborda em quais hardwares, sistemas operacionais e navegadores o software funciona e se ele é compatível com outras aplicações.
- Confiabilidade, Manutenibilidade e Disponibilidade: Estes tratam da frequência de falhas críticas, o tempo necessário para corrigir problemas e a probabilidade de o sistema estar acessível a qualquer momento.
- Segurança: Garante que todos os dados dentro do sistema sejam protegidos contra ataques maliciosos ou acesso não autorizado.
- Localização: Define quão bem um sistema se alinha com o contexto do mercado local, incluindo idiomas, leis, moedas, entre outros.
- Usabilidade: Aborda a facilidade de uso do produto.

Recomendações Gerais:

- Tornar os RNFs mensuráveis e testáveis.
- Definir requisitos para componentes do sistema e não apenas para produtos inteiros.
- Vincular RNFs a objetivos de negócios.
- Considerar limitações de terceiros e arquitetônicas.
- Consultar padrões e guias existentes.

# ENTENDENDO NÓS E TÓPICOS

O sistema ROS 2 (Robot Operating System) é composto por uma série de conceitos fundamentais que, juntos, formam a estrutura de grafo do ROS (2). Este grafo é uma rede de elementos ROS 2 que processam dados simultaneamente. Se fossemos visualizar este grafo, ele englobaria todos os executáveis e as conexões entre eles.

Um "nó" é um dos principais elementos do ROS 2. Cada nó deve ser responsável por uma única função modular. Por exemplo, um nó pode ser responsável por controlar os motores das rodas ou por publicar dados de sensores, como um laser range-finder. Os nós podem enviar e receber dados de outros nós através de tópicos, serviços, ações ou parâmetros. Um sistema robótico completo é composto por muitos nós trabalhando em conjunto. Em ROS 2, um único executável (programa C++, programa Python, etc.) pode conter um ou mais nós.

O ROS 2 utiliza tópicos como um dos principais meios de comunicação entre nós. Os tópicos permitem que os dados sejam transmitidos entre nós, possibilitando a interação e a execução de tarefas complexas em sistemas robóticos. Aqui está um guia sobre como os tópicos funcionam no ROS 2, com base no tutorial fornecido.

# PACOTES EM ROS

O workspace de ROS é basicamente uma pasta onde se concentram um ou mais pacotes ROS. Ela é útil pois podemos juntar vários pacotes e compilá-los com apenas um comando e também dar apenas um source para adicionar os comandos de run/launch ao nosso sistema.


Em ROS (Robot Operating System), um pacote é a unidade básica de organização de software. Ele é um diretório que contém todo o código-fonte, arquivos de configuração, dependências e outros recursos necessários para realizar uma função específica. Os pacotes são a maneira padrão de organizar e compartilhar código em ROS, e eles facilitam a modularidade e a reutilização de software.

Cada pacote em ROS é estruturado de acordo com convenções específicas. Um pacote geralmente inclui os seguintes elementos:

1. **Código-fonte:** Os scripts, programas ou bibliotecas que realizam tarefas específicas relacionadas ao robô ou sistema controlado pelo ROS.

2. **Arquivos de configuração:** Arquivos YAML ou XML que especificam configurações específicas do pacote.

3. **Manifesto do pacote (package.xml):** Um arquivo XML que fornece informações sobre o pacote, como nome, versão, descrição e dependências.

4. **Lançadores (launch files):** Arquivos XML que especificam como iniciar vários componentes do pacote e suas configurações.

5. **Diretório de dependências:** Se o pacote depender de outros pacotes, geralmente há um diretório que lista essas dependências.

6. **Recursos adicionais:** Outros recursos, como modelos 3D, mapas, dados de calibração, entre outros, que são necessários para o funcionamento do pacote.

Ao organizar o código em pacotes, os desenvolvedores podem criar sistemas ROS mais modulares, facilitando o desenvolvimento, teste e manutenção do software. Além disso, a modularidade dos pacotes torna mais fácil compartilhar e reutilizar componentes de software entre diferentes projetos e comunidades na plataforma ROS.


# LAUNCH FILES

Um launch file nada mais é do que um script em Python que automatiza o processo de rodar diversos nós/pacotes. É muito comum que um sistema complexo desenvolvido em ROS seja composto por diversos pacotes diferentes, uma ou mais workspaces e diversos nós. Seria tedioso ter que toda vez rodar cada um desses nós um por um. A solução? Criar uma ferramenta capaz de automatizar tudo isso.

Um arquivo de lançamento (launch file) no ROS (Robot Operating System) é um arquivo XML que é usado para iniciar e configurar diferentes componentes de um sistema ROS. Esses arquivos são particularmente úteis para simplificar o processo de inicialização de vários nós (nodes), parâmetros e configurações associadas em um único comando.

Aqui estão alguns conceitos importantes relacionados aos arquivos de lançamento:

1. **Node:** Um nó é uma unidade de execução no ROS. Pode ser um componente de software específico que realiza uma função particular, como controle de motores, processamento de imagem, etc.

2. **Launch File:** Um arquivo de lançamento é usado para iniciar e configurar nós e outros elementos do sistema ROS de uma só vez. Ele fornece uma maneira de configurar vários componentes do sistema de forma consistente.

3. **Launch Node:** É uma tag dentro do arquivo de lançamento que especifica qual nó deve ser iniciado. Pode incluir o nome do nó, o pacote ao qual pertence, o tipo de nó, argumentos e outros parâmetros relevantes.

4. **Namespace:** É uma maneira de agrupar nós e tópicos relacionados em um espaço de nomes específico. Os arquivos de lançamento podem configurar namespaces para evitar conflitos entre diferentes componentes do sistema.

5. **Parameter:** É possível configurar parâmetros para um nó específico usando o arquivo de lançamento. Os parâmetros são valores que afetam o comportamento do nó e podem ser usados para ajustar configurações.

6. **Include Tag:** Permite a inclusão de outros arquivos de lançamento dentro de um arquivo principal, facilitando a modularidade e reutilização de configurações.

Os arquivos de lançamento simplificam a inicialização de sistemas complexos no ROS, facilitando a configuração e a execução de vários componentes com um único comando. Eles são especialmente úteis em sistemas robóticos, onde diferentes nós precisam ser iniciados e configurados para trabalhar em conjunto de maneira coordenada.



# QUATERNIONS

Um dos principais usos práticos dos quaternions é em como eles descrevem a rotação 3d. Estes primeiros dois módulos ajudarão você a construir uma intuição de quais quaternions correspondem a quais rotações 3d, embora exatamente como isso funciona permanecerá, por enquanto, um mistério. Análogo a abrir o capô de um carro pela primeira vez, todas as partes serão expostas a você, especialmente à medida que você examina mais de perto, mas entender como tudo se encaixa virá com o tempo. Aqui estamos apenas olhando para o "o quê", antes do "como" e do "porquê".

Os quaterniões são um tipo especial de número usado em matemática, particularmente na álgebra linear e na representação de rotações tridimensionais. Eles foram inventados por Sir William Rowan Hamilton no século XIX.

Um quaternião é uma extensão dos números complexos e tem a forma geral:

\[ q = a + bi + cj + dk \]

Onde:
- \( a, b, c, \) e \( d \) são números reais.
- \( i, j, \) e \( k \) são chamadas unidades imaginárias, cada uma delas satisfazendo \( i^2 = j^2 = k^2 = -1 \), e \( ij = k \), \( jk = i \), \( ki = j \), \( ji = -k \), \( ik = -j \), \( kj = -i \).

Os quaterniões têm algumas propriedades interessantes, como a não comutatividade da multiplicação. Ou seja, em geral, \( ab \neq ba \) para quaterniões \( a \) e \( b \).

Uma aplicação significativa dos quaterniões está na representação de rotações tridimensionais. Eles são especialmente úteis em computação gráfica, simulações físicas e robótica, onde a representação eficiente e sem singularidades de rotações é crucial.

A forma exponencial dos quaterniões é frequentemente usada para representar rotações. Um quaternião unitário (com norma 1) pode ser escrito como \( q = \cos(\theta/2) + \sin(\theta/2)(xi + yj + zk) \), onde \( \theta \) é o ângulo de rotação e \( (x, y, z) \) é um vetor unitário representando o eixo de rotação. Essa representação é útil porque evita problemas associados a outras representações, como a singularidade dos ângulos de Euler em certos casos.


# SERVIÇOS E AÇÕES EM ROS

Os serviços no ROS 2 são uma forma essencial de comunicação entre os nós. Diferentemente dos tópicos, que operam no modelo de publicação-subscrição, os serviços funcionam com base em um modelo de chamada e resposta. Isso significa que, enquanto os tópicos permitem que os nós se inscrevam em fluxos de dados e recebam atualizações contínuas, os serviços fornecem dados apenas quando são especificamente chamados por um cliente. Aqui está um guia sobre como os serviços funcionam no ROS 2:


Em ROS (Robot Operating System), os serviços são uma forma de comunicação entre nós (nodes) que permite solicitar a execução de tarefas específicas e receber uma resposta. Enquanto os tópicos são usados para comunicação unidirecional (publicação e assinatura) e os parâmetros são usados para armazenar configurações, os serviços são projetados para comunicação bidirecional, onde um nó solicita a execução de uma ação a outro nó e espera por uma resposta.

A estrutura básica de um serviço em ROS envolve dois componentes principais:

1. **Serviço (Service):** O nó que fornece uma funcionalidade específica é chamado de serviço. Ele recebe solicitações, executa a tarefa associada e envia uma resposta de volta ao nó solicitante.

2. **Cliente (Client):** O nó que solicita a execução da tarefa é chamado de cliente. Ele envia uma solicitação para o serviço, aguarda a resposta e, em seguida, pode continuar com base na resposta recebida.

A comunicação entre serviço e cliente é síncrona, o que significa que o cliente envia uma solicitação e espera pela resposta antes de continuar sua execução.

Aqui está um exemplo simplificado de como um serviço pode ser definido em ROS usando Python:

1. **Definindo o serviço (no lado do servidor):**

```python
# Importando as bibliotecas necessárias
from meu_pacote.srv import MinhaSolicitacao, MinhaResposta
from rospy import Service

# Função de tratamento da solicitação
def handle_request(req):
    # Lógica para processar a solicitação
    resultado = req.a + req.b
    print(f"Solicitação recebida: {req.a} + {req.b} = {resultado}")
    
    # Retorna a resposta
    return MinhaResposta(resultado)

# Inicializando o serviço
rospy.init_node('meu_servico')
meu_servico = Service('meu_servico', MinhaSolicitacao, handle_request)
rospy.spin()
```

2. **Chamando o serviço (no lado do cliente):**

```python
# Importando as bibliotecas necessárias
from meu_pacote.srv import MinhaSolicitacao
from rospy import ServiceProxy

# Inicializando o cliente
rospy.init_node('meu_cliente')
meu_servico_proxy = ServiceProxy('meu_servico', MinhaSolicitacao)

# Criando a solicitação
solicitacao = MinhaSolicitacao(a=3, b=4)

# Chamando o serviço e recebendo a resposta
resposta = meu_servico_proxy(solicitacao)

# Imprimindo a resposta
print(f"Resposta recebida: {resposta.resultado}")
```

Neste exemplo, o serviço (lado do servidor) soma dois números e retorna o resultado. O cliente (lado do cliente) cria uma solicitação, a envia para o serviço e recebe a resposta. Este é um exemplo simples, e na prática, os serviços podem ser usados para realizar tarefas mais complexas e diversas em sistemas robóticos.

Ações no ROS 2 são um tipo de comunicação destinado a tarefas de longa duração. Elas são compostas por três partes: um objetivo (goal), feedback e um resultado (result). As ações são construídas sobre tópicos e serviços, oferecendo funcionalidades semelhantes aos serviços, mas com a capacidade de serem canceladas e fornecerem feedback contínuo.



# EXPRESSÕES REGULARES

Expressões regulares, também conhecidas como regex ou regexp, são padrões utilizados para encontrar correspondências em strings de texto. Elas são extremamente poderosas e versáteis, tornando-se uma ferramenta indispensável para programadores, analistas de dados e qualquer pessoa que trabalhe com processamento de texto. Este artigo tem como objetivo fornecer uma introdução detalhada sobre o que são expressões regulares e como usá-las.

1. O que são Expressões Regulares?
Expressões regulares são sequências de caracteres que formam um padrão de busca. Elas são utilizadas para realizar operações de busca e substituição em textos, bem como para validação de formatos de dados. O poder das expressões regulares reside em sua capacidade de descrever padrões complexos de forma concisa.

-r 

# UTILIZANDO O CHATGPT



# LLM 

## TOKENS

Um token nada mais é do que a unidade básica de processamento de texto. Imagine que cada palavra, pontuação ou até mesmo parte de uma palavra é dividida em pequenos pedaços. Cada um desses pedaços é um "token". Os LLMs usam esses tokens para entender e gerar texto, pois eles ajudam o modelo a processar e analisar as informações de forma mais eficiente e detalhada. Simplificando, são como os tijolos que constroem as frases e textos que os LLMs criam ou interpretam.



# Langchain

Conceitos básicos do LangChain

Framework para Modelos de Linguagem: LangChain é uma estrutura de programação destinada ao desenvolvimento de aplicações que utilizam modelos de linguagem. Ele oferece uma interface padrão para "cadeias", facilitando a integração com outras ferramentas e possibilitando cadeias de ponta a ponta para aplicações comuns.

Open Source e Orientado a Dados: Como um framework open source, LangChain permite a criação de experiências personalizadas e enriquecidas ao se conectar com diversas fontes de dados. Ele é descrito como "data-aware" e "agentic", o que significa que as aplicações desenvolvidas com ele podem interagir com o ambiente e conectar-se a outras fontes de dados.

Componentes Modulares: Os principais componentes do LangChain incluem "LLM Wrappers", "Prompt Template" e índices para recuperação de informações relevantes. Esses componentes são blocos de construção modulares, prontos e fáceis de usar para desenvolver aplicações poderosas.

Usos e Aplicações: LangChain é utilizado em várias aplicações, incluindo análise e resumo de documentos, chatbots e análise de código. Isso demonstra sua versatilidade e capacidade de se adaptar a diferentes necessidades e contextos.

Agentes e Ferramentas: Os agentes no LangChain são componentes reutilizáveis que podem executar tarefas específicas, como geração de texto, tradução de idiomas e resposta a perguntas. Além disso, existem ferramentas que são bibliotecas de funções auxiliares no desenvolvimento de diversas aplicações.

Facilitação do Desenvolvimento: O LangChain atua como uma orquestração para o desenvolvimento de aplicações, simplificando o uso de LLMs em diferentes contextos, desde cálculos algébricos até a geração de saídas gráficas.


An open source framework that allows AI developers to combine LLMs like GPT-4 with external sources of computation and data.

Quebro meu documento em chunks e após isso, guardo esses chunks em um banco de vetores.

Components: LLM wrappers, prompt templates, indexes for relevant information retrieval.
Chains: Assemble components to solve a specific task, such as finding info in a book.
Agents: Agents allow LLM's to interact with it's enironment. For instance, make API request with a specfic action.